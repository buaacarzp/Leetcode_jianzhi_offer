from typing import List
import numpy as np
class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for j in range(6*n+1)]for i in range(n+1)]
        dp[0][0]=1
        print(np.array(dp))
        for i in range(1,n+1):
            for j in range(i,6*i+1): #注意这里是i,因为是从第1个骰子开始遍历
                #假设现在是dp[1][1],那么就需要遍历dp[0][1-1]
                for k in range(1,7):
                    if j-k>=0:
                        dp[i][j]+=dp[i-1][j-k]
        res = list(map(lambda x:x*(1/6)**n,dp[n][n:]))
        return res
n=2
sol =Solution()
res =sol.twoSum(n)
# print(res)