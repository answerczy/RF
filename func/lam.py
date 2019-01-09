# f = lambda x: x**2  x:变量  x**2为返回值 匿名函数通常赋值给f  调用为f()
# gretting = lambda : print('hello')
# gretting()
#
# action = lambda a,b:a+b
# print(action(4,5))
#
# def func(x):
#     f1 =lambda x:x**2
#     f2 =lambda x:x**3
#     return f1(x)+f2(x)
# print(func(2))

x ,y =5,3
funlist = [lambda a,b:a+b,lambda a,b:a-b,lambda a,b:a*b]
for funcd in funlist:
    print(funcd(x,y))

def calculate(a,b,func):
    return func(a,b)
print(calculate(x,y,lambda a,b:a*b))


