class Solution:
    def exist(self, board, word):
        def dfs(i,j,k):
            # print(i,j,k)
            if i>=0 and i<=len(board)-1 and j>=0 and j<=len(board[0])-1 and k<=len(word)-1:
                if k<len(word)-1 and board[i][j]==word[k] :
                    temp,board[i][j]=board[i][j],'/'
                    '''
                     因为 or 是有阻断效应的，可以起到“剪枝”的效果，
                     例如第一个 dfs(i + 1, j, k + 1) == true 了，就会直接赋值 res = true 了，不会再执行后面三个方向的递归了。若按照你的新写法，先暂存四个方向的结果再 or，
                     那么就算找到了结果，也不会提前返回，仍然要搜索所有的情况。
                    '''
                    res = dfs(i,j+1,k+1) or dfs(i,j-1,k+1) or dfs(i-1,j,k+1) or dfs(i+1,j,k+1)
                    board[i][j]=temp
                elif board[i][j]==word[k] and k==len(word)-1:
                    return True
                else:
                    return False
                return res
            else:
                return False
        k=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(i,j,k)
                res = dfs(i,j,k)
                if res:return True
        return False

nums =[["a","b"],["c","d"]]#[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "abcd"#"ABCCED"
# nums=[['a']]
# word ="bfce"
sol =Solution()
res =sol.exist(nums,word)
print(res)
