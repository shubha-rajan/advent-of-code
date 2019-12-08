from collections import defaultdict
def readdata():
    data = []
    with open("../input.txt") as f:
        for line in f:
            data.append(line)
    return data

def search_for_santa(orbits):
    graph = defaultdict(lambda : set())

    for orbit in orbits:
        objects = orbit.split(")")
        graph[objects[1].strip()].add(objects[0])
        graph[objects[0]].add(objects[1].strip())
    visited = set()
    def search(node):
        if "SAN" in graph[node]: 
            return 1
        elif not ([neighbor for neighbor in graph[node] 
                    if neighbor not in visited]):
            return 0
        
        else:
            visited.add(node)
            count = max([search(neighbor) 
                                for neighbor in graph[node]
                                if neighbor not in visited])
            visited.remove(node)
            if count >= 1: return 1 + count
            return 0

    return search(graph["YOU"].pop()) - 1

if __name__ == '__main__':
    orbits = readdata()
    print(search_for_santa(orbits))