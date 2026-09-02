class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting=set()
        completed=set()
        order=[]
        def dfs(course):
            if course in visiting:
                return False

            if course in completed:
                return True

            visiting.add(course)
            pre=preMap[course]
            for p in pre:
                if not dfs(p):
                    return False
            visiting.remove(course)
            completed.add(course)
            order.append(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order
            