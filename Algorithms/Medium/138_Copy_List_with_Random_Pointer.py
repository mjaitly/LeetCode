'''
A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.
Return a deep copy of the list.
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
'''

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

'''
# Soultion 1
# Runtime: 52 ms, faster than 39.52% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 16 MB, less than 6.98% of Python3 online submissions for Copy List with Random Pointer.
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            node = Node(p.val, None, None)
            node.next = p.next
            p.next = node
            p = p.next.next
            # p = node.next
        p = head    
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead
'''
# Solution 2
# Runtime: 48 ms, faster than 71.80% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 16.1 MB, less than 6.98% of Python3 online submissions for Copy List with Random Pointer.
class Solution:
    def copyRandomList(self, head):
        curNode = head
        nodeTable = {}
        while curNode:
            nodeTable[curNode.val] = Node(curNode.val, None, None)
            curNode = curNode.next
        
        n1 = head
        n2 = result = Node(0, None, None)
        while n1:
            n2.next = nodeTable[n1.val]
            if n1.next:
                n2.next.next = nodeTable[n1.next.val]
            if n1.random:
                n2.next.random = nodeTable[n1.random.val]
            n2 = n2.next
            n1 = n1.next
        return result.next

'''
class Solution:
    def copyRandomList(self, head):
        if head == None:
            return head

        if head.next == None:
            new_node = Node(head.val, None, None)
            if head.random == None:
                return new_node
            else:   
                new_node.random = new_node
                return new_node

        else:
            curr = head
            while curr != None:
                new_node = Node(curr.val, curr.next, curr.random)
                new_node.next = curr.next
                curr.next = new_node 
                curr = curr.next.next
            
            curr = head 
            while curr != None:
                curr.next.random = curr.random.next
                curr = curr.next.next

            curr = head
            copied_head = curr.next
            while curr.next != None:
                temp = curr.next
                curr.next = curr.next.next
                curr = temp 
            return copied_head
'''

if __name__ == "__main__":
    sol = Solution()
    # head = None
    # node2 = Node(2, None, None)
    # node2.random = node2
    # head = Node(1, node2, node2)
    # node2 = Node(2, None, None)
    
    # head = Node(-1, None, None)
    # head.random = head
    node2 = Node(1, None, None)
    head = Node(-1, node2, node2)
    result = sol.copyRandomList(head)
    while head != None:
        string = "head.val " + str(head.val) + " head.next " + str(head.next) + " head.random " + str(head.random)
        print(string)
        head = head.next
