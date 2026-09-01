class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        memo={}

        def dfs(left,right):
            if left+1==right:
                return 0
            
            if (left,right) in memo:
                return memo[(left,right)]

            ans =0

            for i in range(left+1,right):
                coins =(
                    dfs(left,i)+
                    nums[left]*nums[i]*nums[right]+
                    dfs(i,right)
                )

                ans=max(ans,coins)
            memo[(left,right)]=ans
            return ans
        
        return dfs(0,len(nums)-1)
        
