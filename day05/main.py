class FreshRange():
    def __init__(self, freshrange):
        lower, _ , higher = freshrange.partition('-')
        self.low = int(lower)
        self.high = int(higher)

    def in_range(self, num):
        if self.low <= num <= self.high:
            return True
        return False

    def amend(self, other):
        if self.low < other.low < self.high and self.low < other.low < self.high:
            # Other's range is in self
            return set()
        elif other.low < self.low < other.high and other.low < self.high < other.high:
            # Self's range is in other
            return {other}
        elif self.low > other.high or self.high < other.low:
            # No overlap
            return {other}
        else:
            # Overlap!
            self.low = min(self.low, other.low)
            self.high = max(self.high, other.high)
            return set()

    def __repr__(self):
        return f"{self.low}-{self.high}"

def main():
    # Setup
    ranges = set()
    ids = set()
    with open('example2.txt') as txt:
        for line in txt:
            if line.find('-') != -1:
                new_range = FreshRange(line)
                print(f"Adding {new_range}")
                new_ranges = set()

                for r in ranges:
                    new_ranges |= new_range.amend(r)
                    print(new_ranges)
                new_ranges.add(new_range)
                print(new_ranges)

                ranges = new_ranges

            elif line != '\n':
                ids.add(int(line))

    # Compare ids in ranges
    fresh = set()
    for r in ranges:
        for i in ids:
            if r.in_range(i):
                fresh.add(i)

    print(len(fresh))

if __name__ == "__main__":
    main()
