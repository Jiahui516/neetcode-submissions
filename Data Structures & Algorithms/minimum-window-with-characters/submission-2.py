class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for c in t:
            need[c]=need.get(c,0)+1
        
        window={}
        need_count=len(need)
        have=0
        left=0

        res=[-1,-1]
        res_len=float("inf")

        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have+=1
            
            while have == need_count:
                if right-left+1<res_len:
                    res=[left,right]
                    res_len=right-left+1

                left_char=s[left]
                window[left_char]-=1

                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                left+=1

        l,r=res
        if res_len==float("inf"):
            return ""
        return s[l:r+1]

