# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, inorder, postorder):
        if len(postorder)<1 or len(inorder)<1:return None
        root_val = postorder[-1]
        print(root_val)
        root = TreeNode(root_val)
        find_index = inorder.index(root_val)
        root.left = self.buildTree(inorder[:find_index],postorder[:find_index])
        root.right = self.buildTree(inorder[find_index+1:],postorder[find_index:-1])
        return root
'''
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
'''
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol =Solution()
res = sol.buildTree(inorder,postorder)
print(res)