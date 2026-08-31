class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        
        target=sum(nums)//2

        memo={}
        def dfs(i,remaining):
            if remaining==0:
                return True
            
            if i==len(nums) or remaining<0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            ans=(
                dfs(i+1,remaining-nums[i]) 
                or
                dfs(i+1,remaining)
            )
            memo[(i,remaining)]=ans
            return ans
        
        return dfs(0,target)