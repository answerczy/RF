"""map函数映射函数到可迭代对象上 map(func,iterable)
"""
scores = [78,65,86,45,67.3]
def func(x):
    return x+2
print(list(map(func,scores)))

students = ['tom','jerry','mike']
print(list(map(lambda s:s.upper(),students)))