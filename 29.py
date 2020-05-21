class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if len(matrix)==0:return []
        left,right,top,bottom = 0,len(matrix[0]),0,len(matrix) 
        res =[]
        while 1:
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1#为了下次的从做到右还是为了下次的从上到下
            # print(res)
            if top>bottom-1:#不能等于，假设有2*2的矩阵，虽然从左边到右边结束后，top+1，也就是下面的从上到下就不会执行，但是还是要执行从右到左的
                break
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            if left>right-1:
                break
            for i in range(right-1,left-1,-1):#从右到左(0,3)-> ()
                res.append(matrix[bottom-1][i])
            bottom-=1
            if top>bottom-1:
                break
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            if left>right-1:
                break
        return res
nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol =Solution()
res = sol.spiralOrder(nums)
print("out>",res)