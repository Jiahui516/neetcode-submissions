class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums) 
        max_length=0

        for num in numSet:
            if (num-1) not in numSet:
                length=1
                while(num+length) in numSet:
                    length+=1
                max_length=max(length,max_length)
        
        return max_length
