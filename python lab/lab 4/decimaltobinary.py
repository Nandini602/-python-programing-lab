#python program to convert the decimal to binary number
print("enter decimal number:", end=" ")
dnum= int(input())
bnum=0
mul = 1
while dnum>0:
    rem = dnum%2
    bnum=dnum+(rem*mul)
    mul = mul* 10
    dnum=int(dnum/2)
print("\n binary value  is=", bnum)

