from itertools import product

class Machine:
    def __init__(self, manual_line):
        # Manual lines are like "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
        end_of_ind = manual_line.index(']') # <-- Allows us to pull the substring "[.##."
        self.indicators = [False] * (end_of_ind-1) # Subtract the open bracket off the front
        self.configured = manual_line[1:end_of_ind]

        start_of_jolt = manual_line.index('{') # <-- Allows us to pull the substring "{3,5,4,7}\n"
        self.joltages = [int(j) for j in manual_line[start_of_jolt+1:-2].split(',')]
        self.jolts = [0] * len(self.joltages)

        self.buttons = []
        # Isolate the buttons, and cut off the end so we don't get an empty split
        buttons = manual_line[end_of_ind+2:start_of_jolt-2].split(') ')
        for button in buttons:
            # Slice the open parens off the front, the rest are comma-separated ints.
            self.buttons.append({int(i) for i in button[1:].split(',')})

    def show_indicators(self):
        rep = []
        for ind in self.indicators:
            if ind:
                rep.append('#')
            else:
                rep.append('.')

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

    def bruteforce_joltages(self):
        seq_size = max(self.joltages)
        while True:
            for combo in product(range(len(self.buttons)), repeat=seq_size):
                for button_idx in set(combo):
                    button_count = combo.count(button_idx)
                    for jolts_idx in self.buttons[button_idx]:
                        self.jolts[jolts_idx] += button_count

                if all([i == j for i, j in zip(self.joltages, self.jolts)]):
                    return seq_size
                else:
                    self.jolts = [0] * len(self.jolts)

            seq_size += 1

    def configure_joltages(self):
        seq = Machine.__solve_subjoltage(self.joltages, self.buttons)
        print('!!!', seq)
        return sum([i[0] for i in seq])

    @staticmethod
    def __solve_subjoltage(jolts, buttons):
        min_joltage_idx = jolts.index(min(jolts))
        presses = jolts[min_joltage_idx]
        print(min_joltage_idx, presses, jolts)

        relevant_buttons = [button for button in buttons if min_joltage_idx in button]
        if len(relevant_buttons) == 0:
            print('No relevant buttons to press')
            return [(-1,)]

        remaining_buttons = buttons.copy()
        for button in relevant_buttons:
            remaining_buttons.remove(button)
        print('relevant:', len(relevant_buttons), 'remaining:', len(remaining_buttons))

        for button in relevant_buttons:
            print('Trying', button)
            new_jolts = jolts.copy()
            for jolts_idx in button:
                new_jolts[jolts_idx] -= presses
            new_jolts[min_joltage_idx] = 999

            if len(set(new_jolts)) == 1 and new_jolts[0] == 999:
                print('Configured!')
                return [(presses, button)]
            else:
                print('Next button...')
                subpresses = Machine.__solve_subjoltage(new_jolts, remaining_buttons)
                print(subpresses)
                if subpresses[-1][0] > 0:
                    subpresses.append((presses, button))
                    return subpresses

        print('Out of buttons!')
        return [(-1,)]

def main():
    machines = []
    with open('example.txt') as txt:
        for line in txt:
            machines.append(Machine(line))

    return machines

if __name__ == "__main__":
    machines = main()

    #presses = [m.configure_indicators() for m in machines]
    presses = [m.configure_joltages() for m in machines]
    print(presses)
    print(sum(presses)) # 13633 Minimum!
