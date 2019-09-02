# 1.使用for...in循环打印九九乘法表
print('九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(i, j, j*i), end=' ')
    print()

# 2.使用whil 循环打印九九乘法表并用条件把偶数行去掉
print('九九奇数乘法表')
i=1
while i<=9:
    j=1
    while j<=i:
        if i%2==0:
            break
        print('{}x{}={}'.format(i, j, j*i), end=' ') 
        j=j+1
    print()
    i=i+1




