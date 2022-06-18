def calculateLength(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length
def sumofdigits(num):
    rem=sum=0
    len=calculateLength(num)

    while(num>0):
        rem=num%10
        sum=sum+(rem**len)
        num=num//10
        len=len-1
    return sum
result =0
print("Diaarium number between 1 to 100")
for i in range(1,101):
    result=sumofdigits(i)
    if(result==i):
        print(i)