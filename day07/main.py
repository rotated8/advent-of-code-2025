def main():
    splits = 0
    beams = None
    with open('input.txt') as txt:
        for line in txt:
            if beams == None:
                beams = [False] * len(line)
                beams[line.index('S')] = True
            elif line.find('^') == -1:
                continue
            else:
                beam_idx = [idx for idx, beam in enumerate(beams) if beam]
                for idx in beam_idx:
                    if line[idx] == '^':
                        beams[idx-1]  = True
                        beams[idx] = False
                        beams[idx+1] = True
                        splits += 1

    print(splits)

if __name__ == "__main__":
    main()
