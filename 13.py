class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(m,n,i,j,visited):
            if i<=m-1 and j<=n-1 and sum(list(map(int,str(i)+str(j))))<=k:
                if visited[i][j]==0:
                    print("road=",[i,j])
                    visited[i][j]=1
                    res =1+ (dfs(m,n,i+1,j,visited) + dfs(m,n,i,j+1,visited))
                    return res
                else:
                    return 0
            else:
                return 0
        visited=[[0 for i in range(n)] for j in range(m)]
        res =dfs(m,n,0,0,visited)
        return res
m,n,k=38,15,9
sol =Solution()
res = sol.movingCount(m,n,k)       
print(res)
        #121
        # 38 15 9       135