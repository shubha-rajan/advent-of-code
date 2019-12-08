def crossed_wires():
    wires = []
    def manhattan(point):
        x,y = point
        return abs(x) + abs(y)
    
    def trace(wire):
        points = set()
        pos = (0, 0)
        for vector in wire:         
            direction = vector[0]
            dist = int(vector[1:])
            for _ in range(dist):
                x,y = pos
                if direction == 'U':
                    pos = (x, y + 1)
                elif direction == 'D':
                    pos = (x, y - 1)
                elif direction == 'L':
                    pos = (x - 1, y)
                elif direction == 'R':
                    pos = (x + 1, y)
                points.add(pos)
        return points

    with open("../input.txt") as f:
        for line in f:
            wires.append(line.split(","))
    
        wire_1_path = trace(wires[0])
        wire_2_path = trace(wires[1])
        intersection = wire_1_path & wire_2_path
        return min([manhattan(x) for x in intersection])

if __name__ == "__main__":
    print(crossed_wires())
    

    