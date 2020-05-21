class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: 
                return False
            #能执行到这就说明上面的三个or条件都需要同时满足,满足后还需要判断k当前是否是最后一个元素，
            #如果是最后一个元素，那么就返回true,因为最后一个条件是满足board[i][j] == word[k]
            if k == len(word) - 1: 
                return True
            tmp, board[i][j] = board[i][j],'/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): 
                    return True
        return False
# nums =[["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
nums=[['a']]
word ="bfce"
sol =Solution()
res =sol.exist(nums,word)
print(res)