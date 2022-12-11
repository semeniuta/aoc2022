from collections import deque
import operator
import math

OPERATORS = {
    '+': operator.add,
    '*': operator.mul,
}


class Monkey:

    def __init__(self):
        self.items = deque()
        self.id = None
        self.operation = None
        self.test = None
        self.on_true = None
        self.on_false = None
        self.monkeys = None
        self.n_inspections = 0
    
    def add_items(self, items):
        self.items += items

    def do_round(self):

        #print(f'Round for {self.id}')

        while len(self.items) > 0:

            val = self.items.popleft()
            val = self.operation(val)
            self.n_inspections += 1
            
            target = self.monkeys[self.on_true] if self.test(val) else self.monkeys[self.on_false]
            
            #print(f'Throwing {val} to {target.id}')
            target.items.append(val)

        #print()


def parse_test(test_s):
    
    divisor = int(test_s.split('divisible by')[-1].strip())

    return lambda x: x % divisor == 0


def after_being_bored(initial):
    return int(math.floor(initial / 3))


def parse_operation(op_s):
    right_side_s = op_s.split('new = ')[-1].strip()

    first_s, operator_s, second_s = right_side_s.split(' ')
    operator = OPERATORS[operator_s]

    def old_to_new(old):
        first = old if first_s == 'old' else int(first_s)
        second = old if second_s == 'old' else int(second_s)

        initial = operator(first, second)
        
        return after_being_bored(initial)

    return old_to_new


def parse_target_monkey_index(line):
    return int(line.split('throw to monkey')[-1].strip())


def parse_monkeys(fname):
    
    monkeys = {}
    current_monkey = Monkey()

    with open(fname) as f:

        for line in f:
            if line.startswith('Monkey'):

                if current_monkey.id is not None:
                    monkeys[current_monkey.id] = current_monkey
                
                current_monkey = Monkey()
                id = int(line.strip().split(' ')[-1][:-1])
                current_monkey.id = id

            elif line.startswith('  Starting items'):
                
                numbers_as_strings = line.split('Starting items:')[-1].strip().split(',')
                numbers = [int(n_s.strip()) for n_s in numbers_as_strings]
                current_monkey.add_items(numbers)

            elif line.startswith('  Operation'):

                op_s = line.split('Operation:')[-1].strip()
                operation = parse_operation(op_s)
                current_monkey.operation = operation

            elif line.startswith('  Test'):
                
                test = parse_test(line)
                current_monkey.test = test

            elif line.startswith('    If true'):
                current_monkey.on_true = parse_target_monkey_index(line)

            elif line.startswith('    If false'):
                current_monkey.on_false = parse_target_monkey_index(line)

    monkeys[current_monkey.id] = current_monkey

    for m in monkeys.values():
        m.monkeys = monkeys

    return monkeys


if __name__ == '__main__':

    monkeys = parse_monkeys('data/input.txt')
    
    for _ in range(20):
        for id in sorted(monkeys.keys()):
            m = monkeys[id]
            m.do_round()

    n_inspections = sorted([m.n_inspections for m in monkeys.values()], reverse=True)
    first_highest, second_highest = n_inspections[:2]
    print('Monkey business level: ', first_highest * second_highest)