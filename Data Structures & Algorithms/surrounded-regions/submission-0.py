class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if board[r][c] == 'O':
                board[r][c] = 'S'

                for dr, dc in DIRECTIONS:
                    if (r + dr > 0) and (c + dc > 0) and (r + dr < ROWS - 1) and (c + dc < COLS - 1):
                        dfs(r + dr, c + dc)
            else:
                return

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS-1)

        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS-1, col)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                if board[i][j] == 'S':
                    board[i][j] = 'O'