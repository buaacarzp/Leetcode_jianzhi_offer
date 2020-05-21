'''
堆排序
'''
def heapify(n,i,tree): #维护堆
    #假设i是最大值
    c1 = 2*i+1
    c2 = 2*i+2
    
    if i>=n:
        return
    maxi=i
    if c1<n and tree[c1]>tree[i]:
        maxi=c1
    if c2<n and  tree[c2]>tree[maxi]:
        maxi=c2
    if maxi!=i:
        tree[maxi],tree[i]=tree[i],tree[maxi]
        heapify(n,maxi,tree)
   
    '''
    小于符号就是让小的浮上来，大于符号就是让大的浮上来。为什么这么做？是因为会剔除掉最后一个结点
    '''
    # mini=i
    # if c1<n and tree[c1]<tree[i]:
    #     mini=c1
    # if c2<n and  tree[c2]<tree[mini]:
    #     mini=c2
    # if mini!=i:
    #     tree[mini],tree[i]=tree[i],tree[mini]
    #     heapify(n,mini,tree)
    
def build_headp(tree,n):#创建堆:父节点大于子节点，建立最大堆是从下岛上
    last_node =n-1
    parent_node = (last_node-1)//2
    while parent_node>=0:
        heapify(n,parent_node,tree)
        parent_node-=1
def heap_sort(tree,n):
    build_headp(tree,n)
    last_node =n-1
    for i in range(last_node,-1,-1):
        # print(i)
        tree[i],tree[0]=tree[0],tree[i]
        heapify(i,0,tree)#注意维护最大堆是从上到下
        print('->\n')
    


nums = [2,5,3,1,10,10,4]
