class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        leftMax=0
        rightMax=0

        water=0
        while left<=right:
            leftMax=max(height[left],leftMax)
            rightMax=max(height[right],rightMax)

            if leftMax>rightMax:
                water+=rightMax-height[right]
                right-=1
            else:
                water+=leftMax-height[left]
                left+=1
        return water