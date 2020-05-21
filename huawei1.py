inputs= input().split("|")
xingqiji_1  = int(inputs[0].split(" ")[3])
day_1 = int(inputs[0].split(" ")[2])
month_1= int(inputs[0].split(" ")[1])
year_1= int(inputs[0].split(" ")[0])

day_2 = int(inputs[1].split(" ")[2])
month_2= int(inputs[1].split(" ")[1])
year_2= int(inputs[1].split(" ")[0])
day = (year_2-year_1)*365
month = (month_2-month_1)*7
day_o = day_2-day_1
print(day,month,day_o)
res = (day_o+xingqiji_1+day+month)%7
if res==0:
    print(7)
else:
    print(res)