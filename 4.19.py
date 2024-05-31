"""s = "helloworld"
for i in range(0, len(s)):
    print(i, s[i], end='\t\t')
# print转到
print('\n' + '-' * 40)
# 40-分界
for i in range(-10, 0):
    print(i, s[i], end='\t')
# 7.左闭右开

s = "helloworld"
s1 = s[0:5:2]
print(s1)
# 省略开始位置
print(s[:5:1])
# 省略结束位置
print(s[0:7:1])
# 省略步长
print(s[0:6])
# 省略开始位置,结束位置，步长(默认1)
print(s[::])

# 步长为负，表示从后向前提取字符
s = "helloworld"
print(s[::-1])
print(s[-1:-11:-1])
print('-' * 40)
# 从0开始，向后方逆序步长为1输出，因为0左侧没有数值，所以为空
print(s[0:10:-1])
print('-' * 40)
print(s[4:-11:-1])

s = "helloworld"
print("e在s中存在吗?", 'e' in s)
print("v在s中存在吗?", 'v' in s)
print("e在s中不存在吗?", 'e' not in s)
print("v在s中不存在吗?", 'v' not in s)
# 内置函数的使用
print('len():', len(s))
print('max():', max(s))
print('min():', min(s))
print('s.index(o):', s.index('o'))
# print('s.index(v):',s.index('v'))
print('s.count(l):', s.count('l'))

# 直接使用[]创建列表
lst = ['hello', 'world', 98, 100.5]
print(lst)

# 可以使用内置的函数list()创建列表
lst2 = list('helloworld')
lst3 = list(range(1, 10, 2))
print(lst2)
print(lst3)

#
lst4 = [10, 20, 30]
print(lst4)

del lst4
print(lst4)

# 序列的相乘操作
print(lst+lst2+lst3)
print(lst * 3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o'))  # 统计o的个数
print(lst2.index('o'))

lst = ['hello', 'world', 'python', 'php']
for item in lst:
    print(item)
#
for i in range(0, len(lst)):
    print(i, '--->', lst[i])

#
for index, item in enumerate(lst):
    print(index, item)
    #
for index, item in enumerate(lst,1):
    print(index, item)

lst = ['hello', 'world', 'python']
print('原列表:', lst, id(lst))
#
lst.append('sql')
print('增加元素之后:', lst, id(lst))

lst.insert(__index=1, __object=100)
print(lst)
lst.remove('world')
print('删除元素之后的列表:', lst, id(lst))

print(lst.pop(1))
print(lst)
# 清楚列表中所有的元素clear()
# lst.clear()
# print(lst.id(lst))

new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))

# 元素的修改
"""
lst = [4, 56, 3, 78, 40, 56, 89]
print('原列表:', lst)
#
lst.sort()
print('升序:', lst)
#
lst.sort(reverse=True)
print('降序:', lst)

lst2 = ['banana', 'apple', 'Cat', 'Orange']
print('原列表：', lst2)
#
lst2.sort()
print('升序:', lst2)
#
lst2.sort(reverse=True)
print('降序:', lst2)
#
lst2.sort(key=str.lower)
print(lst2)

# 两种不同的排序
lst = [4, 56, 3, 78, 40, 56, 89]
print('原列表:', lst)
# 排序
asc_lst = sorted(lst)
print('升序', asc_lst)
print('原列表', lst)
# 降序
desc_lst = sorted(lst, reverse=True)
print('降序', desc_lst)
print('原列表', lst)
