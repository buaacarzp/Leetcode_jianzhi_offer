class Solution:
    def findNumberIn2DArray(self, matrix, target):
        N,M = len(matrix),len(matrix[:1])
        if M<1:return False
        print(111)
        def binary_search(nums,target):
            i=0;j=len(nums)-1
            print(i,j)
            while i<=j:
                mid =(i+j)//2
                if target>nums[mid]:
                    i=mid+1
                elif target<nums[mid]:
                    j=mid-1
                else:
                    return True
            return False
        for i in range(N):
            print("fuck?")
            status=binary_search(matrix[i],target)
            if status:return True 
        return False

nums =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target =20

sol =Solution()
res = sol.findNumberIn2DArray(nums,target)
print(res)