from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2


            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1
