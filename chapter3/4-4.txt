r,c=map(int,input().split())
x,y,m=map(int,input().split())
a=[[0 for j in range(c)] for i in range(r)]
for i in range(r):
	b=list(map(int,input().split()))
	for j in range(c):
		a[i][j]=b[j]
  
count=0
result=0
dx=x
dy=y
while True:
  count+=1
  if count<=4:
    if m==0:
      m=3
      dy=y-1
    elif m==1:
      m=0
      dx=x-1
    elif m==2:
      m=1
      dy=y+1
    elif m==3:
      m=2
      dx=x+1
      
    if dx<0 or dy<0 or dx>r or dy>c:
      dx=x
      dy=y   
    else:
      if a[dx][dy]==0:
        a[x][y]=2 #가본 칸은 2로 변경
        result+=1
        x=dx
        y=dy
        count=0
      else:
			#가보거나 바다일 때 x,y좌표값을 원래대로 돌려놔야함!!!
        dx=x 
        dy=y  

  #네 방향 모두 가본 칸이거나 바다로 된 칸인 경우 
  else: 
    result+=1
    a[x][y]=2
    if m==0: #m이 변경되기 전 방향(m=1 동쪽)로 고려해야함
      dy=y-1
    elif m==1:#m=2 남쪽
      dx=x-1
    elif m==2: #m=3 서쪽
      dy=y+1
    elif m==3: #m=0 북쪽
      dx=x+1

    if a[dx][dy]==1:
      break #한칸 뒤로 이동한 곳이 바다면 끝내기
    else:
      count=0
      

print(result)