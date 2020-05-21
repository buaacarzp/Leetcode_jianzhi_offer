class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        A =nums[-k:]
        B =nums[:k]
        print(A,'\n',B)
        for i in range(len(A)):
            nums[i]=A[i]
        for i in range(len(A),len(A)+len(B)+1):
            nums[i]=B[i-len(A)]
        return nums
nums = [1,2,3,4,5,6,7];k = 3
sol =Solution()
res = sol.rotate(nums,k)
print(res)