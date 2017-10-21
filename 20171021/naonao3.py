# 定义一个函数，返回一元二次方程的两个解
import math

# google is best


def qua(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("数据错误")
    if a == 0:
        print("非一元二次方程")
        if b == 0:
            return "无解"
        else:
            return -c/b

    else:
        d = b**2 - 4*a*c
        if d < 0:
            return "无解"
        else:
            x1 = (-b + math.sqrt(d))/2*a
            x2 = (-b - math.sqrt(d))/2*a
            print(x1 + x2)
print(qua(0, 0, 1))
print(qua(0, 1, 1))
print(qua(2, 1, 1))


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
move(3, 'a', 'b', 'c')
# 切片
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])
M = tuple(range(10))
print(M)
print(M[:3])
A = 'ancdefghigklmnopqrstuvwxyz'
print(A[:2])
print(A[::4])
# 迭代
e = {'a': 1, 'b': 2, 'c': 3}
for key in e:
    print(key)
