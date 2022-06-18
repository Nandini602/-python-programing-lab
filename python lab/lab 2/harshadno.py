#python program to check the given number is harshad no. or not

n=int(input("enter the number"))
sum=0
for i in str(n):
    sum+=int(i)
if n%sum==0:
    print(n,"is the harshad number")
else:
    print(n,"is not a harshad number")

