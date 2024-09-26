#數字奇偶判斷
a=int(input('輸入數字:'))
x=a%2
while(x==0):
    print("結果:",a,"是偶數")
    break

while(x==1):
    print("結果:",a,"是奇數")
    break
