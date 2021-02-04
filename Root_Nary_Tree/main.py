"""
Given all the nodes of an N-ary tree as an array Node[]
tree where each node has a unique value.

Find and return the root of the N-ary tree.

            1
          / | \
         2  3  4
        / \
       5   6
return node 1

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []



def findRoot(tree):
    seen = set()
    for t in tree:
        for c in t.children:
            seen.add(c)

    for t in tree:
        if t not in seen:
            return t.val

    return None


if __name__ == "__main__":
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node2 = Node(2, [node5, node6])
    node1 = Node(1, [node2, node3, node4])

    a = [node6, node5, node2, node1, node4, node3]

    print(findRoot(a))
