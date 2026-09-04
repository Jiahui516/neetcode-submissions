class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half=(total+1)//2

        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1

        left=0
        right=len(nums1)
        while True:
            i=(left+right)//2
            j=half-i

            Aleft=nums1[i-1] if i>0 else float("-inf")
            Aright=nums1[i] if i<len(nums1) else float("inf")
            Bleft=nums2[j-1] if j>0 else float("-inf")
            Bright=nums2[j] if j<len(nums2) else float("inf")

            if Aleft <= Bright and Bleft<=Aright:
                if total%2==1:
                    return float(max(Aleft,Bleft))
                else:
                    return((max(Aleft,Bleft)+min(Aright,Bright))/2)

            elif Aleft>Bright:
                right=i-1
            else:
                left=i+1
