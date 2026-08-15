class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def robLine(arr):
            if len(arr)==1:
                return arr[0]

            dp=[0]*len(arr)

            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])

            for i in range(2,len(arr)):
                dp[i]=max(
                    arr[i]+dp[i-2],
                    dp[i-1]
                )
            
            return dp[-1]
        
        return max(
            robLine(nums[1:]),
            robLine(nums[:-1])
        )

            
