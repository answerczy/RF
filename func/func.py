#任意参数
# def avg(a,*args):
#     return (a+sum(args))/(1+len(args))
# print(avg(3,4,5,3,4,65,7))
#
# def func(a,*args):
#     print(a,args)
# t=(10,20,30)
# func(1,*t)
def funcb(a,*args,**kwargs):
    print(a,args,kwargs)
employee = {'name':'tom','job':'dev'}
funcb(22,332,545,64,name='tom',age=20)
funcb(232,43,53,**employee)