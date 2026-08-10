class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen= new HashSet<>();
        int res=0, l=0;

        for(int r=0; r<s.length();r++){
            while(seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l));
                l++;
            }
            seen.add(s.charAt(r));
            res=Math.max(res,r-l+1);
        }
        return res;
    }
}
