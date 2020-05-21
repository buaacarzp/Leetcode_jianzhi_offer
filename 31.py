from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[];popi=0
        for i in pushed:
            stack.append(i)
            while stack and popi<len(poped) and stack[-1]==popped[popi]:
                print('stack={},popped={},popi'.format(stack,popped[popi:]),popi)
                stack.pop()
                # popped.pop(popi)
                popi+=1
                
        if popi==len(popped) :
            return True
        else:
            return False
pushed =[1,2,3,4,5]
poped = [5,4]#[4,5,3,2,1]
sol =Solution()
res = sol.validateStackSequences(pushed,poped)
print(res)