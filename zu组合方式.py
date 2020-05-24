'''
给定一个数k，求出从1-k中和为k的所有可能性,要求不能有重复的数
结果是对的，但是含有重复的元素
'''
def sumk(k):
    def back_track(nums,temp):
        if sum(temp)==k :
            res_all.append(temp)
            return        
        for i in range(len(nums)):
            if sum(temp)>k:
                break
            back_track(nums[:i]+nums[i+1:],temp+[nums[i]])
        
    res_all=[]
    nums =[i for i in range(1,k)]
    back_track(nums,[])
    # print(nums)
    return res_all

'''
将nums[:i]+nums[i+1:] 改成nums[i+1:]即可保证每组元素出现的数是不一样的
现在如果限制temp的个数为n，那么只需要加一个判断即可
'''
def sumk2(k):
    def back_track(nums,temp):
        if sum(temp)==k :
            res_all.append(temp)
            return        
        for i in range(len(nums)):
            if sum(temp)>k:
                break
            back_track(nums[i+1:],temp+[nums[i]]) 
        
    res_all=[]
    nums =[i for i in range(1,k)]
    back_track(nums,[])
    # print(nums)
    return res_all
def sumk3(k,n):
    def back_track(nums,temp):
        if sum(temp)==k and len(temp)==n:
            res_all.append(temp)
            return        
        for i in range(len(nums)):
            if sum(temp)>k:
                break
            back_track(nums[i+1:],temp+[nums[i]])
        
    res_all=[]
    nums =[i for i in range(1,k)]
    back_track(nums,[])
    return res_all
'''
现在回到掷骰子的题目，要求的是n为筛子的个数，并且不要求有重复的元素，以为是一个全排列加上和和sum的问题
'''
def sumk4(k):
    def back_track(nums,sumk,temp):
        if sum(temp)==sumk and len(temp)==k:
            res_all.append(temp)
            return        
        for i in range(len(nums)):
            if sum(temp)>sumk or len(temp)>k:
                break
            back_track(nums,sumk,temp+[nums[i]])
        
    res_all=[]
    res_all_sumk=[]
    nums =[i for i in range(k,(k*6)+1)]
    for sumk in nums:
        val =[i for i in range(1,6+1)]
        back_track(val,sumk,[])
        res_all_sumk.append(len(res_all))
        # res_all_sumk.append((res_all))
        res_all=[]
    return res_all_sumk
def sumk21(k):
    def back_track(nums,temp):
        if sum(temp)==k :
            res_all.append(temp)
            return        
        for i in range(len(nums)):
            if sum(temp)>k:
                break
            back_track(nums,temp+[nums[i]])
        
    res_all=[]
    nums =[i for i in range(1,k)]
    back_track(nums,[])
    return res_all
k=3
res = sumk4(k)
print(res)
# ls = list(map(lambda x : x*(1/6)**k,res)) #9应该是25个，但是我算出来的是28个
# print(ls)
# import numpy as np
# print(np.array(res))
