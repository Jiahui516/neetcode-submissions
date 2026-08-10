class Solution {
    public int characterReplacement(String s, int k) {
        int res=0;
        Set<Character> charset = new HashSet<>();
        for(char c:s.toCharArray()){
            charset.add(c);
        }

        for(char c:charset){
            int count=0, left=0;
            for(int right=0; right<s.length(); right++){
                if(s.charAt(right)==c){
                    count++;
                }
                while(((right-left)+1-count)>k){
                    if(s.charAt(left)==c) count--;
                    left++;
                }
                res=Math.max(res,right-left+1);

            }
            

        }
        return res;
    }
}
