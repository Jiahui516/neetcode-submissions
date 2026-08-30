class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(k):
            hours=0
            for pile in piles:
                hours+=(pile+k-1)//k
            return hours<= h

        left=1
        right=max(piles)

        while left<=right:
            mid=left+(right-left)//2
            if canFinish(mid):
                right=mid-1
            else:
                left=mid+1
        return left