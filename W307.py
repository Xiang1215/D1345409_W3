#進制轉換
a=int(input('輸入一個十進制數字:'))

print("二進制:",'{:0b}'.format(a,'b'))
print("八進制:",'{:0o}'.format(a,'o'))
print("十六進制:",'{:0x}'.format(a,'x'))