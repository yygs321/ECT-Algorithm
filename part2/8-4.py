n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))

#m의 최대 크기가 10000이므로 불가능한 수로 10001 설정
d=[10001]*(m+1)

d[0]=0 #아무 화폐도 쓰지 않았을 때
for i in range(n):
  for j in range(array[i],m+1):
    #이전 화폐단위들로만 만들었을 경우/ 새로운 화폐를 쓰는 경우 
    d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])