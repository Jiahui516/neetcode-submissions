class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def dfs(i,current_sum):
            if i==len(nums):
                return 1 if current_sum==target else 0
            
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]

            ans=(
                dfs(i+1,current_sum+nums[i])+
                dfs(i+1,current_sum-nums[i])
            )   
            memo[(i,current_sum)]=ans
            return ans
        return dfs(0,0)

            
            