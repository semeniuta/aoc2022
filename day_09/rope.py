import numpy as np

class Rope:

    def __init__(self):
        self.head = np.array([0, 0])
        self.tail = np.array([0, 0])
        self.visited = {tuple(self.tail), }

    def move(self, dir_vec, length):

        for _ in range(length):

            head_prev = self.head.copy()
            self.head += dir_vec
            
            dx, dy = np.abs(self.head - self.tail)

            if (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1) or (dx == 0 and dy == 0):
                continue

            self.tail = head_prev
            self.visited.add(tuple(self.tail))


def parse_command(line):
    
    direction, length_s = line.strip().split(' ')

    dir_vec = np.zeros(2)
    if direction == 'L':
        dir_vec = np.array([-1, 0], dtype=int)
    elif direction == 'R':
        dir_vec = np.array([1, 0], dtype=int)
    elif direction == 'U':
        dir_vec = np.array([0, 1], dtype=int)
    elif direction == 'D':
        dir_vec = np.array([0, -1], dtype=int)

    length = int(length_s)

    return dir_vec, length


if __name__ == '__main__':

    with open('data/input.txt') as f:
        commands = [parse_command(line) for line in f]

        sim = Rope()
        for dir_vec, length in commands:
            sim.move(dir_vec, length)

    print(len(sim.visited))

        