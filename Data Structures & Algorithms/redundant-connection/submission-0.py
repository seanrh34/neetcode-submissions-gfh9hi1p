class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numNodes = len(edges)

        def helper(graph):
            visited = set()

            def dfs(node, prev):
                if node in visited:
                    return False
                
                visited.add(node)
                for n in graph[node]:
                    if n != prev:
                        if not dfs(n, node):
                            return False
                return True

            return dfs(1, -1) and len(visited) == numNodes

        for i in range(numNodes - 1, -1, -1):
            graph = [[] for x in range(numNodes + 1)]
            for j in range(len(edges)):
                if j != i:
                    e1, e2 = edges[j][0], edges[j][1]
                    graph[e1].append(e2)
                    graph[e2].append(e1)

            if helper(graph):
                return edges[i]
                
        return []