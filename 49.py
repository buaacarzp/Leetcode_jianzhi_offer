class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp =[1 for i  in range(n)]
        dp=[1]
        cnt=1
        t2=t3=t5=0
        t2_val =2;t3_val=3;t5_val=5
        while 1:#cnt<n:
            if dp[t2]*t2_val == dp[t3]*t3_val == dp[t5]*t5_val:
                print(dp[t2],dp[t3],dp[t5])
                break
            dp.append(min(dp[t2]*t2_val,dp[t3]*t3_val,dp[t5]*t5_val))
            if dp[t2]*t2_val ==dp[cnt]:t2+=1
            if dp[t3]*t3_val ==dp[cnt]:t3+=1
            if dp[t5]*t5_val ==dp[cnt]:t5+=1
            cnt+=1
        return dp[-1]
nums=7
sol =Solution()
res = sol.nthUglyNumber(nums)
print(res)