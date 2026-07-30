class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        lst = [[] for i in range(n)]

        for e1, e2 in edges:
            lst[e1].append(e2)
            lst[e2].append(e1)

        visited = set()
        print(lst)

        def dfs(curNode, prev):
            print(curNode)
            if curNode == prev:
                return True
            
            if curNode in visited:
                return False

            visited.add(curNode)
            for n in lst[curNode]:
                if n == prev:
                    continue

                if not dfs(n, curNode):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n