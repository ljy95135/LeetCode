// review: dummy head make logic easier

//  Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

// class Solution
class addTwoNumbersSolution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(-1);
        ListNode curr = dummyHead;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int v1 = (l1 != null) ? l1.val : 0;
            int v2 = (l2 != null) ? l2.val : 0;
            int sum = v1 + v2 + carry;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        if (carry == 1) curr.next = new ListNode(1);
        return dummyHead.next;
    }
}