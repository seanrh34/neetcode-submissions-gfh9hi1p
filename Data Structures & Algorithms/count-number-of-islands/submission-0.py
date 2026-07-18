class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isOut(r, c):
            if r < 0 or c < 0:
                return True

            if r >= len(grid):
                return True

            if c >= len(grid[0]):
                return True

        def dfs(r, c):
            if isOut(r, c):
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            if not isOut(r + 1, c):
                dfs(r + 1, c)
            if not isOut(r, c + 1):
                dfs(r, c + 1)
            if not isOut(r - 1, c):
                dfs(r - 1, c)
            if not isOut(r, c - 1):
                dfs(r, c - 1)

        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIslands += 1
                    dfs(i, j)

        return numIslands