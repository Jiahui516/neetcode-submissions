class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i<nums.length; i++){
            if(nums[i] != nums[i-1]){
                i++;
            }
            else{
                return true;
            }
        }
        return false;
    }
}
