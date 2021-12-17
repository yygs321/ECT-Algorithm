n= int(input())
d=list(input().split())
x=1
y=1
for i in range(len(d)):
  if d[i]=='L':
    if y>1:
      y-=1
  elif d[i]=='R':
    if y<n:
      y+=1
  elif d[i]=='U':
    if x>1:
      x-=1
  elif d[i]=='D':
    if x<n:
      x+=1
print(x,y,end=' ')