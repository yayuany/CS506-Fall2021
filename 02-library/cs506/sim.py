def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)


def manhattan_dist(x, y):
    sum = 0
    for i in range(len(x)):
        sunm += abs(x[i]-y[i])

    return sum   

def jaccard_dist(x, y):
    intersection = set(x and y)
    card_i = len(intersection)
    union = set( x or y)
    card_u = len(union)
    if card_i == 0:
        return 0
    elif card_u == 0:
        return 'undefined'
    else:
        return 1 - ((float)card_i /card_u)


def cosine_sim(x, y):
    dot = 0
    x_len = 0
    y_len = 0
    
    for i in x:
        dot += x[i] * y[i]
        x_len += x[i]**2
        y_len += y[i]**2
        
    x_len = xlen**(1/2)
    y_len = ylen**(1/2)
    
    c_product = x_len * y_len
 
    if c_product == 0:
        return 'undefined'
    else:
        return dot / c_product   
 

# Feel free to add more
