n=int(input())
d=[0]*1001

d[1]=1
d[2]=3
for i in range(3,n+1):
  #796796은 숫자가 너무 커질 껄 대비해서 나누는 출제 조건
  d[i]=(d[i-1] + d[i-2]*2) %796796 

print(d[n])