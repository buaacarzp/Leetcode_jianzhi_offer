from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def Merge_sort(nums):
            n=len(nums)
            if n<=1:
                return nums
            left = Merge_sort(nums[:n//2])
            right = Merge_sort(nums[n//2:])
            res = []
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    self.cnt+=len(left)-i
                    j+=1
            return res+left[i:]+right[j:]
        self.cnt = 0
        Merge_sort(nums)
        return self.cnt
nums = [7,5,6,4]
sol = Solution()
res = sol.reversePairs(nums)
print(res)