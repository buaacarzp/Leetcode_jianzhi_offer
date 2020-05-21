class Tree(object):
    def __init__(self,val):
        self.val =val
        self.left =None
        self.right =None

class solution(object):
    def __init__(self):
        self.root =None
    def bfs(self,num):
        node =Tree(num)
        if self.root is None:
            self.root =node
            queue = [self.root]
        else:
            node = queue.pop(0)
            if node.left is None:
                node.left =node
                queue.append(node.left)
            elif node.right is None:
                queue.append(node.right)

                
            



'''
  1
 2 
3 
'''


num = [1,2,3,4,5,6]
# BFS(nums)
sol = solution()
sol.bfs(num)
print('end')
