class Solution:
    def __init__(self):
        self.cnt=0
    def translateNum(self, nums: int) -> int:
        left=right=0
        if len(nums)==1:
            self.cnt+=1
            return 1
        else:
            left += self.translateNum(nums[1:]) 
        if len(nums)==2:
            self.cnt+=1+left
            return 1+left
        else:
            right += self.translateNum(nums[2:])
        print("debug->")
        return left+right 
nums ='12258'
sol = Solution()
res = sol.translateNum(nums)
print(res)
