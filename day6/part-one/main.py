from collections import defaultdict
def readdata():
    data = []
    with open("../input.txt") as f:
        for line in f:
            data.append(line)
    return data

def count_orbits(orbits):
    graph = defaultdict(lambda : None)

    orbit_count = 0
    for orbit in orbits:
        objects = orbit.split(")")
        graph[objects[1].strip()] = objects[0]

    for orbit in orbits:
        objects = orbit.split(")")
        curr = objects[0]

        while curr:
            curr = graph[curr]
            orbit_count += 1
            

    return orbit_count

if __name__ == '__main__':
    orbits = readdata()
    print(count_orbits(orbits))