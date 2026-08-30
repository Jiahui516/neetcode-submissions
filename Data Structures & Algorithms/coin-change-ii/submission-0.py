class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 1

            if remaining < 0 or i == len(coins):
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            ans = (dfs(
                i, remaining - coins[i]) + 
                dfs(i + 1, remaining
                ))
            memo[(i,remaining)]=ans
            return ans

        return dfs(0,amount)
