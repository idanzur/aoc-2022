#!/usr/bin/python3
from collections import defaultdict
from dataclasses import dataclass

file = './sample.txt' if 0 else './input.txt'


@dataclass
class Graph:
    adjacency: dict

    def get_neighbors(self, v):
        return self.adjacency[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        return 1

    def a_star_algorithm(self, start_node, stop_node):
        open_list = {start_node}
        closed_list = set([])

        g = {start_node: 0}

        parents = {start_node: start_node}

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)
        return None


cell_val_mapping = {'S': ord('a'), 'E': ord('z')}


def parse_data():
    with open(file) as f:
        data = f.read().splitlines()
    adjacency = defaultdict(list)
    width = len(data[0])
    height = len(data)
    start = end = None
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            cell_val = cell_val_mapping.get(cell, ord(cell))
            if cell == 'S':
                start = (cell, i, j)
            elif cell == 'E':
                end = (cell, i, j)
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= y < height and 0 <= x < width and not (y == i and x == j):
                    target = data[y][x]
                    target_val = cell_val_mapping.get(target, ord(target))
                    if (cell_val - target_val) >= -1:
                        adjacency[(cell, i, j)].append(((target, y, x), 1))
    graph = Graph(adjacency)
    return data, graph, start, end


def part1():
    data, graph, start, end = parse_data()
    path = graph.a_star_algorithm(start, end)
    ans = len(path) - 1
    print(f'part 1: {ans}')


def find_visited_path(paths, start):
    for path in paths.values():
        if start in path:
            return path[path.index(start) + 1:]


def part2():
    data, graph, _, end = parse_data()
    paths = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell not in ['a', 'S']:
                continue
            start = (cell, i, j)
            if visited_path := find_visited_path(paths, start):
                paths[start] = visited_path
            elif new_path := graph.a_star_algorithm(start, end):
                paths[start] = new_path[1:]
    ans = min(map(len, paths.values()))
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()
