'''
import random
lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for _ in range(10)]
print(lst)

#从列表中选择符合条件的元素组成的列表
lst=[i for i in range(10) if i%2==0]
print(lst)
'''


'''
#创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)

#遍历二维列表使用双层for循环
for row in lst: # 行
    for item in row: # 列
        print(item,end='\t')
        print()# 换行

#列表生成式生成一个4行5列的二维列表
lst2=[ [j for j in range(5)]for i in range(4)]
print(lst2)
'''


'''
#使用小括号创建元组
t=('hello',[10,20,30],'phthon','world')
print(t)

#使用内置函数tuple()创建元组
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在:',(10 in t))
print('10在元组中是不存在的:',(10 not in t))
print('最大值:',max(t))
print('最小值:',min(t))
print('len:',len(t))
print('t.index:',t.index(10))
print('t.count',t.count(10))

#如果元组中只有一个元素
t=(10)
print(t,type(t))

#如果元组中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))
'''


'''
t=('python','hello','world')
#根据索引访问元组
print(t[0])
t2=t[0:3:2] #元组支持切片操作
print(t2)

#元组的遍历
for item in t:
    print(item)

# for*range()*len()
for i in range(len(t)):
    print(i,t[i])

#使用enumerate()
for index,item in enumerate(t):
    print(index,'---->',item)

for index,item in enumerate(t,start=11): # 序号从11开始
    print(index,'---->',item)
'''


'''
#(1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时,value值进行了覆盖

# (2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj) # <zip object at 0x000001ECD5A24F00>
# print(list(zipobj)) # [(10, 'cat'),(20, 'dog'),(30, 'pet'),(40, 'zoo')]
d=dict(zipobj)
print(d) # {10: 'cat',20: 'dog',30: 'pet',40: 'zoo'}

#使用参数创建字典
d=dict(cat=10,dog=20) # 左侧cat是key,右侧的是value
print(d)

t=(10,20,30)
print({t:10}) # t是key,10是value,元组是可以作为字典中的key

# lst=[10,20,30]
# print({lst:10}) # TypeError:unhashable type: 'list'
'''