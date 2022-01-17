INF=int(1e9)

#노드,간선의 개수 
n=int(input())
m=int(input())

#2차원 리스트 만들고 모든 값을 무한으로 초기화
#(n+1)개 만들어서 나중에 1~n까지만 확인
graph=[[INF]*(n+1) for i in range(n+1)]

#자기 자신에서 자기자신으로 가는 비용 0
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

#각 간선 입력받아서 초기화
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=c

#점화식에 따라 플로이드-워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#결과 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print("INFINITY", end=' ')
    else:
      print(graph[a][b], end=' ')
  print()