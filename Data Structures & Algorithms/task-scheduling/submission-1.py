from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            count[task]=count.get(task,0)+1

        heap=[]
        for cnt in count.values():
            heap.append(-cnt)
        heapq.heapify(heap)

        cooldown=deque()
        time=0

        while cooldown or heap:
            time+=1

            if heap:
                count=heapq.heappop(heap)
                count+=1
                if count !=0:
                    cooldown.append((count,time +n))
            if cooldown and time==cooldown[0][1]:
                count, _ = cooldown.popleft()
                heapq.heappush(heap,count)
        return time

        

