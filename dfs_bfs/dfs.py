#!/usr/bin/env python
## -*- coding: utf-8 -*-

# http://thatmattbone.com/binary-tree-traversal-in-python-with-generators.html


graph1 = [
    {'key': '1', 'children': ('2', '3')},
    {'key': '2', 'children': ('4', '5')},
    {'key': '3', 'children': ('6', '7')},
]

graph2 = [
    {'key': '50', 'children': ('40', '60')},
    {'key': '40', 'children': ('35', '45')},
    {'key': '60', 'children': ('55', '65')},
]


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(graph):
    root_node = None
    saved_nodes = {}

    def get_node(value):
        if value not in saved_nodes:
            saved_nodes[value] = Node(value)
        return saved_nodes[value]

    for node_definition in graph:
        node = get_node(node_definition['key'])

        node.left = get_node(node_definition['children'][0])
        node.right = get_node(node_definition['children'][1])

        if not root_node:
            root_node = node

    return root_node


def recursive_dfs(node):
    nodes = []

    if node is not None:
        nodes.append(node)
        nodes.extend(recursive_dfs(node.left))
        nodes.extend(recursive_dfs(node.right))

    return nodes


def basic_bfs(node):
    if node is not None:
        yield node
        for children in basic_bfs(node.left):
            yield children
        for children in basic_bfs(node.right):
            yield children


def left_then_right(node):
    if node is not None:
        yield node.left
        yield node.right


def right_then_left(node):
    if node is not None:
        yield node.right
        yield node.left


def binary_search_chooser(value):
    def binary_search_chooser_inner(node):
        if int(value) == int(node.value):
            return

        if node is not None and node.value is not None:
            if int(value) <= int(node.value):
                yield node.left
            else:
                yield node.right

    return binary_search_chooser_inner


def bfs(node, chooser=left_then_right):
    if node is not None:
        yield node

        for children in chooser(node):
            for child_node in bfs(children, chooser=chooser):
                yield child_node


def print_values(path):
    print([node.value for node in path])


root = build_tree(graph1)

path = recursive_dfs(root)
print_values(path)

path = list(basic_bfs(root))
print_values(path)

path = list(bfs(root, chooser=left_then_right))
print_values(path)

path = list(bfs(root, chooser=right_then_left))
print_values(path)

root = build_tree(graph2)

path = list(bfs(root, chooser=binary_search_chooser(55)))
print_values(path)
