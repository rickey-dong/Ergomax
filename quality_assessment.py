# returning True means bad posture
# returning False means posture is fine

NOSE = 0
LEFT_EYE = 1
RIGHT_EYE = 2
LEFT_EAR = 3
RIGHT_EAR = 4
LEFT_SHOULDER = 5
RIGHT_SHOULDER = 6
Y = 0
X = 1
CONFIDENCE_VALUE = 2
CONFIDENCE_THRESHOLD = 0.26

def check_confidence_thresholds(current):
    if current[NOSE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD:
        # if the model is less than 26% confident about the location of any
        # particular body point, then there's not enough data to make a guess
        # or could mean that the user is severely slouching and has most of the
        # body off camera
        return True
    return False

def check_current_deviations(baseline, current):
    # if current body landmarks y-coords are greater than the baseline,
    # then that means the landmarks are further downwards than ideal, so could
    # be indicative of slouching because it has deviated a lot

    if ((current[LEFT_SHOULDER][Y] >= baseline[LEFT_SHOULDER][Y] + 0.10) or (current[RIGHT_SHOULDER][Y] >= baseline[RIGHT_SHOULDER][Y] + 0.10)):
        return True
    if ((current[LEFT_EAR][Y] >= baseline[LEFT_EAR][Y] + 0.10) or (current[RIGHT_EAR][Y] >= baseline[RIGHT_EAR][Y] + 0.10)):
        return True
    if ((current[LEFT_EYE][Y] >= baseline[LEFT_EYE][Y] + 0.10) or (current[RIGHT_EYE][Y] >= baseline[RIGHT_EYE][Y] + 0.10)):
        return True
    if ((current[NOSE][Y] >= baseline[NOSE][Y] + 0.10)):
        return True
    return False

def check_head_tilt(current):
    # if eyes are at ear level, then head is tilted
    if current[LEFT_EYE][Y] > current[LEFT_EAR][Y] + 0.10:
      return False
    if current[RIGHT_EYE][Y] > current[RIGHT_EAR][Y] + 0.10:
      return False
    return True

def check_slump(current):
    # comparing shoulders vs. eyes
    if current[LEFT_EYE][Y] > current[LEFT_SHOULDER] + 0.10:
        return False
    if current[RIGHT_EYE][Y] > current[RIGHT_SHOULDER] + 0.10:
        return False
    return True