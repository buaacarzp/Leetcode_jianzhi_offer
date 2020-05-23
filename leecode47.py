'''
list在哈希中不能去重，所以该如何写
'''
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back_track(nums,temp):
            if len(nums)==0:
                res_all.append(temp)
            for i in range(len(nums)):
                if  i>0 and nums[i]==nums[i-1]:
                    continue
                else:
                    back_track(nums[:i]+nums[i+1:],temp+[nums[i]])       
        temp=[]
        res_all=[]
        nums.sort()
        back_track(nums,temp)
        return res_all
nums =[1,1,2,2]
sol = Solution()
res =sol.permuteUnique(nums)
print(res)