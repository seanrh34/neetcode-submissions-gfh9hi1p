"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(cur_node):
            if cur_node in clones:
                return clones[cur_node]

            clone = Node(cur_node.val)
            clones[cur_node] = clone

            for neighbor in cur_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
