class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}
        for u,v,w in times:
            if u not in graph:
                graph[u]=[]
            graph[u].append((v,w))

        heap=[(0,k)]
        visited=set()
        max_time=0
        while heap:
            dist,node=heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            max_time=dist
            
            for nei, weight in graph.get(node,[]):
                heapq.heappush(heap,(weight+dist,nei))
        
        if len(visited)<n:
            return -1
        return max_time

