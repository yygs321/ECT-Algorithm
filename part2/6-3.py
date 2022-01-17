n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#배열 A의 가장 작은 수와 배열 B의 가장 큰 수 비교해서 바꿔치기
a.sort()
b=sorted(b,reverse=True)
#b=sort(reverse=True)도 가능

for i in range(k):
  if(a[i]<=b[i]):
    a[i],b[i]=b[i],a[i]
  else:
    break

print(sum(a))