# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next  # 保存curr的next
                curr.next = prev  # 把当前节点的箭头反过来指向已经反转好的部分
                prev = curr  # prev始终指向已经反转好的那一段的头
                curr = temp  # 现在的项往右一个

            # 此时groupPrev.next还指向原来的关系
            temp = groupPrev.next
            groupPrev.next = kth  # 指向新头（e.g.第一次反转完是3）
            groupPrev = temp  # 把 groupPrev 移到这一组的新尾巴，准备处理下一组

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
