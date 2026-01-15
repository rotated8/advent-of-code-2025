def main():
    zeros = 0
    position = 50

    with open('input.txt') as txt:
        for line in txt:
            direction = line[0]
            rotation = int(line[1:])

            # Hundreds of rotations, cut them out immediately.
            rotations = rotation // 100
            rotation = rotation - 100 * rotations

            if direction.upper() == 'L':
                rotation = -1 * rotation

            new_position = position + rotation
            # Check for negative rotation through zero.
            if position > 0 and new_position < 0:
                rotations += 1
            # Check for landing on zero. Check this BEFORE the one below.
            if new_position == 0:
                rotations += 1
            # Could land on up to 198, so check if we went over.
            if new_position >= 100:
                new_position -= 100
                rotations += 1

            # This does the wrap from negative numbers back to positive.
            new_position = new_position % 100

            # print(f"pos{position}+{rotation}={new_position}: r{rotations} z{zeros}")

            position = new_position
            zeros += rotations

    print(zeros)


if __name__ == '__main__':
    main()
