class Solution {
    public int subarraySum(int[] nums, int k) {
        int res=0;
        int count=0;
        Map<Integer, Integer> prefixcount = new HashMap<>();
        prefixcount.put(0,1);
        for(int i=0; i<nums.length; i++){
            count+=nums[i];
            int diff = count-k;
            if(prefixcount.containsKey(diff)){
                res += prefixcount.get(diff);
            }
            prefixcount.put(count, prefixcount.getOrDefault(count,0)+1);
            
        }
        return res;
    }
}