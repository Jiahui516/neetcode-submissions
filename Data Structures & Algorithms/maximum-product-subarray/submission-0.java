class Solution {
    public int maxProduct(int[] nums) {
        int res=nums[0];
        int curMax=1, curMin =1;

        for(int num:nums){
            int temp = num*curMax;
            curMax = Math.max(Math.max(num*curMax, num*curMin),num);
            curMin = Math.min(Math.min(temp, num*curMin), num);
            res =Math.max(curMax, res);
        }
        return res;
    }
}
