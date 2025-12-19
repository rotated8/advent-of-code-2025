class Matrix:
    def __init__(self):
        self.matrix = []
        with open('input.txt') as txt:
            for line in txt:
                row = []
                for char in line:
                    if char == '.':
                        # Must be a 9- using zero would mean a roll with no neighbors would not get counted.
                        # Also, a 9 is not a valid count of the eight neighbors.
                        row.append(9)
                    elif char == '@':
                        row.append(1)
                self.matrix.append(row)

    def sum_adjacents(self):
        for v in range(len(self.matrix)):
            for h in range(len(self.matrix[v])):
                if self.matrix[v][h] != 9:
                    neighbors = []
                    # Cardinals: N,S,E,W
                    neighbors.append(self.get_val(v-1, h))
                    neighbors.append(self.get_val(v+1, h))
                    neighbors.append(self.get_val(v, h+1))
                    neighbors.append(self.get_val(v, h-1))
                    # Diagonals: NE, NW, SE, SW
                    neighbors.append(self.get_val(v-1, h+1))
                    neighbors.append(self.get_val(v-1, h-1))
                    neighbors.append(self.get_val(v+1, h+1))
                    neighbors.append(self.get_val(v+1, h-1))

                    self.matrix[v][h] = sum(neighbors)

    def get_val(self, v, h):
        if v < 0 or h < 0 or v >= len(self.matrix) or h >= len(self.matrix[0]):
            # Out of bounds
            return 0
        elif self.matrix[v][h] == 9:
            # Not a roll, empty space.
            return 0
        return 1

    def find_with_fewer_neighbors(self, cutoff):
        total = 0
        for row in self.matrix:
            for cell in row:
                if cell < cutoff:
                    total += 1

        return total

    def debug(self):
        # Print X's for rolls you can get, and dots for filler.
        for row in self.matrix:
            dr = []
            for cell in row:
                if cell < 4:
                    dr.append('X')
                else:
                    dr.append('.')
            print(dr)

if __name__ == "__main__":
    m = Matrix()
    m.sum_adjacents()
    #m.debug()
    print(m.find_with_fewer_neighbors(4))
