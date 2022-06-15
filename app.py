import cv2
# import tensorflow as tf
# import tensorflow_hub as hub
# import numpy as np
# from numpy.linalg import norm

"""
Load model from TensorFlow Hub.
There are a wide variety of models to choose from
such as: "movenet_lightning", "movenet_thunder",
"movenet_lightning_f16.tflite", "movenet_thunder_f16.tflite",
"movenet_lightning_int8.tflite", and "movenet_thunder_int8.tflite".


We'll choose "movenet_lightning".
"""

# model = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
# movenet = model.signatures['serving_default']

# NOSE = 0
# LEFT_EYE = 1
# RIGHT_EYE = 2
# LEFT_EAR = 3
# RIGHT_EAR = 4
# LEFT_SHOULDER = 5
# RIGHT_SHOULDER = 6
# Y = 0
# X = 1
# CONFIDENCE_VALUE = 2
# CONFIDENCE_THRESHOLD = 0.26

# def feature_extraction(image_file):
#     """
#     takes in an image
#     and
#     returns a list of relevant landmarks
#     with y, x, and confidence values
#     """

#     # run the model!
#     outputs = movenet(image_file)

#     keypoints = outputs['output_0'].numpy()

#     # converting this 4-layered array into something more manageable
#     # i don't think we're too comfortable working with numpy so maybe
#     # better to convert
#     cleaner_2d_array = [ [0]*3 for i in range(7) ]
#     body_part = 0
#     for ary0 in keypoints:
#         for ary1 in ary0:
#             while body_part < 7:
#                 index = 0
#                 for num in keypoints[0][0][body_part]:
#                     cleaner_2d_array[body_part][index] = num
#                     index += 1
#                 body_part += 1

#     return cleaner_2d_array

# baseline_image = tf.io.read_file("baseline.jpg")
# baseline_image = tf.compat.v1.image.decode_jpeg(baseline_image)
# baseline_image = tf.expand_dims(baseline_image, axis=0)
# baseline_image = tf.cast(tf.image.resize_with_pad(baseline_image, 192, 192), dtype=tf.int32)
# keypoints_of_ideal_pose = feature_extraction(baseline_image)

# def calculate_cosine_similarity(ideal, current):
#     A = np.array(ideal)
#     B = np.array(current)
#     cosine = np.sum(A*B, axis=1)/(norm(A, axis=1)*norm(B, axis=1))
#     return cosine

# def has_bad_posture(ideal, current):
#     """
#     takes in two lists of keypoints and confidence values
#     returns true if user has bad posture currently,
#     false otherwise
#     """
#     # useful articles?
#     # https://medium.com/roonyx/pose-estimation-and-matching-with-tensorflow-lite-posenet-model-ea2e9249abbd
#     # https://medium.com/@priyaanka.garg/comparison-of-human-poses-with-posenet-e9ffc36b7427
#     if current[NOSE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[LEFT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[RIGHT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[LEFT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[RIGHT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[LEFT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
#         current[RIGHT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD:
#             # if the model is less than 26% confident about the location of any
#             # particular body point, then there's not enough data to make a guess
#             # or could mean that the user is severely slouching and has most of the
#             # body off camera
#             return 'NOT ENOUGH DATA'
#     cos_sims = calculate_cosine_similarity(ideal, current)
#     for sim_value in cos_sims:
#         if sim_value < 0.4:
#             return 'NOT SIMILAR POSTURE'
#     # if current body landmarks y-coords are greater than the baseline,
#     # then that means the landmarks are further down than ideal, so could
#     # be indicative of slouching
#     if ((current[LEFT_SHOULDER][Y] >= ideal[LEFT_SHOULDER][Y] + 0.01) or (current[RIGHT_SHOULDER][Y] >= ideal[RIGHT_SHOULDER][Y] + 0.01)):
#         return 'BAD POSTURE'
#     if ((current[LEFT_EAR][Y] >= ideal[LEFT_EAR][Y] + 0.01) or (current[RIGHT_EAR][Y] >= ideal[RIGHT_EAR][Y] + 0.01)):
#         return 'BAD POSTURE'
#     return 'NICE'

def read_camera():
    # define a video capture object
    # with the built-in webcam device
    current_frame = 0
    vid = cv2.VideoCapture(0)
    seconds = 4 # every <> seconds take a snapshot of pose
    fps = vid.get(cv2.CAP_PROP_FPS) # gets frame rate attribute
    frames = fps * seconds # every (fps*seconds) frames, take a pic of pose
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
                # image = tf.io.read_file("current_image.jpg")
                # image = tf.compat.v1.image.decode_jpeg(image)
                # image = tf.expand_dims(image, axis=0)

                # # resize and pad the image
                # # the PoseNet model expects 192 by 192 size
                # image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)

                # # extract features
                # keypoints_of_current_pose = feature_extraction(image)
                
                # # quality assessment
                # has_bad_posture(keypoints_of_ideal_pose, keypoints_of_current_pose)
        current_frame += 1
        # press q button to quit
        if cv2.waitKey(1) == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

read_camera()