class Solution {
    public int countSubstrings(String s) {
        int res=0;
        for(int i=0; i<s.length(); i++){
            res+=countpali(s,i,i);
            res+=countpali(s,i,i+1);
        }
        return res;
    }

    private int countpali(String s, int l, int r){
        int res=0;
        while(l>=0&&r<s.length()&&
              s.charAt(l)==s.charAt(r)){
            res++;
            l--;
            r++;
            }
        return res;
    }
}
