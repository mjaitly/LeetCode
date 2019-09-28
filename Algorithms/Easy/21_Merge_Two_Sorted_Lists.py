'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Solution 1: Recursive
# Runtime: 36 ms, faster than 96.94% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.6 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1 

        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        
        return head

if __name__ == "__main__":
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3
    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3
   
    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)
    node = result
    while node != None:
        print(node.val)
        node = node.next


'''
# Solution 2: Iterative
# Definition for singly-linked list.
# Runtime: 44 ms, faster than 63.91% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1 

        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next   
        
        tail.next = l1 or l2
        return head.next  


if __name__ == "__main__":
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3
    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3
   
    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)
    node = result
    while node != None:
        print(node.val)
        node = node.next
'''
