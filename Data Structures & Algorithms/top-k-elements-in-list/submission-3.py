class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result
