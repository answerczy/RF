"""模块搜索路径：
1.程序主目录
2.系统环境变量sys.path 即python-path中去找
3.标准库目录
4.任意的.pth目录中去搜索
5.第三方扩展库site-packages中去找
"""
import b
greting = 'hello'
def  print_hello():
    print(greting)
print_hello()
b.print_b_time()
b.print_c()