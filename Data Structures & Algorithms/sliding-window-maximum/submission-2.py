from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        res=[]

        for right in range(len(nums)):
            while d and nums[d[-1]]<nums[right]:
                d.pop()
            
            d.append(right)

            if(d[0]<right-k+1):
                d.popleft()

            if right>=k-1:
                res.append(nums[d[0]])
        return res