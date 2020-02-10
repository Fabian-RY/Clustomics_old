# -*- coding: utf-8 -*-

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib

def cluster(array, num_clusters, distance_type, linkage_type):
    algorithm = AgglomerativeClustering(
                                        linkage=linkage_type,
                                        n_clusters=num_clusters,
                                        affinity=distance_type)
    algorithm.fit(array)
    validation = silhouette_score(array, algorithm.labels_, metric=distance_type)
    return (algorithm.labels_, validation)
    

def plot(array, labels):
    if len(array[0]) != 2:
        return None
    with matplotlib.pyplott as plt:
        pass