import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while(len(stones)>=2):
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if first==second:
                continue
            else:
                heapq.heappush(stones,-abs(first-second))
        if stones:
            return -heapq.heappop(stones)
        else:
            return 0
