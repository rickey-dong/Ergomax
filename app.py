import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import time
import csv

# VIDEO CAPTURING

# define a video capture object
# with the built-in webcam device
vid = cv2.VideoCapture(0)

count = 0
path = "./"
seconds = 50
# every 50 ticks? read an image from the webcam

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

NOSE = 0
LEFT_EYE = 1
RIGHT_EYE = 2
LEFT_EAR = 3
RIGHT_EAR = 4
LEFT_SHOULDER = 5
RIGHT_SHOULDER = 6

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

baseline_image = tf.io.read_file("baseline_image.jpg")
baseline_image = tf.compat.v1.image.decode_jpeg(baseline_image)
baseline_image = tf.expand_dims(baseline_image, axis=0)
baseline_image = tf.cast(tf.image.resize_with_pad(baseline_image, 192, 192), dtype=tf.int32)
keypoints_of_ideal_pose = feature_extraction(baseline_image)

def has_bad_posture(ideal, current):
    """
    returns true if user has bad posture currently,
    false otherwise
    """
    # useful articles?
    # https://medium.com/roonyx/pose-estimation-and-matching-with-tensorflow-lite-posenet-model-ea2e9249abbd
    # https://medium.com/@priyaanka.garg/comparison-of-human-poses-with-posenet-e9ffc36b7427

    good = {}
    bad = {}

    with open(ideal,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            good[row[0]] = [float(row[1]), float(row[2]), float(row[3])]

    with open(current,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            bad[row[0]] = [float(row[1]), float(row[2]), float(row[3])]
            #joint : [x, y, z]

    if ((bad['left_shoulder'][1] >= good['left_shoulder'][1] + 0.01) or (bad['right_shoulder'][1] >= good['right_shoulder'][1] + 0.01)):
        return 'BAD POSTURE'
    if ((bad['left_elbow'][1] >= good['left_elbow'][1] + 0.01) or (bad['right_ear'][1] >= good['right_ear'][1] + 0.01)):
        return 'BAD POSTURE'
    return 'NICE'

print(has_bad_posture('good.csv', 'bad.csv'))

while vid.isOpened():
    ret, frame = vid.read()
    # ret is True or False
    # frame is the actual snapshot
    if ret == False:
        break

    if count % seconds == 0:
        cv2.imwrite(path + "current_image.jpg", frame)
        # BEGIN FEATURE EXTRACTION
        # (labeling the eyes, nose, etc.)
        
        # load the input image
        image = tf.io.read_file("current_image.jpg")
        image = tf.compat.v1.image.decode_jpeg(image)
        image = tf.expand_dims(image, axis=0)

        # resize and pad the image
        # the PoseNet model expects 192 by 192 size
        image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)

        # extract features
        keypoints_of_current_pose = feature_extraction(image)
        
        # quality assessment
        has_bad_posture(keypoints_of_ideal_pose, keypoints_of_current_pose)
    
    count += 1
    time.sleep(1)
    vid.set(cv2.CAP_PROP_POS_FRAMES, count)

    # press q button to quit
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
