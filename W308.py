#分解五位數
a=int(input('請輸入一個五位數:'))
x=a//10000
y=(a-x*10000)//1000
z=(a-x*10000-y*1000)//100
b=(a-x*10000-y*1000-z*100)//10
c=a-x*10000-y*1000-z*100-b*10

print(x)
print(y)
print(z)
print(b)
print(c)