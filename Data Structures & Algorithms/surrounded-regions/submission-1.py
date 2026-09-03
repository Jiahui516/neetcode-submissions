from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        queue=deque()
        for r in range(rows):
            if board[r][0]=="O":
                queue.append((r,0))
                board[r][0]="U"
            if board[r][cols-1]=="O":
                queue.append((r,cols-1))
                board[r][cols-1]="U"
        
        for c in range(cols):
            if board[0][c]=="O":
                queue.append((0,c))
                board[0][c]="U"
            if board[rows-1][c]=="O":
                queue.append((rows-1,c))
                board[rows-1][c]="U"
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if(
                    nr<0 or nr>=rows or
                    nc<0 or nc>=cols or
                    board[nr][nc] != "O"
                ):
                    continue
                board[nr][nc]="U"
                queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="U":
                    board[r][c]="O"