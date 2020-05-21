class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt=0#计数多少个1
        pre_num = 1#该位之前的数
        # int_i=0#这一位的值
        pow_i=1#第几位
        while pre_num!=0:
            post_num = n%(10**(pow_i-1))
            pre_num = n//(10**(pow_i))
            int_i = (n%(10**pow_i)-n%(10**(pow_i-1)))//(10**(pow_i-1))
            if int_i>1:
                cnt +=(pre_num+1)*(10**(pow_i-1))
            elif int_i==1:
                cnt +=(pre_num)*(10**(pow_i-1))+post_num+1
            else:
                cnt+=(pre_num)*(10**(pow_i-1))
            pow_i+=1
        return cnt 
n=32145
sol =Solution()
res = sol.countDigitOne(n)
print(res)