class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo={}

        def dfs(i,j):
                        
            if j==len(p):
                return i==len(s)

            match= (
                i<len(s) and
                (s[i]==p[j] or p[j]==".")
            )

            if (i,j) in memo:
                return memo[(i,j)]

            if j+1<len(p) and p[j+1]=="*":
                ans= (
                    dfs(i,j+2) 
                    or
                    (match and dfs(i+1,j))
                )
                memo[(i,j)]=ans
                return ans
            
            if match:
                ans= dfs(i+1,j+1)
                memo[(i,j)]=ans
                return ans
            
            return False
        return dfs(0,0)