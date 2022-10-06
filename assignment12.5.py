#Write a python script to find next prime number of a given number
def nextprime(n):
    p=n+1
    for i in range(2,p):
        if(p%i==0):
            p=p+1
    else:
        print(p,end=" ")
n=int(input())
nextprime(n)