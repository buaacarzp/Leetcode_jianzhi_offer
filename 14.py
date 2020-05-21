class Solution:
    def cuttingRope(self, n: int) -> int:
        
        dp=[0,1,2]
        max_dp=0
        if n ==2:return 1
        for j in range(3,n+1):#n=6
            for i in range(1,j):
                max_dp=max(dp[i]*(j-i),max_dp,i*(j-i))
            dp.append(max_dp)
        return dp[n]
        # res =-1
        # print(n)
        # if n ==2:
        #     return 1
        # elif n==1:
        #     return 1
        # for i in range(1,n):
        #     res =max(self.cuttingRope(n-i)*i,(n-i)*i,res)
        #     # print(res)
        # return res
n=int(input())
sol =Solution()
res =sol.cuttingRope(n)
print(res)