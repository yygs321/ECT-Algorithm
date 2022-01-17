n=int(input())
a=[]
for i in range(n):
  a.append(list(input().split()))

def setting(data):
  return data[1]

for i in range(n):
  #sorted()한 이후엔 다른 변수에 넣어줘야 함
  a=sorted(a,key=setting) 
  print(a[i][0], end=' ')