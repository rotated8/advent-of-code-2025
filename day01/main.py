def main():
    zeros = 0
    position = 50

    with open('input.txt') as txt:
        for line in txt:
            direction = line[0]
            rotation = int(line[1:])

            if direction.upper() == 'L':
                rotation = -1 * rotation

            position += rotation

            rotations = position // 100

            position += -100 * rotations
            zeros += abs(rotations)


    print(zeros)

if __name__ == '__main__':
    main()

