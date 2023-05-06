"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。



示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
方法一:使用栈逆置链表
"""

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         stack = []
#         while head:
#             stack.append(head)
#             head = head.next
#
#         dummy = ListNode(-1)
#         cur = dummy
#         while stack:
#             node = stack.pop()
#             cur.next = node
#             cur = cur.next
#
#         cur.next = None
#         return dummy.next


"""
方法二:迭代
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
