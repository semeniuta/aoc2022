import numpy as np


def read_data(fname):

    elves = [[]]
    current = elves[0]
    
    with open(fname) as f:
        for line in f:
            if line == '\n':
                elves.append([])
                current = elves[-1]
            else:
                count = int(line)
                current.append(count)

    return [np.array(numbers) for numbers in elves]


def get_sums(data):
    sums = [np.sum(arr) for arr in data]
    return np.array(sums)


def get_highest_n(arr, n=3):
    arr_sorted = np.array(sorted(arr, reverse=True))
    return arr_sorted[:n]


if __name__ == '__main__':

    assert(24_000 == get_sums(read_data('data/test_input.txt')).max())
    assert(45_000 == get_highest_n(get_sums(read_data('data/test_input.txt'))).sum())

    print('Highest calories: ', get_sums(read_data('data/input.txt')).max())
    print('Sum of top 3 carriers: ', get_highest_n(get_sums(read_data('data/input.txt'))).sum())