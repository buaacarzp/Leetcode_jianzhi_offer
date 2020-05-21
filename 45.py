from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def merge_sort(nums):
            n = len(nums)
            if n<=1:
                return nums
            left = merge_sort(nums[:(n)//2])
            right = merge_sort(nums[(n)//2:])
            result = []
            i=j=0
            while i<=len(left)-1 and j<=len(right)-1:
                if left[i]+right[j]<right[j]+left[i]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            # print("left[i:]={},right[j:]={}".format(left[i:],right[j:]))
            return result+(left[i:])+(right[j:])
        nums =list(map(str,nums))
        # print(nums)
        res = merge_sort(nums)
        res = ''.join([i for i in res]) 
        return res
nums = [3,30,34,5,9]
sol =Solution()
res = sol.minNumber(nums)
print(res)