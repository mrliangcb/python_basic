#位运算
# 或运算 |   与 运算 &


#十进制的数不能以0开头，否则报错invalid token   开头加上0b表示这个是二进制数
a=0b000111
b=0b000110
print('二进制与',a&b)   #二进制与  遇到0就为0，全1才是1    这里输出的是十进制数
print('输出二进制格式',bin(a&b))   #输出二进制格式


print(0b000111)#对应十进制7
print(0b000110)# 十进制6
print('十进制与',6&7)#跟二进制一样














