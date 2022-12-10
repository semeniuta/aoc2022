import numpy as np


class Instruction:
    
    def __init__(self, text):
        text = text.strip()

        self.is_noop = False
        self.addx = None
        
        if text == 'noop':
            self.is_noop = True
            return
        elif text.startswith('addx'):
            self.addx = int(text.split(' ')[-1])
        else:
            raise Exception(f'unreachable: text={text}')


if __name__ == '__main__':

    x = 1
    count = 0
    history = [x, ]

    with open('data/input.txt') as f:
        for line in f:
            instruction = Instruction(line)

            if instruction.is_noop:
                count += 1
                history.append(x)
            else:
                history += [x, x]
                x += instruction.addx
                count += 2

    s = 0
    for i in [20, 60, 100, 140, 180, 220]:
        val = history[i]
        strength = i * val
        s += strength

    print(s)

    pixels = []
    for i in range(1, len(history)):
        val = history[i]
        pos = (i - 1) % 40
        pixel = '#' if (pos >= val - 1 and pos <= val + 1) else '.'
        pixels.append(pixel)

    image = np.array(pixels).reshape((6, 40))

    for i in range(6):
        for j in range(40):
            print(image[i, j], end='')
        print()
