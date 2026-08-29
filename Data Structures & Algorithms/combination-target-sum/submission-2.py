class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,remaining, current):
            if remaining==0:
                res.append(current.copy())
                return
            
            if remaining<0 or i==len(nums):
                return 
            
            current.append(nums[i])
            remaining-=nums[i]
            dfs(i,remaining,current)

            current.remove(nums[i])
            remaining+=nums[i]
            dfs(i+1,remaining,current)
        
        dfs(0,target,[])
        return res