# program to count the occurrence of the each word in given sentence 
a= list(map(str,input("enter te sentence").split()))
s=set(a)
for i in s :
    print(i,"occures",(a.count(i)),"time")