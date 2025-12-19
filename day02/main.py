def main():
    total = 0
    with open('input2.txt') as txt:
        for line in txt:
            ranges = line.split(',')
            for r in ranges:
                invalids = process_range(r)
                total += sum(invalids)

    print(total)

def process_range(id_range):
    lower, upper = id_range.split('-', 1)

    if len(lower) % 2 == 0:
        pass

    return [int(lower)]

if __name__ == '__main__':
    main()
