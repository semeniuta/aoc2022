

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




