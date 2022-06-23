import numpy as np

# returning True means posture is bad
# returning False means posture is fine

def cosine_similarity(x, y):
    flattened_x = []
    for body_point in x:
        flattened_x.append(body_point[1])
        flattened_x.append(body_point[0])

    flattened_y = []
    for body_point in y:
        flattened_y.append(body_point[1])
        flattened_y.append(body_point[0])

    # Ensure length of x and y are the same
    if len(flattened_x) != len(flattened_y) :
        return None
    
    # Compute the dot product between x and y
    dot_product = np.dot(flattened_x, flattened_y)
    
    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum([elem**2 for elem in flattened_x])) 
    magnitude_y = np.sqrt(np.sum([elem**2 for elem in flattened_y]))
    
    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    if cosine_similarity < 0.9985:
        print("Current pose not similar enough to baseline according to cosine similarity.")
        return True
    return False

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