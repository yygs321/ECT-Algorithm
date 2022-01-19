n=int(input())
data=list(map(int,input().split()))

#작은 값부터 비교해서 최대한의 그룹 만들기
data.sort()

count=0
result=0
for i in data:
  count+=1
  #count값이랑 동일한 수가 나와야 이전i 값들도 그룹 가능하므로
  if count==i:
    result+=1
    count=0