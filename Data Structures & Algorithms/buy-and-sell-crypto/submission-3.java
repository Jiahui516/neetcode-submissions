class Solution {
    public int maxProfit(int[] prices) {
        int left=0, right=1;
        int profit=0;
        while(right<prices.length){
            int diff=prices[right]-prices[left];
            profit=Math.max(diff,profit);
            if(prices[right]<prices[left]){
                left=right;
                right++;
            }else{
                right++;
            }
        }
        return profit;
    }
}
