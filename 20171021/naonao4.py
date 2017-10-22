from collections import Iterable
# 判断字符串是否可迭代
a = isinstance("abc", Iterable)
print(a)
# 判断list是否可迭代
b = isinstance([1, 2], Iterable)
print(b)
# 判断tuple是否可迭代
c = isinstance((1, 2), Iterable)
print(c)
# 判断整数是否可迭代
d = isinstance(123, Iterable)
print(d)
# python内置的enumerate可以把list变成索引元素对
for x, value in enumerate(['A', 'B', 'C']):
    print(x, value)
