n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

result=0

for i in range(m):
  for j in range(n):
    if b[i]==a[j]:
      result=1
    else:
      continue
  if result==1:
    print("yes", end=' ')
  else:
    print("no", end=' ')