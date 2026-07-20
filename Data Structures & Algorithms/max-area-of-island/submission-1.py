class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            curOutput = 0
            q = deque()
            q.append((row, col))
            grid[row][col] = 0

            while q:
                r, c = q.popleft()
                curOutput += 1

                if not isOut(r+1,c) and grid[r+1][c] == 1:
                    q.append((r+1,c))
                    grid[r+1][c] = 0
                if not isOut(r,c+1) and grid[r][c+1] == 1:
                    q.append((r,c+1))
                    grid[r][c+1] = 0
                if not isOut(r-1,c) and grid[r-1][c] == 1:
                    q.append((r-1,c))
                    grid[r-1][c] = 0
                if not isOut(r,c-1) and grid[r][c-1] == 1:
                    q.append((r,c-1))
                    grid[r][c-1] = 0

            return curOutput

        def isOut(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return True
            else:
                return False

        output = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    output = max(output, bfs(i, j))

        return output