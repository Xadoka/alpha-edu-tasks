# str = "Congratulations"
# for i in str:
# 	if i!="a":
# 		print(i, end = '')
				
# print( )

# for j in range(len(str)):
# 	if j==5 or j == 7:
# 		continue
# 	print(str[j], end = '')

###HomeWork
#First task
print("Числа которые делятся на 3, 5, 7, 9 без остатка: " ,end='')
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
        print(i, end=" ")

print(' ')
#Second task
str = "Congratulations"
for j in range(len(str)):
    if j % 2==0:
        print(str[j], end = '')

#!Third task
x=0
total_sum=0

while x<=1000:
  if x % 15 == 0 or x % 17 ==0 or x % 25 ==0:
    print(x)
    total_sum += x
  x+= 1;
print('Сумма всех чисел: ', total_sum)