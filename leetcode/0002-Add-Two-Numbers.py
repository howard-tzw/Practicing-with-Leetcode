# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        resultTail = result
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            resultTail.next = ListNode(out)
            resultTail = resultTail.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next


class MySolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = 0
        res = ListNode(0)
        head = res
        while l1 or l2 or q:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + q
            q = sum // 10
            remainder = sum % 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            node = ListNode(remainder)
            res.next = node
            res = res.next

        return head.next


print(divmod(3, 10))
