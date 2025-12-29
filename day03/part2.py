NUM_LEN = 12

def main():
    total= 0

    with open('input.txt') as txt:
        for line in txt:
            line = line.strip()
            line_array = [ i for i in line ]
            total += bank(line_array)

    print(total)

def bank(line_array):
    num = []
    start_range = 0
    array_length = len(line_array)

    if NUM_LEN > array_length:
        raise AttributeError("Not enough digits in the bank")

    # Create a range so that there are NUM_LEN slices of the array.
    for end_range in range(array_length - NUM_LEN, array_length):
        # Check bounds for fast case
        if start_range == end_range:
            num.extend(line_array[start_range:])
            break
        # Slice the line, keeping the end of the range.
        line_slice = line_array[start_range:end_range+1]
        # Find the largest number in the slice, add it to our bank number.
        m = max(line_slice)
        num.append(m)
        # Move the start of the next slice so it does not include the selected number.
        i = line_slice.index(m)
        start_range += i+1

    return int(''.join(num))

if __name__ == "__main__":
    main()
