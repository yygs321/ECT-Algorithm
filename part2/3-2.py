r,l=map(int,input().split())
min=0

for i in range(r):
  len=list(map(int,input().split()))
  len.sort()
  if min<=len[0]:
    min=len[0]
print(min)