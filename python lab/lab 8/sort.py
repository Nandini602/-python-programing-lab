# sort the python dictionary by key and the value

key_value={}
key_value[5]=10
key_value[3]=8
key_value[6]=77
key_value[4]=23

print("sorting  on the basic of values")

print(sorted(key_value.items(),key=lambda keyval: (keyval[1],keyval[0])))