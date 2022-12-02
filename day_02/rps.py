
ROCK = 1
PAPER = 2
SCISSORS = 3

FIRST_MAPPING = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}

SECOND_MAPPING = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}

RESULT_SCORES = {
    -1: 0,
    0: 3,
    1: 6
}


def calculate_total_score(table):
    scores = (calculate_score(first, second) for first, second in table)
    return sum(scores)


def calculate_score(first, second):
    result = rock_paper_scissors(first, second)
    return second + RESULT_SCORES[result]


def rock_paper_scissors(first, second):
    
    if first == second:
        return 0
    
    if first == SCISSORS and second == ROCK:
        return 1

    if first == ROCK and second == SCISSORS:
        return -1

    if first < second:
        return 1

    return -1


def read_data(fname):

    table = []

    with open(fname) as f:
        for line in f:
            first, second = line.strip().split(' ')
            table.append((FIRST_MAPPING[first], SECOND_MAPPING[second]))

    return table


if __name__ == '__main__':

    assert(15 == calculate_total_score(read_data('data/test_input.txt')))

    print('Total score:', calculate_total_score(read_data('data/input.txt')))