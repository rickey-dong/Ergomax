###
##
# VIDEO CAPTURING

import cv2

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
        feature_extraction(img_file)
        #
        ##
        ###
    
    count += 1
    cap.set(cv2.CAP_PROP_POS_FRAMES, count) #?

    # press q button to quit

    if cv2.waitKey(1) == ord('q'):
        break
#
##
###

def feature_extraction(image_file):
    """
    takes in an image
    and
    returns a list of all landmarks
    with x, y, and confidence values
    """
    