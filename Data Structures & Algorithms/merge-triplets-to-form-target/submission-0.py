class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        1.Filter all triplets, eliminate triplets w/ higher value at any index than target triplet's
        2.Check all "safe" triplets, return if there is at least one triplet with required number in ith postion, if not return False
        3.all triplets checked, three positions satisfied, return True
        '''
        matched=[False,False,False]
        for triplet in triplets:
            if(
                triplet[0]>target[0] or
                triplet[1]>target[1] or
                triplet[2]>target[2]
            ):
                continue
            
            for i in range(3):
                if triplet[i]==target[i]:
                    matched[i]=True
        
        return all(matched)

