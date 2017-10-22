import os

print([d for d in os.listdir('.')])
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([y * y for y in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'abc' for n in 'xyz'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

M = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in M])
