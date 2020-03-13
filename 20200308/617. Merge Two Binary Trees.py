# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        ans = [t1.val+t2.val]
        stack = [t1.val]
        visit = [t1.val]
        
        def backtrack():
            if stack:
                return
            else:
                test.stack.pop()
                if t1.left != None and t1.right != None and t2.left != None and t2.right != None:
                    ans.append(t1.left+t2.left)
                    stack.append