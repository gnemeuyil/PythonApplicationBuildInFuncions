# 查看python中所有的内置函数和方法
# dir()函数会生成一个列表的字符串
print(dir(__builtins__))
import builtins
print(dir(builtins))

# abs() 返回指定数字的绝对值
print(abs(-32))
# bin() 返回数的二进制版本
print(bin(150))

# ascii() 函数返回任何对象（字符串，元组，列表等）的可读版本
# ascii() 函数会将所有非 ascii 字符替换为转义字符：
x = ascii("My name is coding")
print(x)
x = ascii("My name is 口丁")
print(x)

# chr() 函数返回代表指定 unicode 的字符
x = chr(78)
print(x)

# split()
print("a+b+c+d+e".split('+'))

# complex() 函数通过指定实数和虚数来返回复数
x = complex(7, 8)
print(x)
x = complex('7+8j')
print(x)

# dir() 函数返回指定对象的所有属性和方法，不带值
# 此函数会返回所有属性和方法，甚至是所有对象默认的内置属性
class Person:
  name = "Bill"
  age = 63
  country = "USA"

print(dir(Person))

# format() 函数把指定值格式化为指定格式
x = format(0.5, '%') # 百分数
print(x)
x = format(250000000000, ',') # 使用‘，’作为千位分隔符
print(x)
x = format(25000, 'x') # 十六进制 
print(x)

# int()	返回整数
print(int(15.58))

# hash() 返回指定对象的哈希值
x = "location"
print(hash(x))

# iter() 返回迭代器对象
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
# ???
# print(next(x))

# 遍历迭代器对象中的元素
lst=[1,2,3,4]
item = iter(lst)    # 创建迭代器对象
for x in item:
    print (x)

import sys         # 引入 sys 模块
lst=[1,2,3,4]
item = iter(lst)
while True:
    try:
        print (next(item))
    except StopIteration:
        print ("reached the end of iteration, Stop the program")
        break
        #sys.exit(0)


# 使用了yield关键词的函数被称为生成器（generator）
# 这些函数返回的是一个迭代器
# 还记得上次我们做过的斐波那契数列函数吗？我们试着用生成来完成一样的任务
import sys
def fibonacci_gen(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f_i = fibonacci_gen(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f_i), end=" ")
    except StopIteration:
        print()
        break
        #sys.exit(0)

# reversed() 函数返回反向的迭代器对象
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
    print(x)

# slice() 函数返回 slice 对象（切片）
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(4)
print(a[x])
y = slice(2,5,2)
print(a[y])

# 常用数学功能range(),min(),max(),round(),sum(),pow()以及sorted()
print(range(6))
x = [1,2,5,8,123,6,8,0]
print(min(x))
print(max(x))
print(sum(x))
print(pow(x[2],x[5]))
print(round(x[5]//x[2]))
print(sorted(x))

