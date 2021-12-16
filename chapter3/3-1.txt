n,m,k=map(int,input().split())
a=input().split()
for i in range(n):
  a[i]=int(a[i])
max=0
max2=0
num=0
#가장 큰 수가 2개인 경우 : max와 max2에 넣음
for i in range(n):
  if max<a[i]:
    max=a[i]
    num=i
  elif max==a[i]:
    max2=max
#가장 큰 수가 1개인 경우: 그 다음 큰 수 max2에 넣음
if max2==0:
  del a[num]
  for i in range(n-1):
    if max2<a[i]:
      max2=a[i]
#max값을 k번씩 m//k번 더하므로 나머지 횟수만큼만 max2값 더함
sum=0
for i in range(m-(k*(m//k))):
  for j in range(k):
    sum+=max
  sum+=max2

print(sum)