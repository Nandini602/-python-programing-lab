# python program to find the tuple which have all elemets divisible by k from the list of tuple
tuple = [(6,24,12),(7,9,6),(12,18,21)]
print("the original list is "+str(tuple))
k=6
res=[sub for sub in tuple if all(ele % k ==0 for ele in sub )]
print("k multiple elemets tuples:"+ str(res))