class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur_sum,cur_nums):
            if cur_sum==target:
                res.append(cur_nums.copy())
                return

            if i==len(nums) or cur_sum>target:
                return

            cur_sum+=nums[i]
            cur_nums.append(nums[i])
            dfs(i,cur_sum,cur_nums)

            cur_nums.pop()
            cur_sum-=nums[i]
            dfs(i+1,cur_sum,cur_nums)
        
        dfs(0,0,[])
        return res