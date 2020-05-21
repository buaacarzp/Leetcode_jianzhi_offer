def search(nums):
    dicts={}
    for i in nums:
        if i not in dicts:
            dicts[i] =1
        else:
            dicts[i]+=1
    print(dicts)
    for i in dicts:
        if dicts[i]==1:
            return i
    return " "
nums='abaccdeff'
res = search(nums)
print(res)