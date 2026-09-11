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
        #For each meeting, store their end time in a minheap, for new meeting, check the start time against the first time in minheap, which is the first released room
        #if starttime>minheap[0], then the room could be reused, pop out the time from minheap and push back the new end time
        #at the meantime keeptrack of the maxroom we used
        maxroom=0
        minheap=[]
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            start=interval.start
            end=interval.end
            if minheap and minheap[0]<=start:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap,end)
            maxroom=max(maxroom, len(minheap))
        return maxroom