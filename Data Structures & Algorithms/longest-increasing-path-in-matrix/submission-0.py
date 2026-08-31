class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo={}
        rows=len(matrix)
        cols=len(matrix[0])

        directions=[
            (1,0),
            (0,1),
            (-1,0),
            (0,-1),
        ]

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]

            ans=1

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
            
                if (
                    0<=nr<rows and
                    0<=nc<cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    ans=max(ans,1+dfs(nr,nc))
  
            memo[(r,c)]=ans

            return ans
        
        res=0
        for r in range(rows):
            for c in range(cols):
                cur=dfs(r,c)
                res=max(cur,res)
        return res

