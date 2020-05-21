class A(object):
    def __init__(self):
        self.head=None
        self.a = 1
    def append(self,nums):
        for i in range(2):
            if self.a==1:
                self.head=nums
                self.a+=1
            
            else:
                nums[:]=[1,2,3]
            print('self.a->',self.a)
            print('self.head->',self.head)
            
        
nums =[3,2,1]
b=1
a =A()
a.append(nums)

# print(nums)
        