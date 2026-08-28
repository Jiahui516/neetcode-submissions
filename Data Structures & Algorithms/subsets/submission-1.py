class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]

        def dfs(i,current):
            if i==len(nums):
                res.append(current.copy())
                return

            current.append(nums[i])
            dfs(i+1,current)
            current.pop()

            dfs(i+1,current)
            
        dfs(0,subset)
        return res