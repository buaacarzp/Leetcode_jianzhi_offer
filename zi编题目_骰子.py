'''
问题：有k个筛子，请把可能掷出的所有点数和统计出来
突然想起来可以用迭代的方法去保存从最小值到最大值所有可能的解集
'''
class Solution(object):
    def zhiShaiZi(self,k):
        res = [i for i in range(k,(6*k)+1)]
        print("res=",res)
        def back_track(nums):
            if nums==0:
                self.num+=1
                return 
        self.num=0
        self.number=[]
        for val in res:
            #每一种能取到的值
            for i in range(1,7):
                if val-i<0:
                    continue
                back_track(val-i)
            self.number.append(self.num)
            self.num=0
        
        return self.number

k=2
sol =Solution()
res =sol.zhiShaiZi(k)
print(res)
print(len(res))