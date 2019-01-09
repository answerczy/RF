"""
filter () 过滤选择项
"""
scores = [75,89,42,70,53,66]
students = ['jerry','tom','mike','dell']
result = []
for i in scores:
    if i > 60:
        result.append(i)
print(result)

print(list(filter(lambda x:x>70,scores)))
print(list(filter(lambda s:'m' in s,students)))