from math import sqrt, prod
import heapq

class Box:
    def __init__(self, coords):
        x, y, z = coords.split(',', 3)
        self.x, self.y, self.z = int(x), int(y), int(z)

    def distance_to(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

def main():
    boxes = []
    heap = []

    with open('input.txt') as txt:
        for line in txt:
            new_box = Box(line)
            new_idx = len(boxes)

            for idx, box in enumerate(boxes):
                d = new_box.distance_to(box)
                heapq.heappush(heap, (d, {new_idx, idx}))

            boxes.append(new_box)

    circuits = []
    for _ in range(1000):
        # Get the connection, discard the distance.
        conn = heapq.heappop(heap)[-1]

        cleanup = []
        for idx, circuit in enumerate(circuits):
            if len(conn & circuit) > 0:
                conn |= circuit
                cleanup.append(idx)

        circuits.append(conn)

        for idx in sorted(cleanup, reverse=True):
            circuits.pop(idx)

    circuit_lengths = [len(circ) for circ in circuits]
    circuit_lengths.sort(reverse=True)
    print(prod(circuit_lengths[:3]))

if __name__ == "__main__":
    main()
