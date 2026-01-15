def main():
    machines = dict()

    with open('input.txt') as txt:
        for line in txt:
            key, outs = line.split(':')
            outs = set(outs.strip().split())
            machines[key] = outs

    return machines


def count_paths(machines, start='you', end='out'):
    if end in machines[start]:
        return 1
    elif 'out' in machines[start]:
        return 0
    else:
        total = 0
        for next_machine in machines[start]:
            if next_machine != 'out':
                total += count_paths(machines, next_machine, end)
        return total


def list_paths(machines, path=[], start='svr', end='out'):
    path.append(start)
    path_idx = len(path)

    if end in machines[start]:
        if 'fft' in path and 'dac' in path:
            print('+++', path)
            return 1
        else:
            # print('---', path)
            return 0
    elif 'out' in machines[start]:
        return 0
    else:
        total = 0
        for next_machine in machines[start]:
            if next_machine in path:
                print('Cycle detected!', next_machine, path)
                break
            else:
                del path[path_idx:]
                total += list_paths(machines, path, next_machine)
        return total


if __name__ == '__main__':
    machines = main()
    print(count_paths(machines))
    # print(list_paths(machines))
    # print(list_paths(machines, start='dac', end='fft')) # Cycles abound!

    # 4934 - low. Number of paths from dac to out. There are 0 paths from dac to fft.
