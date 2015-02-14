#!/usr/bin/env python
## -*- coding: utf-8 -*-

graph1 = {
    '1': set(['2', '3', '4']),
    '2': set(['5', '6']),
    '5': set(['9', '10']),
    '4': set(['7', '8']),
    '7': set(['11', '12'])
}

# http://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/300px-Breadth-first-tree.svg.png

graph2 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# https://lh6.googleusercontent.com/-OcCSNQHlktZQMhDuzK4mHbyT6Z9jsS1wJpSNRM2Rw6LpvNxfJ9SxvxP4yWN1BvIiplB1A=w1896-h823


def dfs(graph, start):
    """
    Browse the graph using a DFS (depth) tranversal algorithm.
    A DFS is using a stack.
    """
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            if vertex not in graph:
                graph[vertex] = set()

            stack.extend(graph[vertex] - visited)
    return visited


def bfs(graph, start):
    """
    Browse the graph using a BFS (depth) tranversal algorithm.
    A DFS is using a queue.
    Just pop the first instead of the last (1)
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0) # (1)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def dfs_recursive(graph, start, visited=None):
    """
    Recursive implementation of DFS.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited


def get_dfs_path(graph, start, end):
    """
    Return the shortest bath between start and end using a BFS tranversal
    algorithm.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()

        # declare the node in the graph is it doesn't exist
        # (if it has no child)
        if vertex not in graph:
            graph[vertex] = set()

        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Python 3 with yield from
# def get_dfs_path2(graph, start, goal, path=None):
#     if path is None:
#         path = [start]
#     if start == goal:
#         yield path
#     for next in graph[start] - set(path):
#         yield from get_dfs_path2(graph, next, goal, path + [next])


def get_bfs_path(graph, start, end):
    """
    Return the shortest bath between start and end using a BFS tranversal
    algorithm.
    """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)

        # declare the node in the graph is it doesn't exist
        # (if it has no child)
        if vertex not in graph:
            graph[vertex] = set()

        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def get_shortest_path(graph, start, end):
    """
    Return the first result of the paths returned by a BFS tranversal
    algorithm.
    """
    return next(get_bfs_path(graph, start, end))


print('DFS:')
print(dfs(graph1, '1'))
print(dfs_recursive(graph1, '1'))

print('---')

print(dfs(graph2, 'A'))
print(dfs_recursive(graph2, 'A'))

print('---')

print('Get paths with DFS:')
print(list(get_dfs_path(graph1, '1', '11'))) # [['1', '4', '7', '11']]
print(list(get_dfs_path(graph2, 'A', 'F'))) # [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]

print('---------')

print('BFS:')
print(bfs(graph1, '1'))

print('---')

print(bfs(graph2, 'A'))

print('---')

print('Get paths with BFS:')
print(list(get_bfs_path(graph1, '1', '11'))) # [['1', '4', '7', '11']]
print(list(get_bfs_path(graph2, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

print('Shortest path, take only the first of the list of BFS:')
print(get_shortest_path(graph2, 'A', 'F')) # ['A', 'C', 'F']
