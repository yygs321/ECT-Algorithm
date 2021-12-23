#괴물을 피ㅐ 탈출하기 위한 최단거리
#BFS : 시작 지점에서 가까운 노드부터 차례대로 모든 노드 탐색 
# -> 모든 노드의 값을 거리 정보로 넣기
from collections import deque

n,m=map(int,input().split())
a=[]
for i in range(n):
  a.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  #Queue구현을 위해 deque라이브러리 사용
  queue=deque()
  queue.append((x,y))

  #큐가 빌때까지 반복
  while queue:
    x,y=queue.popleft()
    for i in range(4): #인접한 모든 노드 방문
      nx=x+dx[i]
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if a[nx][ny]==1:
        a[nx][ny]=a[x][y]+1
        queue.append((nx,ny)) #while문에서 다음노드로 사용
  #제일 마지막노드에 있는 값이 거리
  return a[n-1][m-1]

print(bfs(0,0))