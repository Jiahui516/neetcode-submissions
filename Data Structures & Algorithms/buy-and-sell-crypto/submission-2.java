class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int minP = prices[0];

        for(int i=0; i<prices.length; i++){
            int profit= prices[i]-minP;
            maxP =Math.max(maxP, profit);
            minP =Math.min(minP,prices[i]);
        }
        return maxP;
    }
}
