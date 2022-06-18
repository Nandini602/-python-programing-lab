# python program to check if the list contains 3 consecutive numbers
arr = [ 2,1,1,1,2,2,2,3]
i=len(arr)
for i in range(i-2):
    if arr[i] ==arr[i+1] and arr[i+1] ==arr[i + 2]:
        print(arr[i])
