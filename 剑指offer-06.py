"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        def reverse(node):
            if not node:
                return
            reverse(node.next)
            res.append(node.val)

        reverse(head)
        return res


"""
思考:通过递归实现链表逆置,假设当前递归到了链表的最后一个节点，这时候会触发回溯操作，
回溯到倒数第二个节点，倒数第二个节点的指针指向了最后一个节点，
将最后一个节点加入数组后，回溯到倒数第三个节点，以此类推，最终将整个链表反向输出。
"""
