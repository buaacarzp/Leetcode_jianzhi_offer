import numpy as np 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p)+1)]for i in range(len(s)+1)]
        dp[0][0]=True
        for j in range(len(p)):
            if p[j]=='*':
                dp[0][j+1]=dp[0][j-1]
        # print(np.array(dp)) 
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i]== p[j] or p[j]=='.':
                    # a  a       a .
                    dp[i+1][j+1]=dp[i][j]
                elif p[j]=='*':
                    if s[i]==p[j-1] or p[j-1]=='.':
                        dp[i+1][j+1]=dp[i][j+1] #or dp[i+1][j-1]
                    dp[i+1][j+1] |=dp[i+1][j-1]
        print(np.array(dp))
        return dp[-1][-1]   

            


s="missi"
p="mis*i"

sol =Solution()
res = sol.isMatch(s,p)
'''
1.
"abcd"
"d*"
或者：
"missi"
"mis*"
这种情况不能直接取复制位置，应该为false，输出了True,因为复制前需要确定s[i]与p[j-1]是相等的。
2.
即使加上了复制的限制条件,但是
"ab"
".*"
就不行了,因此判断条件可以再加上p[j-1]是'.'
3.
"missi"
"mis*i"
这种情况下，应该为true，输出了false
原因是因为把删除的条件放在了复制的条件下，应该是放在 p[j]=='*'下面
'''