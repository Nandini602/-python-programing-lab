# python program to remove the ith occurrence of the give word in the list where words repeat
def omit (l1,w,n):
    c=0
    idx = 0
    for i in l1 :
        idx+=1
        if i==w:
            c+=1
            if c==n:
                l1.pop(idx-1)
    return l1
l1=["the", "boy","is","smart","he","is","intelligents","he","is","silents"]
w="is"
n=2
print("new list is:",omit(l1,w,n))