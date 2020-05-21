def find(nums):
    m,n=len(nums)+1,len(nums[0])+1
    dp= [[0 for j in range(n)] for i in range(m)]
    # print(dp)
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])+nums[i-1][j-1]
    print(dp[m-1][n-1])
nums =[[1]
]
find(nums)