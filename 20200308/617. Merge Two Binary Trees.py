# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        deep = 0
        ans = []
        
        
        def find_deep(tree, k):
            nonlocal deep
            if tree.left == None or tree.right == None:
                if tree.left == None and tree.right == None:
                    deep = max(deep, k)
                else:
                    deep = max(deep, k+1)
            else:
                find_deep(tree.left, k+1)
                find_deep(tree.right, k+1)
        
        
        def merge_tree(t1, t2, k):
            if k == 2:
                if t1 != None and t2 != None:
                    ans.append(t1.val+t2.val)
                elif t1 != None and t2 == None:
                    ans.append(t1.val)
                elif t1 == None and t2 != None:
                    ans.append(t2.val)
                else:
                    ans.append(None)
                return
            else:
                ans.append(t1.val+t2.val)
                merge_tree(t1.left, t2.left, k+1)
                merge_tree(t1.right, t2.right, k+1)
                
        
        find_deep(t1, 0)
        find_deep(t2, 0)
        merge_tree(t1, t2, 0)
        print(ans)
        # return ans