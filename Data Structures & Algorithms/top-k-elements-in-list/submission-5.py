import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        wordcount={}

        for num in nums:
            wordcount[num]=wordcount.get(num,0)+1
        
        heap=[]

        for num, cnt in wordcount.items():
            heapq.heappush(heap,(-cnt,num))
        
        res=[]
        while k and heap:
            cnt, num = heapq.heappop(heap)
            res.append(num)
            k-=1
        return res