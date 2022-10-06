# Python program to Reverse a number in Python
num = int(input())
rev = 0 
while num > 0: 
 rem = num % 10  
 rev = (rev*10) + rem
 num = num//10  
print("%d " % rev)
