l = [1,2,5,6,9,8,7,4,12,35,56]
print(l[1:3])#取list中从第一到第二两个元素，第三个截至。注意：list是从0开始的
#所以应当输出的是2和5
print(l[-3:-1])#取的是从右倒数第三个开始数，一直数到倒数第一个不包括倒数第一个
print(l[5:len(l)])#从第五个开始一直取到最后一个
print(l[0:])#输出全部
print(l[0:3])#输出前三个元素
print(l[:3])#输出前三个0省略
print(l[::2])#每两个元素取一个
L = list(range(101))#y由于python 3中range函数生成的不是一个list
#生成的是一个生成器这样可以节约内存，所以需要在前面加一个List这样才可以生成list
print(L[2::3])#取出所有3的倍数，从2开始每隔3取一个数
print(L[0:50:3])#切片操作符中的三个参数分别代表的意思是：
#第一个代表的初始范围，中间的参数代表的是结束范围，第三个代表的是间隔范围
#代表从0开始取到第50个每3个取一个
print(L[-50:-1])#只需要记住最后一个元素 的位序为-1，一个切片操作符时
#前后两个参数分别为起始和截至范围，两个切片操作符时，前两个为起始和截至范围，
#第三个为间隔单位
print(L[-10:])#取出最后十个数字
print(L[-46::5])#取出最后十个五的倍数
#还可以对字符串进行切片操作
s = 'ABCDEFG'
print(s[:3])#打印输出字符串从0开始的到3结束的三个字符
print(s[-3:])#打印输出从倒数第三个开始直至最后一个的字符
s_1 = 'abcdefg'
print(s_1.upper())
#设计一个函数实现对字符串首字母的大写,其余字母小写
def upper_firt(s):
    return s[0].upper()+s[1:].lower()
s = input()
print(upper_firt(s))
