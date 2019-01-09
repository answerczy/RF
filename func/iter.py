"""手动迭代模拟for in ,主要通过全局iter方法及next方法
"""
scores = [66,7,4,53,74,42,24]
i = iter(scores)
while  True:
    try:
        s = next(i)
    except StopIteration:
        break
    print(s)
#迭代通过自身的__next__方法
studets = ['tom','jerry','mike']
m = iter(studets)
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
