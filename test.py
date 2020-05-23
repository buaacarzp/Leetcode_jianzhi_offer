from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        def back(nums,temp):
            # print("temp的值为:",sets.add(sum(temp)))
            # res+=temp
            if len(nums)==0:
                sets.add(temp)
                res_all.append(temp)
                return 
            for i in range(len(nums)):
                # print(temp+[nums[i]])
                back(nums[:i]+nums[i+1:],temp+nums[i]) #如何记录上一次的数组状态？ 
                #将上层的值放在参数中，这样就可以保留上次递归传入的参数值
        res_all=[]
        temp=''
        sets=set()
        back(s,temp)
        # print(sets)
        
        return list(sets)
s='aabaaba'
sol = Solution()
res =sol.permutation(s)
print(res)