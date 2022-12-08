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


def scenic_score(forest, i, j):

    top = np.flip(forest[:i, j])
    bottom = forest[i+1:, j]
    left = np.flip(forest[i, :j])
    right = forest[i, j+1:]

    h = forest[i, j]

    score = 1
    for arr in (top, bottom, left, right):
        higher = arr >= h
        lower = arr < h

        side_score = 0
        if np.all(lower):
            side_score = len(lower)
        else:
            first = np.argmax(higher)
            side_score = first + 1

        score *= side_score

    return score



if __name__ == '__main__':
    
    rows = []
    with open('data/input.txt') as f:
        for line in f:
            numbers = np.array([int(c) for c in line.strip()])
            rows.append(numbers)

    forest = np.array(rows)
    n_rows, n_cols = forest.shape

    n_visible = 2 * n_cols + 2 * (n_rows - 2)
    tree_scenic_score = 0

    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            if is_visible(forest, i, j):
                n_visible += 1

            scenic_score_candidate = scenic_score(forest, i, j)
            if scenic_score_candidate > tree_scenic_score:
                tree_scenic_score = scenic_score_candidate

    print(n_visible, tree_scenic_score)
