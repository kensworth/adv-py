def num_islands(map):
    visited = set()
    count = 0
    for i in xrange(len(map)):
        for j in xrange(len(map[0])):
            if map[i][j] and (i, j) not in visited:
                explore_island(map, (i, j), visited)
                count += 1
    return count

def explore_island(map, start_node, visited):
    frontier = Queue()
    frontier.add(start_node)
    while frontier:
        node = frontier.pop()
        visited.add(node)
        for next_node in neighbours(node, map):
            if next_node not in visited:
                frontier.add(next_node)


def neighbours(node, map):
    i, j = node
    adjacent_land = []
    if is_land(i + 1, j, map):
        adjacent_land.append((i + 1, j))
    if is_land(i - 1, j, map):
        adjacent_land.append((i - 1, j))
    if is_land(i, j + 1):
        adjacent_land.append((i, j + 1))
    if is_land(i, j - 1):
        adjacent_land.append((i, j - 1))
    return adjacent_land

def is_land(i, j, map):
    return 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == 1
