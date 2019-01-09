#值传递，函数外不可变对象在函数传递的时候传递的是值的副本
# x = 5
# def changenum(a):
#     a += 10
#     print(a)
# changenum(x)
# print(x)

#可变对象在函数传递，传递的是函数的引用
l = [1,2,3]
l2=[3,4,5]
l3=l2.copy()
def changelist(a):
    a[0] = 99
    print(a)
changelist(l)
print(l)
changelist(l3)
print(l2)