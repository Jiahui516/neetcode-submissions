import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        heap=[]

        for (num,freq) in freq.items():
            heapq.heappush(heap,(freq,num))

            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        while heap:
            freq,num=heapq.heappop(heap)
            res.append(num)
        return res