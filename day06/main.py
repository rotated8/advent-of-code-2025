from math import prod


def pt1():
    with open('input.txt') as txt:
        lines = []
        for line in txt:
            lines.append(line.split())

    # Change the lines into columns, putting one problem into each line.
    problems = zip(*lines)

    total = 0
    for p in problems:
        # Pull the operator off the end
        op = p[-1]
        # Change all the numbers into ints.
        p = list(map(int, p[:-1]))

        if op == '+':
            total += sum(p)
        elif op == '*':
            total += prod(p)

    print(total)


class Prob:
    __slots__ = ('op', 'nums')

    def __init__(self, operator, number=None):
        self.op = operator
        self.nums = []
        if number is not None:
            self.nums.append(number)

    def solve(self):
        if self.op == '+':
            return sum(self.nums)
        elif self.op == '*':
            return prod(self.nums)


def pt2():
    with open('input.txt') as txt:
        lines = []
        for line in txt:
            lines.append(list(line))

    # Transpose lines into columns.
    lines = zip(*lines)

    total = 0
    problem = None
    for line in lines:
        # Always a 'blank' line between problems (newlines at the end).
        # Work on one problem at a time, then solve and add the total at the end.
        if len(''.join(line).strip()) == 0:
            total += problem.solve()
        # Always an operator at the end of the line for new problems.
        elif line[-1] == '*' or line[-1] == '+':
            op = line[-1]
            num = int(''.join(line[:-1]).strip())
            problem = Prob(op, num)
        # Everything else is a number.
        else:
            num = int(''.join(line).strip())
            problem.nums.append(num)

    print(total)


if __name__ == '__main__':
    pt2()
