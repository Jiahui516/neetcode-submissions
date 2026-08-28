class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0

        left=0
        right=len(heights)-1

        while left<right:
            area=(right-left)*min(heights[left],heights[right])
            maxarea=max(area,maxarea)

            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        
        return maxarea