n,m=map(int,input().split())
a=[]
for i in range(n):
  a.append(list(map(int,input())))

#재귀함수 사용
def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  #현재노드 아직 방문하지 않았으면 방문처리
  if a[x][y]==0:
    a[x][y]=1

    #상,하,좌,우 재귀 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

count=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      count+=1

print(count)