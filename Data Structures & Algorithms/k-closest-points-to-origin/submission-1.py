import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for point in points:
            x=point[0]
            y=point[1]

            dist=x**2+y**2
            heapq.heappush(heap,(dist,x,y))

        res=[]

        for _ in range(k):
            (dist,x,y)=heapq.heappop(heap)
            res.append([x,y])
        return res


