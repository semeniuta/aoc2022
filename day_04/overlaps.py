

def parse_line(line):

    def parse_range(range_s):
        return tuple((int(num_s) for num_s in range_s.split('-')))

    first_s, second_s = line.strip().split(',')

    return (parse_range(first_s), parse_range(second_s))


def range_length(rng):
    a, b = rng
    assert b >= a
    return b - a + 1


def full_overlap_in_ranges(ranges):
    smaller, larger = sorted(ranges, key=range_length)
    return larger[0] <= smaller[0] and larger[1] >= smaller[1]


def count_full_overlaps(fname):

    count = 0

    with open(fname) as f:
        for line in f:
            ranges = parse_line(line)
            if full_overlap_in_ranges(ranges):
                count += 1
    
    return count


if __name__ == '__main__':

    assert 2 == count_full_overlaps('data/test_input.txt')

    print(f"Number of full overlaps: {count_full_overlaps('data/input.txt')}")