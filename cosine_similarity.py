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

baseline = [[0.46785867, 0.51709616, 0.47278127], [0.40887773, 0.57265604, 0.6629583], [0.4054924, 0.4650981, 0.6734771], [0.45224398, 0.6265073, 0.5531765], [0.4420348, 0.40005693, 0.75642467], [0.68867874, 0.74766815, 0.44543105], [0.65519905, 0.31595695, 0.55321544]]
current = [[0.47692168, 0.40884888, 0.6540798], [0.40350756, 0.44656464, 0.6504991], [0.4341948, 0.34083185, 0.7360759], [0.4257486, 0.5135157, 0.39856184], [0.49548003, 0.28694832, 0.47909486], [0.66387886, 0.66587484, 0.35898465], [0.6853894, 0.22712874, 0.4318123]]

baseline_1D = []
for body_point in baseline:
    baseline_1D.append(body_point[1]) # x value
    baseline_1D.append(body_point[0]) # y value

current_1D = []
for body_point in current:
    current_1D.append(body_point[1])
    current_1D.append(body_point[0])


print(cosine_similarity(
    baseline_1D,
    current_1D
))