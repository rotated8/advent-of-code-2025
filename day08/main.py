from math import sqrt, prod
import heapq


class Box:
    def __init__(self, coords):
        x, y, z = coords.split(',', 3)
        self.x, self.y, self.z = int(x), int(y), int(z)

    def distance_to(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


def add_connection(connections, circuits):
    # Get the connection, discard the distance, keep the box indices
    box_indices = heapq.heappop(connections)[-1]
    new_indices = box_indices.copy()

    # If the new connection overlaps circuits, add their indices to the new one, and note which circuits to clean up
    cleanup = []
    for idx, circuit in enumerate(circuits):
        if len(box_indices & circuit) > 0:
            box_indices |= circuit
            cleanup.append(idx)

    # Add the new (any maybe updated) indices to the list of circuits
    circuits.append(box_indices)

    # Remove, in descending index order, the old overlapping circuits
    for idx in sorted(cleanup, reverse=True):
        circuits.pop(idx)

    # Return the indices from the last connection added (as opposed to all the indices in that circuit)
    return new_indices


def main():
    # All the boxes in the order they were created
    boxes = []
    # A heap of distances, and the indices of the boxes at that distance. The heap keeps the distances sorted
    connections = []

    with open('input.txt') as txt:
        for line in txt:
            new_box = Box(line)
            new_box_idx = len(boxes)

            for box_idx, box in enumerate(boxes):
                distance = new_box.distance_to(box)
                heapq.heappush(connections, (distance, {new_box_idx, box_idx}))

            boxes.append(new_box)

    # Each box starts on its own circuit. A circuit is the set of indices of boxes on that circuit
    circuits = [{i} for i in range(len(boxes))]
    for _ in range(1000):
        add_connection(connections, circuits)

    circuit_lengths = [len(circ) for circ in circuits]
    circuit_lengths.sort(reverse=True)
    print(prod(circuit_lengths[:3]))

    last_connection_indices = {}
    while len(circuits) > 1:
        last_connection_indices = add_connection(connections, circuits)

    print(prod([boxes[idx].x for idx in last_connection_indices]))


if __name__ == '__main__':
    main()
