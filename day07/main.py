def main():
    splits = 0
    paths = None

    with open('input.txt') as txt:
        for line in txt:
            if paths == None:
                # First line setup
                paths = [0] * len(line)
                paths[line.index('S')] = 1

                #vis = line.strip()
                #print(vis)
                #print(vis.replace('S', '1'))
            elif line.find('^') == -1:
                # Skip work on lines without splitters
                continue
            else:
                beam_idx = {idx for idx, beam in enumerate(paths) if beam > 0}
                split_idx = {idx for idx, char in enumerate(line) if char == '^'}
                for idx in beam_idx & split_idx:
                    splits += 1
                    paths_to_here = paths[idx]
                    paths[idx] = 0
                    paths[idx-1] += paths_to_here
                    paths[idx+1] += paths_to_here

                #vis = line.strip()
                #for idx in {idx for idx, beam in enumerate(beams) if beam}:
                #    vis = vis[:idx] + '|' + vis[idx+1:]
                #print(vis)
                #print(vis.replace('^', '.'))

    print('Splits:', splits)
    print('Paths:', sum(paths))

if __name__ == "__main__":
    main()
