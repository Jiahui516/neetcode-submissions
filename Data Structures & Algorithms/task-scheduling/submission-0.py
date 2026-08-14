import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        heap = []
        for cnt in count.values():
            heap.append(-cnt)
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and time == q[0][1]:
                cnt, cooldown_time = q.popleft()
                heapq.heappush(heap, cnt)

        return time
