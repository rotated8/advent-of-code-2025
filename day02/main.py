def main():
    total = 0
    with open('input.txt') as txt:
        for line in txt:
            ranges = line.split(',')
            for r in ranges:
                # invalids = process_range(r)
                invalids = process_relaxed_range(r)
                total += sum(invalids)

    print(total)


def process_range(id_range):
    invalids = []
    lower, upper = id_range.split('-', 1)

    for i in range(int(lower), int(upper) + 1):
        str_i = str(i)
        if len(str_i) % 2 == 0:
            mid = len(str_i) // 2
            if str_i[:mid] == str_i[mid:]:
                invalids.append(i)

    # print(id_range, invalids)
    return invalids


def process_relaxed_range(id_range):
    invalids = []
    lower, upper = id_range.split('-', 1)

    for i in range(int(lower), int(upper) + 1):
        str_i = str(i)
        len_i = len(str_i)

        factors = [1]
        for f in range(2, len_i // 2 + 1):
            if len_i % f == 0:
                factors.append(f)

        substrings = []
        for f in factors:
            substrings.append(str_i[:f] * (len_i // f))
        # print(i, factors, substrings)

        if str_i in substrings and len_i > 1:
            invalids.append(i)

    # print(id_range, invalids)
    return invalids


if __name__ == '__main__':
    main()
