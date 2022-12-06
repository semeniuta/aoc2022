from collections import deque


def parse_level(line):
    line = line[:-1]
    values = tuple((line[i] for i in range(1, len(line), 4)))
    return values


def create_stacks(raw_levels):

    stack_names = raw_levels[-1]
    raw_levels_actual = raw_levels[:-1]
    indices = range(len(stack_names))

    stacks = {name: deque(reversed([level[i] for level in raw_levels_actual if level[i] != ' '])) for i, name in zip(indices, stack_names)}

    return stacks


def parse_command(command_s):
    elements = command_s.strip().split(' ')
    num = int(elements[1])
    src = elements[3]
    dst = elements[5]
    return num, src, dst


def rearrange(stacks, commands, preserve_order):
    
    for num, src, dst in commands:
        src_stack = stacks[src]
        dst_stack = stacks[dst]

        if preserve_order:
            popped = reversed([src_stack.pop() for _ in range(num)])
            dst_stack += popped
        else:
            for _ in range(num):
                val = src_stack.pop()
                dst_stack.append(val)


def find_tops(fname, preserve_order):

    with open(fname) as f:

        levels = []
        for line in f:
            if line == '\n':
                break
            level = parse_level(line)
            levels.append(level)

        commands = [parse_command(line) for line in f]

    stacks = create_stacks(levels)
    rearrange(stacks, commands, preserve_order)

    tops = [stacks[k][-1] for k in sorted(stacks.keys())]
    return ''.join(tops)


if __name__ == '__main__':

    assert('CMZ' == find_tops('data/test_input.txt', preserve_order=False))
    assert('MCD' == find_tops('data/test_input.txt', preserve_order=True))

    print('Tops of the stacks:', find_tops('data/input.txt', preserve_order=False))
    print('Tops of the stacks (preserving order):', find_tops('data/input.txt', preserve_order=True))

