'''
序列化二叉树
'''
# import time
from collections import deque
class TreeNode(object):
    def __init__(self,val):
        self.val =val
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.ls=[]
    def serialize(self, root):
        if not root:
            return []
        queue =[root]
        while queue:
            cur = queue.pop(0)
            if cur=='null':
                self.ls.append('null')
            else:
                self.ls.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                else:
                    queue.append('null')
                if cur.right:
                    queue.append(cur.right)
                else:
                    queue.append('null')
        print(self.ls)
        return self.ls
    def deserialize(self, data):
        '''
        迭代
        '''
        self.node =None
        queue =[]
        for i in  range(len(data)):
            if i ==0:
                self.node =TreeNode(data[i])
                queue.append(self.node)
            # if not queue:return 
            parent = queue.pop(0)
            left = TreeNode(data[2*i+1]) if 2*i+1 <=len(data)-1 else None#TreeNode('null')
            right = TreeNode(data[2*i+2]) if 2*i+2 <=len(data)-1 else None#TreeNode('null')
            parent.left = left
            parent.right = right 
            queue.append(parent.left)
            queue.append(parent.right)           
        return self.node
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:return []
    #     stack = deque([root])
    #     res = []
    #     cur_level = 1
    #     next_level = 0

    #     while cur_level>0: #stack or cur_level>0
    #         cur = stack.popleft()

    #         if cur:
    #             cur_level -= 1
    #             res.append(cur.val)
    #             stack.append(cur.left)
    #             stack.append(cur.right)
                    
    #             if cur.left:
    #                 next_level+=1
    #             if cur.right:
    #                 next_level+=1
    #         else:
    #             res.append('null')

            
    #         if cur_level==0:
    #             cur_level=next_level
    #             next_level = 0

    #     return res

    
    # def deserialize(self, data):
    #     '''
    #     递归
    #     '''
    #     def recur(val ):
    #         node = TreeNode(data[val])
    #         if 2*val+1 <=len(data)-1:
    #             node.left = recur(2*val+1) 
    #         if 2*val+2 <=len(data)-1:
    #             node.right = recur(2*val+2)        
    #         return node
    #     return recur(0)
       
nums =[1,2,3,"null","null",4,5]#[1,2,3]#[1,2,3,'null','null',4,5,'null','null','null','null',7]
sol =Codec()
res = sol.deserialize(nums)
res = sol.serialize(res)
print(res)
# sol.deserialize(nums)
# for i in nums:
#     sol.append(i)
# # sol.bfs(sol.root)
# print(sol.root.val)
# print(sol.root.left.val)
# print(sol.root.right.val)
# print(sol.root.right.left.val)