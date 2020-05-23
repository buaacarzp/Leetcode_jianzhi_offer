'''
记录版本
'''
class Solution:
    def translateNum(self, num: int) -> int:
        def back_track(nums,temp):
            if len(nums)==0:
                res_all.append(temp)
                return 
            
            back_track(nums[1:],temp+'|'+nums[:1]+'|')
            if len(nums)>=2:
                back_track(nums[2:],temp+'|'+nums[:2]+'|')
        temp = ''
        res_all=[]
        back_track(num,temp)
        return res_all
nums ='12258'
sol =Solution()
res = sol.translateNum(nums)
print(res)
'''
题解版本
'''
class Solution:
    def translateNum(self, num: int) -> int:
        def back_track(nums):
            if len(nums)==0:
                nonlocal res_all
                # res_all.append(temp)
                res_all +=1
                return 
            if nums[:1]=='0':
                return 
            back_track(nums[1:])
            # back_track(nums[1:],temp+'|'+nums[:1]+'|')
            if len(nums)>=2:
                if nums[:2]>'25':
                    return 
                back_track(nums[2:])
        # temp = ''
        res_all=0
        back_track(num)
        return res_all