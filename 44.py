class Solution:
    def findNthDigit1(self, n: int) -> int:
        # 首先判断target是几位数，用digits表示
        base = 9
        digits = 1
        while n - digits*9 * 10**(digits-1) > 0:
            n -= digits*9 * 10**(digits-1)
            digits += 1
        start = 10**(digits-1)
        number = start+(n-1)//digits
        single = (n-1)%digits
        return(int(str(number)[single]))
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        print(start)
        print(digit)
        num = start + (n - 1) // digit # 2.
        print(num)
        print( int(str(num)[(n - 1) % digit])) # 3.



        
n=123#20#19
sol =Solution()
res = sol.findNthDigit1(n)
print(res)
