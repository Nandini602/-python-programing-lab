# python program to compute the difference between 2 list
from collections import Counter
list1 = [1,2,3,4,5,6]
list2  = [2,3,4,5,6,7,8]
# arr = []
# for i in range(len(len(list1))):
#     if i in list:
#         if i not in list2:
#             arr.append(i)
# print(arr)
a=Counter(list1)
b=Counter(list2)
print(list(a-b))
print(list(b-a))
