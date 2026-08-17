"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewHashMap = {}

        def dfs(node):
            if node in oldToNewHashMap:
                return oldToNewHashMap[node]
            # creating a copy of node
            copy = Node(node.val)
            print(copy.neighbors)
            oldToNewHashMap[node] = copy
            for eachNeighbor in node.neighbors:
                copy.neighbors.append(dfs(eachNeighbor))
            return copy
        if node:
            return dfs(node)
        else:
            return None    
            
        