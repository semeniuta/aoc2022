import numpy as np

class Rope:

    def __init__(self):
        self.head = np.array([0, 0])
        self.tail = np.array([0, 0])
        self.visited = {tuple(self.tail), }

    def move(self, dir_vec, length):

        for _ in range(length):

            self.head += dir_vec
            
            diff = self.head - self.tail
            diff_abs = np.abs(diff)

            diff_max = np.max(diff_abs)
            diff_min = np.min(diff_abs)

            if np.abs(diff_max) == 1 or np.abs(diff_max) == 0:
                 continue

            if diff_max == 2 and diff_min == 0:
                self.tail += np.array(diff / 2, dtype=int)
            elif diff_max == 2 and (diff_min == 1 or diff_min == 2):
                movement = np.array([val / 2 if abs(val) == 2 else val for val in diff], dtype=int)
                self.tail += movement
            else:
                raise Exception("unreachable")

            self.visited.add(tuple(self.tail))


class LongRope:

    def __init__(self):
        self.parts = [Rope() for _ in range(9)]

    def move(self, dir_vec, length):

        for _ in range(length):

            self.parts[0].move(dir_vec, 1)

            for i in range(1, 9):
                current = self.parts[i]
                previous = self.parts[i - 1]

                dir_vec_current = previous.tail - current.head
                current.move(dir_vec_current, 1)


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

    with open('data/input.txt') as f:
        commands = [parse_command(line) for line in f]

        big_sim = LongRope()
        for dir_vec, length in commands:
            big_sim.move(dir_vec, length)

    print(len(big_sim.parts[-1].visited))
