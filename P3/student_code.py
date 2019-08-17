import math
from heapq import heappush, heappop
from copy import deepcopy


def get_distance(M, p1, p2):
    return math.sqrt((M.intersections[p1][0] - M.intersections[p2][0]) ** 2 + (M.intersections[p1][0] - M.intersections[p2][1]) ** 2)


def shortest_path(M, start, goal):
    if start == goal:
        return [start]

    h = dict()
    for i in range(len(M.intersections)):
        if i == goal:
            h[i] = 0.0
        else:
            h[i] = get_distance(M, goal, i)

    candidates = []
    heappush(candidates, (math.inf, [start]))
    visited = set()
    visited.add(start)
    path = []
    history = []
    prev_len = 0
    tmp_visited = set()

    while len(candidates) != 0:
        cur_node = heappop(candidates)

        for item in M.roads[cur_node[1][-1]]:
            if item not in visited and goal not in cur_node[1]:
                distance = get_distance(M, cur_node[1][-1], item)
                score = distance + h[item]

                nodes = deepcopy(cur_node)[1]
                nodes.append(item)
                heappush(candidates, (score, nodes))
                history.append((score, nodes))

                if item == goal:
                    heappush(path, (score, nodes))

                tmp_visited.add(item)
        if prev_len != 0 and len(cur_node[1]) != prev_len:
            visited |= tmp_visited
            tmp_visited = set()
        prev_len = len(cur_node[1])

    return heappop(path)[1]


if __name__ == "__main__":
    from Map import Map
    map_10 = Map("map10")
    map_40 = Map("map40")

    print(shortest_path(map_40, 8, 24))
