from collections import defaultdict

def main():
    machines = dict()

    with open('input.txt') as txt:
        for line in txt:
            key, outs = line.split(':')
            outs = set(outs.strip().split())
            machines[key] = outs

    return machines

def paths(machines, start='you'):
    if 'out' in machines[start]:
        return 1
    else:
        total = 0
        for out in machines[start]:
            total += paths(machines, out)
        return total

if __name__ == "__main__":
    machines = main()
    print(paths(machines))
