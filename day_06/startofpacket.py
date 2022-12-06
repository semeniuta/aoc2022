
def find_n_chars_until_unique_line(buf, line_len):

    start = 0
    end = len(buf) - line_len + 1
    
    for i in range(start, end):
        marker_candidate = buf[i:i+line_len]
        char_set = set(marker_candidate)
        if len(char_set) == line_len:
            return i + line_len
    
    return -1


if __name__ == '__main__':

    assert 7 == find_n_chars_until_unique_line('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
    assert 5 == find_n_chars_until_unique_line('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
    assert 6 == find_n_chars_until_unique_line('nppdvjthqldpwncqszvftbrmjlhg', 4)
    assert 10 == find_n_chars_until_unique_line('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
    assert 11 == find_n_chars_until_unique_line('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)

    assert 19 == find_n_chars_until_unique_line('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
    assert 23 == find_n_chars_until_unique_line('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
    assert 23 == find_n_chars_until_unique_line('nppdvjthqldpwncqszvftbrmjlhg', 14)
    assert 29 == find_n_chars_until_unique_line('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
    assert 26 == find_n_chars_until_unique_line('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)

    with open('data/input.txt') as f:
        big_buf = f.readlines()[0]
        print(f'Start of packet after processing {find_n_chars_until_unique_line(big_buf, 4)} characters')
        print(f'Start of message after processing {find_n_chars_until_unique_line(big_buf, 14)} characters')

