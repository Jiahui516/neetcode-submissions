"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)

        heap=[]
        max_len=0

        for interval in intervals :            
            while heap and interval.start>=heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,interval.end)
            max_len=max(max_len,len(heap))
        return max_len