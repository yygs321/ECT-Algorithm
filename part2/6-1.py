n=int(input())

array=[]
for i in range(n):
  a=int(input())
  array.append(a)

array.sort()
for i in range(len(array)-1,-1,-1):
  #-1<i<=len(array)-1 포함관계 주의!
  print(array[i],end=' ')