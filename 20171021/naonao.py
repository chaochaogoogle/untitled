# 条件循环判断肥胖程度
height = 1.75
weight = 80.5
bmi = weight / height ** 2

if bmi < 18.5:
    print("过轻")
elif 18.5 < bmi < 25:
    print("正常")
elif 25.0 < bmi < 28:
    print("过重")
elif 28.0 < bmi < 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")
# 自己生成数字
a = list(range(5))
print(a)
# 计算0-100的和
sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)
# 计算0-100所有奇数的和
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)
# 利用循环依次对list中的名字打印出hello，xxx！
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello," + name + "!")
# 利用循环依次对list中的名字打印出hello，xxx！
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello,%s!" % name)
