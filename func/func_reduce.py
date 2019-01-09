"""reduce(func,iterable)合并减少 来自functools
"""
from functools import reduce
scores = [88,74,67,53,24,78]
summ = 0
for x in scores:
    summ += x
print(summ)
def func(x,y):
    return x+y
print(reduce(func,scores))
print(sum(scores))
print(reduce(lambda x,y:x+y,scores))
