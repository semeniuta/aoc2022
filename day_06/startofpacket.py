MARKER_SIZE = 4

def find_start_of_packet(buf):

    start = 0
    end = len(buf) - MARKER_SIZE + 1
    
    for i in range(start, end):
        marker_candidate = buf[i:i+MARKER_SIZE]
        char_set = set(marker_candidate)
        if len(char_set) == 4:
            return i + MARKER_SIZE
    
    return -1


if __name__ == '__main__':

    assert 7 == find_start_of_packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    assert 5 == find_start_of_packet('bvwbjplbgvbhsrlpgdmjqwftvncz')
    assert 6 == find_start_of_packet('nppdvjthqldpwncqszvftbrmjlhg')
    assert 10 == find_start_of_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    assert 11 == find_start_of_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')

    with open('data/input.txt') as f:
        big_buf = f.readlines()[0]
        print(f'Start of packet after processing {find_start_of_packet(big_buf)} characters')

