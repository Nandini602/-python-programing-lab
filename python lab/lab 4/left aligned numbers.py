# python program to print the number in left aligned
print("pattern of numbers: ")
num = 1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num = num+1
    print()