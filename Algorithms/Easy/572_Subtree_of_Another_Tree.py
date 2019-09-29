'''
Given two non-empty binary trees s and t, check whether tree t has exactly the 
same structure and node values with a subtree of s. A subtree of s is a tree 
consists of a node in s and all of this node's descendants. The tree s could 
also be considered as a subtree of itself.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
# Solution 1
# Runtime: 76 ms, faster than 97.75% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.3 MB, less than 10.00% of Python3 online submissions for Subtree of Another Tree.

class Solution(object):
    def isSubtree(self, s, t):
        def traverse_tree(node):
            if not node: return None
            return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
        return traverse_tree(t) in traverse_tree(s)
'''

# Solution 2
# Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.1 MB, less than 10.00% of Python3 online submissions for Subtree of Another Tree.

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(a, b):
            if not a or not b:
                return not a and not b
            if a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right):
                return True
            if b is t:
                return dfs(a.left, t) or dfs(a.right, t)
            
            return dfs(a, t)
        
        return dfs(s, t)

if __name__ == "__main__":
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    sol = Solution()
    result = sol.isSubtree(s, t)
    print(result)