# -*- coding: utf-8 -*-
"""
homework 

費式數列 :由一連串的數字組合成的

規則:
    1 1 2 3 5 8 13 21 34 .....
        (1+1)
          (2+1)
            (2+3)
請用串列的方式來呈現
1. 請利用費式數列算出前25項的總和
2. 請利用費式數列算出2/1,3/2,5/3,8/5,13/8....前25項的和
有空題:
    1
    2 3
    4 5 6
    7 8 9 10
"""
#費式數列算出前25項的總和
Fibonacci=[0,1]
count=0
for i in range(1,27):
    Fibonacci.append(Fibonacci[i-1]+Fibonacci[i])

for i in range(1,26):
    count+=Fibonacci[i]

print(count)   
    
#費式數列算出2/1,3/2,5/3,8/5,13/8....前25項的和
count=0
for j in range(2,27):
    count+= Fibonacci[j+1]/Fibonacci[j]
print(count)

#有空題

number=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in range(5):
    for j in range(0,i):
        print(number[count],end=' ')
        count+=1
    print()
        





