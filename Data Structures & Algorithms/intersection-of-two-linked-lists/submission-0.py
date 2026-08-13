# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA=headA
        pB=headB

        while headA!=headB:
            pA=pA.next if pA else headB
            pB=pB.next if pB else headA

            if pA==pB:
                return pA
        return None
