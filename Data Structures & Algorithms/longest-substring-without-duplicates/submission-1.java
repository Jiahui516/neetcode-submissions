class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left =0;
        int res = 0;

        for(int right=0; right<s.length(); right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(s.charAt(right));
            res = Math.max(seen.size(), res);
        }
        return res;
    }
}
