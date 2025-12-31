from math import prod

def main():
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

if __name__ == "__main__":
    main()
