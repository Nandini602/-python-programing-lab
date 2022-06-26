#python program  to sort the tuple by total digit

tuple=[(45,67),(3,4,6,723),(1234,),(134,234,34)]
print("original list is:" + str(tuple))
result=sorted(tuple,key=lambda tup : sum([len(str(element)) for element in tup]))
print("sortted tuple:"+ str(result))