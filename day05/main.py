class FreshRange():
    def __init__(self, freshrange):
        lower, _ , higher = freshrange.partition('-')
        lower, higher = int(lower), int(higher)

        if lower > higher:
            raise AttributeError('wrong way round.')

        self.low = lower
        self.high = higher

    def in_range(self, num):
        if self.low <= num <= self.high:
            return True
        return False

    def __repr__(self):
        return f"{self.low}-{self.high}"

def main():
    # Setup
    ranges = []
    ids = []
    with open('input.txt') as txt:
        for line in txt:
            if line.find('-') != -1:
                ranges.append(FreshRange(line))
            elif line != '\n':
                ids.append(int(line))

    # Compare ids in ranges
    fresh = set()
    for r in ranges:
        for i in ids:
            if r.in_range(i):
                fresh.add(i)

    print(len(fresh))

if __name__ == "__main__":
    main()
