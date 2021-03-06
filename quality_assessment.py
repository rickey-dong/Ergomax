import math

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
SENSITIVITY = 0.09

def check_confidence_thresholds(current):
    # if the model is less than 26% confident about the location of any
    # particular body point, then there's not enough data to make a guess
    # or could mean that the user is severely slouching and has most of the
    # body off camera

    if current[NOSE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_EYE][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_EAR][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[LEFT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD or \
    current[RIGHT_SHOULDER][CONFIDENCE_VALUE] < CONFIDENCE_THRESHOLD:
        print("Model cannot detect body landmarks with certainty.")
        return True
    return False

def check_current_deviations(baseline, current):
    # if current body landmarks y-coords are greater than the baseline,
    # then that means the landmarks are further downwards than ideal, so could
    # be indicative of slouching because it has deviated a lot

    if ((current[LEFT_SHOULDER][Y] >= baseline[LEFT_SHOULDER][Y] + 0.10) or (current[RIGHT_SHOULDER][Y] >= baseline[RIGHT_SHOULDER][Y] + 0.10)):
        print("Shoulders in current pose are more downwards than baseline.")
        return True
    if ((current[LEFT_EAR][Y] >= baseline[LEFT_EAR][Y] + 0.10) or (current[RIGHT_EAR][Y] >= baseline[RIGHT_EAR][Y] + 0.10)):
        print("Ears in current pose are more downwards than baseline.")
        return True
    if ((current[LEFT_EYE][Y] >= baseline[LEFT_EYE][Y] + 0.10) or (current[RIGHT_EYE][Y] >= baseline[RIGHT_EYE][Y] + 0.10)):
        print("Eyes in current pose are more downwards than baseline.")
        return True
    if ((current[NOSE][Y] >= baseline[NOSE][Y] + 0.10)):
        print("Nose in current pose is more downwards than baseline.")
        return True
    return False

def get_ratio(pose):
    left_eye = pose[LEFT_EYE]
    right_eye = pose[RIGHT_EYE]
    eye_width = math.dist([left_eye[X], left_eye[Y]], [right_eye[X], right_eye[Y]])

    left_shoulder = pose[LEFT_SHOULDER]
    right_shoulder = pose[RIGHT_SHOULDER]
    shoulder_width = math.dist([left_shoulder[X], left_shoulder[Y]], [right_shoulder[X], right_shoulder[Y]])

    ratio = eye_width / shoulder_width
    return ratio

def compare_ratios(baseline, current):
    baseline_ratio = get_ratio(baseline)
    current_ratio = get_ratio(current)

    # if user is within SENSITIVITY% of being considered slouching
    # ex: difference in ratios is greater than 9% then it deviates a lot
    if (current_ratio > baseline_ratio * (1 + SENSITIVITY)) or (current_ratio < baseline_ratio * (1 - SENSITIVITY)):
        print("Ratios of baseline pose vs current pose differ by more than 9%.")
        return True
    return False