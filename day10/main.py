from itertools import product

class Machine:
    def __init__(self, manual_line):
        end_of_ind = manual_line.index(']')
        self.indicators = [False] * (end_of_ind-1)
        self.configured = manual_line[:end_of_ind+1]

        start_of_jolt = manual_line.index('{')
        self.joltages = [int(j) for j in manual_line[start_of_jolt+1:-2].split(',')]
        self.jolts = 0

        self.buttons = []
        buttons = manual_line[end_of_ind+2:start_of_jolt-2].split(') ')
        for button in buttons:
            self.buttons.append({int(i) for i in button[1:].split(',')})

    def show_indicators(self):
        rep = ['[']
        for ind in self.indicators:
            if ind:
                rep.append('#')
            else:
                rep.append('.')
        rep.append(']')

        return ''.join(rep)

    def configure_indicators(self):
        seq_size = 1
        while True:
            for combo in product(range(len(self.buttons)), repeat=seq_size):
                prev = None
                skip = False
                for button in combo:
                    if button == prev:
                        skip = True
                        break
                    else:
                        for idx in self.buttons[button]:
                            self.indicators[idx] = not self.indicators[idx]
                        prev = button

                if not skip and self.show_indicators() == self.configured:
                    return seq_size
                else:
                    self.indicators = [False] * len(self.indicators)
                    skip = False

            seq_size += 1

def main():
    machines = []
    with open('input.txt') as txt:
        for line in txt:
            machines.append(Machine(line))

    presses = [m.configure_indicators() for m in machines]
    print(sum(presses))

    return machines

if __name__ == "__main__":
    main()
