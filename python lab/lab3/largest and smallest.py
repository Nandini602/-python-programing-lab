
#python program to print largest and samllest elements in array

arr=[ 12,34,56,78,95,70,64]
print("the array is ")
min =arr[0]
max =arr[0]
print("min and max elements  are :")
for i  in range (len(arr)): 
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max =arr[i]
print(min)
print(max)

