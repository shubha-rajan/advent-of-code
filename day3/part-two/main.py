def crossed_wires():
    wires = []
    def total_steps(point, path1, path2):
        return path1[point] + path2[point]
    
    def trace(wire):
        points = {}
        pos = (0, 0)
        steps = 0
        for vector in wire:         
            direction = vector[0]
            dist = int(vector[1:])
            for _ in range(dist):
                steps += 1
                x,y = pos
                if direction == 'U':
                    pos = (x, y + 1)
                elif direction == 'D':
                    pos = (x, y - 1)
                elif direction == 'L':
                    pos = (x - 1, y)
                elif direction == 'R':
                    pos = (x + 1, y)
                points[pos] = steps
        return points

    with open("../input.txt") as f:
        for line in f:
            wires.append(line.split(","))
    
        wire_1_path = trace(wires[0])
        wire_2_path = trace(wires[1])
        intersection = wire_1_path.keys() & wire_2_path.keys()
        return min([total_steps(x, wire_2_path,wire_1_path) for x in intersection])

if __name__ == "__main__":
    print(crossed_wires())
    