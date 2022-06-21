import cv2
import tensorflow as tf
import tensorflow_hub as hub
from cosine_similarity import *
from quality_assessment import *

"""
Load model from TensorFlow Hub.
There are a wide variety of models to choose from
such as: "movenet_lightning", "movenet_thunder",
"movenet_lightning_f16.tflite", "movenet_thunder_f16.tflite",
"movenet_lightning_int8.tflite", and "movenet_thunder_int8.tflite".


We'll choose "movenet_lightning".
"""

model = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
movenet = model.signatures['serving_default']

def feature_extraction(image_file):
    """
    takes in an image
    and
    returns a list of relevant landmarks
    with y, x, and confidence values
    """

    # run the model!
    outputs = movenet(image_file)

    keypoints = outputs['output_0'].numpy()

    # converting this 4-layered array into something more manageable
    # i don't think we're too comfortable working with numpy so maybe
    # better to convert
    cleaner_2d_array = [ [0]*3 for i in range(7) ]
    body_part = 0
    for ary0 in keypoints:
        for ary1 in ary0:
            while body_part < 7:
                index = 0
                for num in keypoints[0][0][body_part]:
                    cleaner_2d_array[body_part][index] = num
                    index += 1
                body_part += 1

    return cleaner_2d_array

baseline_image = tf.io.read_file("baseline.jpg")
baseline_image = tf.compat.v1.image.decode_jpeg(baseline_image)
baseline_image = tf.expand_dims(baseline_image, axis=0)
baseline_image = tf.cast(tf.image.resize_with_pad(baseline_image, 192, 192), dtype=tf.int32)
keypoints_of_ideal_pose = feature_extraction(baseline_image)

def has_bad_posture(ideal, current):
    """
    takes in two lists of keypoints and confidence values
    returns true if user has bad posture currently,
    false otherwise
    """

    list_of_slouch_checks = []
    list_of_slouch_checks.append(check_confidence_thresholds(current))
    list_of_slouch_checks.append(check_current_deviations(ideal, current))
    #list_of_slouch_checks.append(check_head_tilt_down(current))
    #list_of_slouch_checks.append(check_head_tilt_up(current))
    list_of_slouch_checks.append(compare_ratios(ideal, current))
    list_of_slouch_checks.append(cosine_similarity(ideal, current))

    if any(list_of_slouch_checks):
        return "bad posture"
    else:
        return "posture is fine"

def read_camera():
    # define a video capture object
    # with the built-in webcam device
    current_frame = 0
    vid = cv2.VideoCapture(0)
    seconds = 4 # every <> seconds take a snapshot of pose
    fps = 30 # gets frame rate attribute
    frames = fps * seconds # every (fps*seconds) frames, take a pic of pose
    #bad_posture_true = 0 #
    while vid.isOpened():
        ret, frame = vid.read()
        # ret is True or False
        # frame is the actual snapshot
        if ret == False:
            break
        if current_frame % frames == 0:
            cv2.imwrite("current.jpg", frame)
            # BEGIN FEATURE EXTRACTION
            # (labeling the eyes, nose, etc.)
            
            # load the input image
            image = tf.io.read_file("current.jpg")
            image = tf.compat.v1.image.decode_jpeg(image)
            image = tf.expand_dims(image, axis=0)

            # resize and pad the image
            # the PoseNet model expects 192 by 192 size
            image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)

            # extract features
            keypoints_of_current_pose = feature_extraction(image)
            
            # quality assessment
            print(has_bad_posture(keypoints_of_ideal_pose, keypoints_of_current_pose))
            print("=============================")
        current_frame += 1
        # press q button to quit
        if cv2.waitKey(1) == ord('q'):
            #reports how many checks is performed by the program
            #total_amount of checks = current_frame % frames
            break
    vid.release()
    cv2.destroyAllWindows()
    # percent_spent_in_bad_posture = bad_posture_true/total_amount of checks
read_camera()