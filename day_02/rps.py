
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = -1
DRAW = 0
WIN = 1

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

REAL_SECOND_MAPPING = {
    'X': -1,
    'Y': 0,
    'Z': 1,
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


def calculate_real_total_score(table):
    scores = (calculate_real_score(first, outcome) for first, outcome in table)
    return sum(scores)


def calculate_real_score(first, outcome):
    second = rock_paper_scissors_inverse(first, outcome)
    return second + RESULT_SCORES[outcome]


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


def rock_paper_scissors_inverse(first, outcome):

    def determine_action(outcome):
    
        if outcome == DRAW:
            return first

        if outcome == WIN:
            return first + 1

        return first - 1

    action = determine_action(outcome)

    if action > SCISSORS:
        action = ROCK
    
    if action < ROCK:
        action = SCISSORS

    return action


def read_data(fname, real=True):

    table = []

    with open(fname) as f:
        for line in f:
            first, second = line.strip().split(' ')
            
            second_value = REAL_SECOND_MAPPING[second] if real else SECOND_MAPPING[second]
            table.append((FIRST_MAPPING[first], second_value))

    return table


if __name__ == '__main__':

    assert(15 == calculate_total_score(read_data('data/test_input.txt', real=False)))
    assert(12 == calculate_real_total_score(read_data('data/test_input.txt', real=True)))

    print('Total score:', calculate_total_score(read_data('data/input.txt', real=False)))
    print('Total score (real):', calculate_real_total_score(read_data('data/input.txt', real=True)))
