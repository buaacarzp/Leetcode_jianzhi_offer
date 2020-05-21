class node(object):
    def __init__(self,val):
        self.val =val
        self.left = None
        self.right =None

def create_binary_tree(preorder,inorder):
    '''
    找出下一次递归的时候preorder序列和order序列
    '''
    if len(preorder)<1 or len(inorder)<1:
        return None
    root_val =preorder[0]
    root = node(root_val)
    find_index = inorder.index(root_val)
    root.left = create_binary_tree(preorder[1:find_index+1],inorder[:find_index])
    root.right =create_binary_tree(preorder[find_index+1:],inorder[find_index+1:])
    return root 

preorder =[3,9,20,15,7]
inorder =[9,3,15,20,7]
res =create_binary_tree(preorder,inorder)
print(res.val)