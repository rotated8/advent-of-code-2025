from functools import total_ordering

@total_ordering
class FreshRange():
    def __init__(self, freshrange):
        lower, _ , higher = freshrange.partition('-')
        self.low = int(lower)
        self.high = int(higher)

    def __repr__(self):
        return f"{self.low}-{self.high}"

    def __eq__(self, other):
        return self.low == other.low and self.high == other.high

    def __lt__(self, other):
        return self.low < other.low

    def in_range(self, num):
        return self.low <= num <= self.high

    def length(self):
        return self.high - self.low + 1

def main():
    # Setup ranges and ids.
    ranges = []
    ids = set()
    with open('input.txt') as txt:
        for line in txt:
            if line.find('-') != -1:
                ranges.append(FreshRange(line))
            elif line != '\n':
                ids.add(int(line))

    # Flatten ranges
    ranges.sort()
    flattened = [ranges.pop(0)]
    for r in ranges:
        removals = []
        for f in flattened:
            # r.low >= f.low for all f, so if r.low < f.high, we have overlap.
            if r.low <= f.high:
                r.low = min(r.low, f.low)
                r.high = max(r.high, f.high)
                removals.append(f)
        for i in removals:
            flattened.remove(i)
        flattened.append(r)
        flattened.sort()

    # Compare ids in ranges
    fresh = set()
    for i in ids:
        for r in flattened:
            if r.in_range(i):
                fresh.add(i)

    print(len(fresh))

    print(sum([r.length() for r in flattened]))

if __name__ == "__main__":
    main()
