d5_list=[0,1,2,3,4,5,6,7,8,9]
#将数组翻转
d5_list.reverse() 
print(d5_list)
print('\n')

#翻转后的数组拼接成字符串
s=''
for i in range(0,10):
    d5_list[i]=str(d5_list[i])
d5_string=s.join(d5_list)
print(d5_string)

#字符串切片

d5_string_1=d5_string[2:8]
print(d5_string_1)

