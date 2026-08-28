class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[course].append(pre)

        visiting=set()

        def dfs(course):
            if course in visiting:
                return False
            if graph[course]==[]:
                return True
            visiting.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visiting.remove(course)
            graph[course]=[]
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
