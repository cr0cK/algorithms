#!/usr/bin/env python
## -*- coding: utf-8 -*-


# http://en.wikipedia.org/wiki/Tree_traversal


graph1 = [
    {'key': 'F', 'children': ('B', 'G')},
    {'key': 'B', 'children': ('A', 'D')},
    {'key': 'D', 'children': ('C', 'E')},
    {'key': 'G', 'children': (None, 'I')},
    {'key': 'I', 'children': ('H', None)},
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


def bfs(node, type_):
    if node is not None:
        if type_ == 'preorder' and node.value is not None:
            yield node

        for child_node in bfs(node.left, type_):
            yield child_node

        if type_ == 'inorder' and node.value is not None:
            yield node

        for child_node in bfs(node.right, type_):
            yield child_node

        if type_ == 'postorder' and node.value is not None:
            yield node


def print_values(path):
    print([node.value for node in path])


root = build_tree(graph1)

path = list(bfs(root, 'preorder'))
print_values(path)

path = list(bfs(root, 'inorder'))
print_values(path)

path = list(bfs(root, 'postorder'))
print_values(path)
