# review: use divmod can make the code shorter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # O(n) n is max(l1's length, l2's length)
        v, add1 = Solution._add2numbers(l1.val, l2.val)
        result = ListNode(v)
        k = result
        while l1.next is not None or l2.next is not None:
            if l1.next is not None and l2.next is not None:
                l1 = l1.next
                l2 = l2.next
                v, add1 = Solution._add2numbers(l1.val, l2.val, add1)
                k.next = ListNode(v)
            elif l1.next is not None:
                l1 = l1.next
                v, add1 = Solution._add1number(l1.val, add1)
                k.next = ListNode(v)
            else:  # l2.next is not None
                l2 = l2.next
                v, add1 = Solution._add1number(l2.val, add1)
                k.next = ListNode(v)
            k = k.next
        if add1:
            k.next = ListNode(1)
        return result

    @staticmethod
    def _add2numbers(v1, v2, add1=False):
        x = v1 + v2 + 1 if add1 else v1 + v2
        if x >= 10:
            return x - 10, True
        return x, False

    @staticmethod
    def _add1number(v, add1=False):
        x = v + 1 if add1 else v
        if x >= 10:
            return x - 10, True
        return x, False
