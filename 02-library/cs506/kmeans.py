from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    return [sum(point[i] for point in points) / len(points) for i in range(len(points[0]))]
            


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    
    clusters = list(set(assignments))
    cluster.sort()
    centers = []

    for i in centers:
        points = []
        for i in range(len(dataset)):
            if assignments[i] == i:
                points.append(dataset[i])
        centers.append(point_avg(points))

    return centers
    

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return sim.euclidean_dist(a,b)

def distance_squared(a, b):
    return distance(a,b)**2
    

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    idx = list(range(len(dataset)))
    random.shuffle(idx)
    points = idx[:k]
    init_pts = []
    
    for i in points:
        init_pts.append(dataset[idx])

    return init_pts
    

def cost_function(clustering):
    sum = 0 
    for cluster in clustering.values():
        mean = point_avg(cluster)
        for point in cluster:
            sum += distance_squared(point,mean)
    return sum



def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = []
    centers.append(dataset[random.randint(0,len(dataset)-1)])

    for c in range(k-1):
        dist = []
        for point in dataset:
            min_dist = inf
            for centroid in centers:
                min_dist = min(min_dist,distance(point,centroid))
                dist.append(min_dist**2)
                next_center_idx = find_min_dist(dist)
                centers.append(dataset[next_center_idx])
    return centers

def find_min_dist(dist):
    total = sum(dist)
    rand_sum = random.randint(0,total)
    threshold = 0
    result = -1

    for i, val in enumerate(dist):
        threshold += val
        if rand_sum <= threshold:
            result = 1
            break

    return result






def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
