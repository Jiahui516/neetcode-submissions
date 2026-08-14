class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]

        def dfs(i,total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i>=len(nums) or total >target:
                return
            
            cur.append(nums[i])
            total+=nums[i]

            dfs(i, total)
            cur.pop()
            dfs(i+1,total-nums[i])
        dfs(0,0)
        return res
