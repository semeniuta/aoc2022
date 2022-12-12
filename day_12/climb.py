import numpy as np
import math


class Graph:
    def __init__(self):
        self.adj = {}
        self.unvisited = set()
        self.distances = {}
        self.end_node = None

    def add_node(self, node, neighbors):
        self.adj[node] = neighbors
        self.unvisited.add(node)
        self.distances[node] = math.inf

    def mark_start(self, start_node):
        self.distances[start_node] = 0

    def mark_end(self, end_node):
        self.end_node = end_node

    def do_dijkstra(self):

        while self.end_node in self.unvisited:
            condidates = ((cand, self.distances[cand]) for cand in self.unvisited)
            condidates_sorted = list(sorted(condidates, key=lambda cand: cand[1]))
            node, _ = condidates_sorted[0]

            neighbors = self.adj[node]
            for nb in neighbors:
                new_d = self.distances[node] + 1
                if new_d < self.distances[nb]:
                    self.distances[nb] = new_d

            self.unvisited.remove(node)


def get_neighbors(data_numbers, coordinate):

    i, j = coordinate

    neighbors = []

    for n_i, n_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if n_i < 0 or n_j < 0:
            continue

        if n_i >= data_numbers.shape[0] or n_j >= data_numbers.shape[1]:
            continue

        val = data_numbers[i, j]
        neighbor_val = data_numbers[n_i, n_j]
        if can_move(val, neighbor_val):
            neighbors.append((n_i, n_j))

    return neighbors


def can_move(val, neighbor):
    return neighbor <= val or neighbor - val == 1


if __name__ == '__main__':
    
    with open('data/input.txt') as f:
        data = np.array([list(line.strip()) for line in f])

        start = tuple(np.argwhere(data == 'S')[0])
        end = tuple(np.argwhere(data == 'E')[0])

        data[start[0], start[1]] = 'a'
        data[end[0], end[1]] = 'z'

        data_numbers = np.vectorize(lambda c: ord(c) - ord('a'))(data)

        g = Graph()

        n_rows, n_cols = data_numbers.shape
        for i in range(n_rows):
            for j in range(n_cols):
                node = (i, j)
                neighbors = get_neighbors(data_numbers, node)
                g.add_node(node, neighbors)

        g.mark_start(start)
        g.mark_end(end)

        g.do_dijkstra()

        print(g.distances[g.end_node])