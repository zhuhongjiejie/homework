'''
def add():
    result =1+2
    print(f"1+2的结果是:{result}")

add()

def add(x,y):
    result =x+y
    print(f"{x}+{y}的结果是:{result}")

add(5,6)


print('summer', '星期天', sep='<-->', end='-->')
print('唱歌')

'''

'''
def fun_defalut_parameters(param1,param2=2):
    print(param1+param2)

    
    fun_defalut_parameters(1)
    fun_defalut_parameters(1, 5)
    '''
'''
#关键字参数的正常调用
def fun_keyword_parameters(param1,param2): 
    print(param1-param2)
    fun_keyword_parameters(param1=5,param2=2)


#关键字参数不按顺序传递
fun_keyword_parameters(param1=1,2)
'''

'''
def fun_parameters(param1,param2,param3):
    if param2<=37.5:
        #print(f'{param1},您的体温小于37.5，体温正常')
        print(f'{param1},您的体温小于37.5，体温正常')

fun_parameters('小明',36,'居家隔离')

def fun_parameters(param1,param2,param3):
    if param2>=37.5:
        print(f'{param1},您的体温大于37.5，体温不正常')
fun_parameters('小张',38,'居家隔离')

'''

'''
def add(a,b):
    result = a+b
    return result


r = add(1, 2)
print(r)
'''

'''
def hesuan(name, tem, asd="居家隔离"):
    if tem <= 37.5:
        print(f"{name},您的体温小于，体温正常")
    else:
        print(f"{name},您的体温大于37.5，需要隔离，隔离方式为{asd}")


name1 = input("请输入您的姓名")
tem1 = float(input("请输入您的体温"))
type2 = input("请输入您的隔离方式")
hesuan(name1, tem1, type2)

'''

'''
def count_character(s, char):
    """
    统计字符串中某个字符出现的次数。

    参数:
    s (str): 要统计的字符串。
    char (str): 要统计的字符。

    返回:
    int: 字符在字符串中出现的次数。
    """
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count
'''
''''
# 使用函数
s = "hello world"
char = "o"
count = count_character(s, char)
print(f"字符 '{char}' 在字符串中出现了 {count} 次。")

'''
'''
def user_info(*args):
    print(args)
    
    
user_info('TOM')
#  ('TOM',18)
user_info('TOM',18)

def user_info(**kwargs):
    print(kwargs)
# {'name':'TOM','age':18,'id':110}
user_info(name='TOM',age=18,id=110)
'''
'''
def sum(*nums):
# 定义一个变量,来保存结果
    result=0
#遍历元组，并将元组中的数进行累加
    for n in nums :
        result +=n
        print(result)

sum(123, 456, 789, 10, 20, 30, 40)
'''
'''
def func_b():
    print("---2----")
def func_a():
    print("---1---")

    func_b()

    print("---3----")

# 调用函数func_a
func_a()
'''
'''
def fun1(x,y):
    print("这是函数一")
    sum=x+y
    return sum

def fun2():
    print("这是函数二")
    sum=fun1(2,3)
    print(sum)
fun2()
'''

'''
def max(x,y):
    return x if x > y else y

def maxs(a, b, c, d):
    res1 = max(a, b)
    res2 = max(res1, c)
    res3 = max(res2, d)

    return res3

print(maxs(5,2,420,299))
'''

'''
def factorial(n):
    if n ==1:
        return 1    # 边界
    else:
        return  n*factorial(n-1)    # 递归函数
# 测试
num=5
result=factorial(num)
print(f"The factorial of {num} is:{result}")
'''

n = int(input())
def F(x):
    if x==1:
        return x #边界
    else:
        return(F(x-1)+1)*2 #递归函数
    print(F(n)) #输出递归函数