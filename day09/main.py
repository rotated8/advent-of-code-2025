import heapq

class Point:
    def __init__(self, coords):
        x, y = coords.split(',', 2)
        self.x, self.y = int(x), int(y)

    def __repr__(self):
        return f"<x:{self.x}, y:{self.y}>"

    def rect_area(self, other):
        width = max(self.x, other.x) - min(self.x, other.x) + 1
        height = max(self.y, other.y) - min(self.y, other.y) + 1
        return width*height

def main():
    points = []
    heap = []

    with open('input.txt') as txt:
        for line in txt:
            new_point = Point(line)
            new_idx = len(points)

            for idx, point in enumerate(points):
                a  = new_point.rect_area(point)
                heapq.heappush_max(heap, (a, {new_idx, idx}))

            points.append(new_point)

        m = heapq.heappop_max(heap)
        p = [points[i] for i in m[-1]]
        print(m[0], p)

if __name__ == "__main__":
    main()
