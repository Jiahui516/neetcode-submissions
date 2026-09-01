class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1=0
        prev2=0
        cur=0
        for i in range(len(cost)):
            cur=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=cur
        
        return min(prev1,prev2)