import numpy as np
from numpy.linalg import norm

def cosine_similarity(x, y):
    
    # Ensure length of x and y are the same
    if len(x) != len(y) :
        return None
    
    # Compute the dot product between x and y
    dot_product = np.dot(x, y)
    
    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum([elem**2 for elem in x])) 
    magnitude_y = np.sqrt(np.sum([elem**2 for elem in y]))
    
    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity

baseline = [[0.4960996, 0.5102658, 0.6353961], [0.4432935, 0.57239825, 0.83641464], [0.43734393, 0.44828385, 0.8319421], [0.49394357, 0.640354, 0.72638935], [0.4936411, 0.36972532, 0.60835636], [0.79833263, 0.77638644, 0.7641146], [0.79006904, 0.25415683, 0.6782919]]

baseline1 = [[0.48659152, 0.503603, 0.62343895], [0.42386863, 0.5652974, 0.716406], [0.4193141, 0.43999785, 0.7175697], [0.46879053, 0.63120115, 0.5359382], [0.46576607, 0.3434161, 0.8489068], [0.78261966, 0.78129524, 0.7121437], [0.79404783, 0.18842213, 0.64026904]]

baseline2 = [[0.49941748, 0.50965446, 0.50277346], [0.43166062, 0.5755918, 0.64362675], [0.4262874, 0.44895816, 0.86487776], [0.47211942, 0.6511495, 0.7504279], [0.4670753, 0.3597836, 0.84841275], [0.7948104, 0.790205, 0.7409323], [0.7909874, 0.2074605, 0.69042695]]

baseline3 = [[0.5529456, 0.51365256, 0.62834316], [0.48631307, 0.5786584, 0.7831946], [0.48270354, 0.45155165, 0.8582488], [0.53296894, 0.65027225, 0.68029296], [0.5254053, 0.36130875, 0.7828949], [0.8389382, 0.78675216, 0.57796973], [0.827737, 0.24585842, 0.5496201]]

baseline4 = [[0.5589591, 0.5165766, 0.47601086], [0.490277, 0.58398306, 0.6451709], [0.49012458, 0.45202106, 0.8118346], [0.53058064, 0.657436, 0.7614924], [0.5280209, 0.36101183, 0.77523136], [0.82744616, 0.7894602, 0.48548883], [0.8328347, 0.2581765, 0.37181216]]

obvious_slouching = [[0.5282619, 0.40452465, 0.119273804], [0.49720675, 0.3222111, 0.38576388], [0.5141883, 0.43208766, 0.17543879], [0.49832517, 0.3344543, 0.27941546], [0.50909424, 0.48439753, 0.21113776], [0.6484338, 0.26980793, 0.1967913], [0.5999718, 0.5747812, 0.2074933]]

slight_slouch_0 = [[0.67690206, 0.47169527, 0.608212], [0.60946167, 0.5360638, 0.7442839], [0.6049252, 0.40590352, 0.69451267], [0.642441, 0.6075157, 0.62824327], [0.6394682, 0.31064707, 0.62799436], [0.84937775, 0.6671028, 0.3738962], [0.85265386, 0.24614781, 0.48067233]]

slight_slouch_1 = [[0.7386446, 0.48924848, 0.7191982], [0.66821116, 0.54828185, 0.5906321], [0.6761819, 0.41619503, 0.7148208], [0.6956986, 0.61379814, 0.47199476], [0.7094528, 0.3249342, 0.6225127], [0.8498914, 0.675611, 0.39530566], [0.8594503, 0.28035623, 0.57008904]]

tilt_head_down = [[0.6590723, 0.49912176, 0.40654266], [0.5757103, 0.57754946, 0.6399062], [0.57358336, 0.42903516, 0.7676299], [0.556957, 0.649444, 0.412279], [0.5443812, 0.33340544, 0.5429771], [0.8528627, 0.756698, 0.42355123], [0.83910406, 0.24717787, 0.46706617]]

tilt_head_up = [[0.46217757, 0.527704, 0.50679135], [0.4434143, 0.59034467, 0.77666074], [0.44540057, 0.47004336, 0.73769724], [0.5911541, 0.6705059, 0.51646173], [0.58820593, 0.3732047, 0.43364456], [0.8419714, 0.7592106, 0.44546837], [0.8291291, 0.2679475, 0.36668715]]

baseline_1D = []
for body_point in baseline:
    baseline_1D.append(body_point[1]) # x value
    baseline_1D.append(body_point[0]) # y value

baseline1_1D = []
for body_point in baseline1:
    baseline1_1D.append(body_point[1])
    baseline1_1D.append(body_point[0])

baseline2_1D = []
for body_point in baseline2:
    baseline2_1D.append(body_point[1])
    baseline2_1D.append(body_point[0])

baseline3_1D = []
for body_point in baseline3:
    baseline3_1D.append(body_point[1])
    baseline3_1D.append(body_point[0])

baseline4_1D = []
for body_point in baseline4:
    baseline4_1D.append(body_point[1])
    baseline4_1D.append(body_point[0])

obv_slouch = []
for body_point in obvious_slouching:
    obv_slouch.append(body_point[1])
    obv_slouch.append(body_point[0])

ss_0 = []
for body_point in slight_slouch_0:
    ss_0.append(body_point[1])
    ss_0.append(body_point[0])

ss_1 = []
for body_point in slight_slouch_1:
    ss_1.append(body_point[1])
    ss_1.append(body_point[0])

thd = []
for body_point in tilt_head_down:
    thd.append(body_point[1])
    thd.append(body_point[0])

thu = []
for body_point in tilt_head_up:
    thu.append(body_point[1])
    thu.append(body_point[0])

print(cosine_similarity(
    baseline4_1D,
    thu
))

# baseline vs baseline1:
    # 0.9993298873807803
# baseline vs baseline2:
    # 0.9995551628420549
# baseline vs baseline3:
    # 0.9993965149468059
# baseline vs baseline4:
    # 0.9993758514179505
# baseline vs obv_slouch:
    # 0.9302857957633502
# baseline vs slight slouch 0:
    # 0.9860961310786217
# baseline vs slight slouch 1:
    # 0.9799234224135736
# baseline vs tilted head down:
    # 0.9944372962466497
# baseline vs tilted head up:
    # 0.9981608678334515

# baseline1 vs baseline2:
    # 0.9999051999294907
# baseline1 vs baseline3:
    # 0.9987372419759251
# baseline1 vs baseline4:
    # 0.9985801217768151
# baseline1 vs obv_slouch:
    # 0.9184389536888734
# baseline1 vs slight slouch 0:
    # 0.9838410572177648
# baseline1 vs slight slouch 1:
    # 0.976755503010334
# baseline1 vs tilted head down:
    # 0.9932992471947993
# baseline1 vs tilted head up:
    # 0.9967983804758207

# baseline2 vs baseline3:
    # 0.9988139684856572
# baseline2 vs baseline4:
    # 0.9987056973091837
# baseline2 vs obv_slouch:
    # 0.9206884132292462
# baseline2 vs slight slouch 0:
    # 0.9836410547149325
# baseline2 vs slight slouch 1:
    # 0.9766708396910859
# baseline2 vs tilted head down:
    # 0.9934051477158049
# baseline2 vs tilted head up:
    # 0.9967966870799277

# baseline3 vs baseline4:
    # 0.9999523661478198
# baseline3 vs obv_slouch:
    # 0.9338583110680306
# baseline3 vs slight slouch 0:
    # 0.9909484809541146
# baseline3 vs slight slouch 1:
    # 0.9855980132694753
# baseline3 vs tilted head down:
    # 0.9973124424898395
# baseline3 vs tilted head up:
    # 0.9977737226929116

# baseline4 vs obv_slouch:
    # 0.9347970064728127
# baseline4 vs slight slouch 0:
    # 0.9910460682753853
# baseline4 vs slight slouch 1:
    # 0.9858846053353258
# baseline4 vs tilted head down:
    # 0.9974504234066857
# baseline4 vs tilted head up:
    # 0.997610859544836