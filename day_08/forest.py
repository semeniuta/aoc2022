import numpy as np

def is_visible(forest, i, j):

    top = forest[:i, j]
    bottom = forest[i+1:, j]
    left = forest[i, :j]
    right = forest[i, j+1:]

    h = forest[i, j]

    visible_top = np.all(top < h)
    visible_bottom = np.all(bottom < h)
    visible_left = np.all(left < h)
    visible_right = np.all(right < h)

    return visible_top or visible_bottom or visible_left or visible_right


if __name__ == '__main__':
    
    rows = []
    with open('data/input.txt') as f:
        for line in f:
            numbers = np.array([int(c) for c in line.strip()])
            rows.append(numbers)

    forest = np.array(rows)
    n_rows, n_cols = forest.shape

    n_visible = 2 * n_cols + 2 * (n_rows - 2)

    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            if is_visible(forest, i, j):
                n_visible += 1

    print(n_visible)