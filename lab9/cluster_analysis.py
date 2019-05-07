from itertools import product
from statistics import median
from copy import deepcopy
import numpy as np


RANGE_OF_EUCLID = 1
RANGE_OF_CHEBYSHEV = 0


class Cluster_Analysis:
    
    def __init__(self, coords_data, coords_clusters, type_of_range):
        self.coords_data = coords_data
        self.coords_clusters = coords_clusters
        self.type_of_range = type_of_range
        self.new_coords_clusters = []
        self.sets = []

    def calculate_range(self):
        list_ranges = []
        func = self.range_of_euclid if self.type_of_range\
                            else self.range_of_chebyshev
        for pare in product(self.coords_data, self.coords_clusters):
            list_ranges.append(func(pare))
        list_ranges = np.array(list_ranges).reshape(len(self.coords_data), len(self.coords_clusters))
        self.create_sets(list_ranges)

    def range_of_euclid(self, coords):
        return ((coords[0][0] - coords[1][0]) ** 2 + (coords[0][1] - coords[1][1]) ** 2) ** 0.5

    def range_of_chebyshev(self, coords):
        return max(abs(coords[0][0] - coords[1][0]), abs(coords[0][1] - coords[1][1]))

    def step(self):
        self.calculate_range()
        if self.equal():
            return (True, self.sets)
        self.coords_clusters = deepcopy(self.new_coords_clusters)
        self.new_coords_clusters.clear()
        return (False, self.coords_clusters)

    def equal(self):
        for coords in zip(self.coords_clusters, self.new_coords_clusters):
            if coords[0][0] != coords[1][0] or coords[0][1] != coords[1][1]:
                return False
        return True

    def create_sets(self, list_ranges):
        self.sets = {i: [] for i in range(len(self.coords_clusters))}
        for i, ranges in enumerate(list_ranges):
            self.sets[list(ranges).index(min(ranges))].append(self.coords_data[i])
        self.culculate_clusters()

    def culculate_clusters(self):
        for i, set in enumerate(self.sets.values()):
            coord_cluster = []
            if len(set) == 0:
                coord_cluster = deepcopy(self.coords_clusters[i])
            else:
                for coord in np.array(set).transpose():
                    coord_cluster.append(median(coord))
            self.new_coords_clusters.append(coord_cluster)


if __name__ == '__main__':
    data = [[143, 213], [180, 220], [183, 249],
            [271, 253], [226, 253], [315, 275], 
            [266, 297]]
    clusters = [[159, 238], [270, 278]]
    cluster_analysis = Cluster_Analysis(data, clusters, RANGE_OF_CHEBYSHEV)
    print(cluster_analysis.step())
    print(cluster_analysis.step())