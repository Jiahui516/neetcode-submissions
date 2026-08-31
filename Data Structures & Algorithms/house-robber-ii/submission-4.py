class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            if len(houses)==1:
                return houses[0]

            dp=[0]*len(houses)
            dp[0]=houses[0]
            dp[1]=max(houses[0],houses[1])

            for i in range(2,len(houses)):
                dp[i]=max(dp[i-1],(houses[i]+dp[i-2]))
            
            return dp[-1]
        
        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )