class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(left,right):
            prev1=0
            prev2=0

            for i in range(left,right+1):
                current=max(prev1,prev2+nums[i])
                prev2=prev1
                prev1=current
            
            return prev1
        
        return max(
            rob_linear(0,len(nums)-2),
            rob_linear(1,len(nums)-1)
        )