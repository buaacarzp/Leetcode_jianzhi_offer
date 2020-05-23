from typing import List
class Solution:
    def permute(self, nums):
        def back(nums,temp):
            # print("temp的值为:",sets.add(sum(temp)))
            # res+=temp
            if len(nums)==0:
                res_all.append(temp)
                return 
            for i in range(len(nums)):
                back(nums[:i]+nums[i+1:],temp+[nums[i]]) #如何记录上一次的数组状态？ 
                #将上层的值放在参数中，这样就可以保留上次递归传入的参数值
        res_all=[]
        temp=[]
        # sets=set()
        back(nums,temp)
        # print(sets)
        return res_all
        
s = [1,3]       
sol = Solution()
res = sol.permute(s)
print(res)