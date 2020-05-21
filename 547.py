def cal(nums):
    def dfs(nums,visited,v):
        numsv = nums[v]
        for j in range(len(nums[0])):
            # print(j)
            if visited[j]==0 and numsv[j]==1:
                visited[j]=1#0 0 后visited[0]置为1，所以下一次j=1时候进不来
                # print(j)            #要让visited对每一个行的邻接矩阵都初始化一次
                dfs(nums,visited,j)



    visited = [0 for i in range(len(nums))]
    count=0
    for v in range(len(visited)):

        if visited[v]==0:
            count+=1
            dfs(nums,visited,v)
nums = [[1,1,0],[1,1,1],[0,1,1]]
cal(nums)