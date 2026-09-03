class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin=nums[0]
        curMax=nums[0]
        globalMax=nums[0]
        
        for num in nums[1:]:
            oldMax=curMax
            oldMin=curMin

            newMax=max(
                num,
                oldMax*num,
                oldMin*num
            )
            newMin=min(
                num,
                oldMax*num,
                oldMin*num
            )
            curMax=newMax
            curMin=newMin
            globalMax=max(globalMax,newMax)
            
        return globalMax