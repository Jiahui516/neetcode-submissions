class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        
        target=sum(nums)//2
        def dfs(i,remaining):
            if remaining==0:
                return True
            
            if i==len(nums) or remaining<0:
                return False

            return(
                dfs(i+1,remaining-nums[i]) 
                or
                dfs(i+1,remaining)
            )
        
        return dfs(0,target)