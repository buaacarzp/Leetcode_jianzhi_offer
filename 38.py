from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(s,start,temp):
            if len(temp)==len(s):
                res.append(temp.copy())
                return 
            for i in range(start,len(s)): 
                temp.append(s[i])
                print('debug->')
                dfs(s,i+1,temp)#i = 0 a b c  i=1 
                temp.pop()
                print('????')
            return 
        temp,res=[],[]
        dfs(s,0,temp)
        return res
nums='abc'
sol =Solution()
res = sol.permutation(nums)
print(res)
        