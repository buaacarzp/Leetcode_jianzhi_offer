from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        print(len(postorder))
        if len(postorder)<=1:
            return True
        root_val =postorder[-1]
        
        for left in range(len(postorder)):
            if postorder[left] >root_val:
                break
        for right in range(left,len(postorder)-1):
            if postorder[right]<root_val:
                return False
        # print(left)
        ll=self.verifyPostorder(postorder[:left]) 
        rr=self.verifyPostorder(postorder[left:len(postorder)-1])
        return ll and rr
nums =[4, 6, 7, 5]#[1,3,2,6,5]#[1,6,3,2,5]#[7,4,6,5]#[5,7,6,9,11,10,8]
sol =Solution()
res = sol.verifyPostorder(nums)
print(res)