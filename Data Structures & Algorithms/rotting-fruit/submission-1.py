from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    q.append((row,col))

        minutes=0

        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        q.append((nr,nc))
                        fresh-=1
                        grid[nr][nc]=2
            minutes+=1
        if fresh==0: 
            return minutes
        else:
            return -1
                    