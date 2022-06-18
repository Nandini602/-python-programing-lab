# python program find the tranpose of matrix
a=[[1,2],
  [4,5],
  [6,7]]

result= [[0,0,0],
        [0,0,0]]
for i in range(len(a)):
  for j in range(len(a[0])):
    result[j][i]=a[i][j]
for r in result:
  print(r)




