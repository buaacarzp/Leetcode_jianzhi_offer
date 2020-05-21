def find(nums):
    window=''
    i=0
    max_temp=0
    # print(len(nums))
    while i<len(nums):
        if nums[i] not in window:
            window+=nums[i]
        else:
            index_ = window.index(nums[i])
            window = window[index_+1:]+nums[i]
        max_temp=max(len(window),max_temp)
        i+=1
    # print(window)
    return max_temp
nums="aabaab!bb"
res = find(nums)
print(res)