class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        lst = [[] for i in range(n)]

        for e1, e2 in edges:
            lst[e1].append(e2)
            lst[e2].append(e1)
        
        visited = set()

        def dfs(curNode, prev):
            if curNode in visited:
                return
            
            visited.add(curNode)
            for e in lst[curNode]:
                if e != prev:
                    dfs(e, curNode)

        output = 0

        for i in range(n):
            if i not in visited:
                output += 1
                dfs(i, -1)

        return output