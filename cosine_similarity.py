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


print(cosine_similarity(
    [1,1,1,1,1,0,0],
    [0,0,1,1,0,1,1]
))