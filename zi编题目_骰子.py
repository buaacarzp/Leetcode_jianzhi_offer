'''
问题：有k个筛子，请把可能掷出的所有点数和统计出来
突然想起来可以用迭代的方法去保存从最小值到最大值所有可能的解集
'''
class Solution(object):
    def zhiShaiZi_for(self,k):
        res = [i for i in range(4,(6*k)+1)]
        return res
k=3
sol =Solution()
res =sol.zhiShaiZi(k)
print(res)