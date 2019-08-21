'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1 :
# Runtime: 80 ms, faster than 55.99% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = l1.val + l2.val
        carry = sum // 10
    
        l3 = ListNode(sum % 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while(p1 != None or p2 != None):
            sum = carry + ( p1.val if p1 else 0) + ( p2.val if p2 else 0)
            carry = sum // 10
            p3.next = ListNode(sum % 10)
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
    
        if(carry > 0):
            p3.next = ListNode(carry)
    
        return l3

if __name__ == "__main__":
    # [0,8,6,5,6,8,3,5,7]
    # [6,7,8,0,8,5,8,9,7]
    # OUTPUT [6,5,5,6,4,4,2,5,5,1]
    l1_1 = ListNode(0)
    l1_2 = ListNode(8)
    l1_3 = ListNode(6)
    l1_4 = ListNode(5)
    l1_5 = ListNode(6)
    l1_6 = ListNode(8)
    l1_7 = ListNode(3)
    l1_8 = ListNode(5)
    l1_9 = ListNode(7)
    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5
    l1_5.next = l1_6
    l1_6.next = l1_7
    l1_7.next = l1_8
    l1_8.next = l1_9
    l2_1 = ListNode(6)
    l2_2 = ListNode(7)
    l2_3 = ListNode(8)
    l2_4 = ListNode(0)
    l2_5 = ListNode(8)
    l2_6 = ListNode(5)
    l2_7 = ListNode(8)
    l2_8 = ListNode(9)
    l2_9 = ListNode(7)
    l2_1.next = l2_2
    l2_2.next = l2_3
    l2_3.next = l2_4
    l2_4.next = l2_5
    l2_5.next = l2_6
    l2_6.next = l2_7
    l2_7.next = l2_8
    l2_8.next = l2_9
   
    sol = Solution()
    result = sol.addTwoNumbers(l1_1, l2_1)
    node = result
    while node != None:
        print(node.val)
        node = node.next