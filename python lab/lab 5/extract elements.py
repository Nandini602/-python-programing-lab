# python program to extract the elements with frequency greater than k 
list = [ 1,2,2,4,4,4,5,5,6,4,4,4,6,6,7,5]
k= 5
arr =[]
for i in list:
    freq = list.count(i)
    if freq>k:
        arr.append(i)
print(set(arr))
