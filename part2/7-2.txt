def cutting(array,length,size):
  sum=0
  for i in array:
    s=i-length
    if s<=0:
      s=0
    sum +=s
  if sum<size:
    length-=1
    return cutting(array,length,size)
  else: #요청 길이 이상이면 출력
    return length
    
n,m=map(int,input().split())
rice_cake=list(map(int,input().split()))
#가장 긴 떡의 길이부터 줄여나가기
rice_cake.sort(reverse=True)
length=rice_cake[0]

result=cutting(rice_cake,length,m)
print(result)