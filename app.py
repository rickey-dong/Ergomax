import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

###
##
# VIDEO CAPTURING

# define a video capture object
# with the built-in webcam device
vid = cv2.VideoCapture(0)

count = 0
path = "./"
seconds = 50

# every 50 ticks? read an image from the webcam

while True:
    ret, frame = cap.read()
    # ret is True or False
    # frame is the actual snapshot

    if count % seconds == 0:
        cv2.imwrite(path + "current_image.jpg")
        ###
        ##
        # BEGIN FEATURE EXTRACTION
        # (labeling the eyes, nose, etc.)
        
        image = tf.io.read_file("current_image.jpg")
        image = tf.image.decode_jpeg(image)

        keypoints_of_current_pose = feature_extraction(image)
        
        #
        ##
        ###
        
        # quality assessment

        has_bad_posture(keypoints_of_ideal_pose, keypoints_of_current_pose)
    
    count += 1
    cap.set(cv2.CAP_PROP_POS_FRAMES, count) # ?

    # press q button to quit

    if cv2.waitKey(1) == ord('q'):
        break
#
##
###

"""
Load model from TensorFlow Hub.
There are a wide variety of models to choose from
such as: "movenet_lightning", "movenet_thunder",
"movenet_lightning_f16.tflite", "movenet_thunder_f16.tflite",
"movenet_lightning_int8.tflite", and "movenet_thunder_int8.tflite".


We'll choose "movenet_lightning".
"""

module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
input_size = 192 # ?

def feature_extraction(image_file):
    """
    takes in an image
    and
    returns a list of all landmarks
    with x, y, and confidence values
    """
    ### resize to expected input solution of the model ### to be cont.
    
    model = module.signatures['serving_default']

    # movenet_lightning expects tensor type of int32
    image_file = tf.cast(input_image, dtype=tf.int32)

    # run the model!
    outputs = model(image_file)

    keypoints_with_scores = outputs['output_0'].numpy()

    # converting this 4-layered array into 2d array that is 17 by 3
    cleaner_2d_array = [ [0]*3 for i in range(17) ]
    for ary0 in keypoints_with_scores:
        for ary1 in ary0:
            row = 0
            for xyz in ary1:
                index = 0
                for num in xyz:
                    cleaner_2d_array[row][index] = num
                    index += 1
                row += 1

    return cleaner_2d_array

def has_bad_posture(ideal, current):
    """
    returns true if user has bad posture currently,
    false otherwise
    """
    # MATH
    # A LOT OF MATH
    pass