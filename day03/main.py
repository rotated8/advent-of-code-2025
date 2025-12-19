def main():
    total= 0

    with open('input.txt') as txt:
        for line in txt:
            total += bank(line)

    print(total)

def bank(line):
    for i in reversed(range(10)):
        idx = line.find(str(i))
        if idx != -1 and idx != len(line)-1:
            subline = line[idx+1:]
            for j in reversed(range(10)):
                jdx = subline.find(str(j))
                if jdx != -1:
                    return int(f"{i}{j}")


if __name__ == "__main__":
    main()
