class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen=0 #minimum open parenthesis required
        maxOpen=0 #maximum open parenthesis required
        
        for character in s:
            if character=="(":
                minOpen+=1
                maxOpen+=1
            if character==")":
                minOpen-=1
                maxOpen-=1
            if character=="*":
                minOpen-=1
                maxOpen+=1
            
            minOpen=max(0,minOpen)
            if maxOpen<0:
                return False
            
        return minOpen<=0