from collections import deque

#도시의 개수,도로의 개수,원하는 거리 정보, 출발 도시 번호
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]

#도로 정보 입력 받기
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화
distance=[-1]*(n+1)
distance[x]=0 #출발 노드 거리는 0으로 설정

#너비 우선 탐색(BFS)
q=deque([x]) #시작노드 부터 넣음
while q:
  now=q.popleft()
  #시작 노드에서 이동할 수 있는 모든 도시 확인
  for next_node in graph[now]:
    #아직 방문하지 않는 도시라면
    if distance[next_node]==-1:
      #최단 거리 갱신
      distance[next_node]= distance[now]+1
      #시작노드와 인접한 노드들부터 확인
      q.append(next_node)

check=False
for i in range(1,n+1):
  if distance[i]==k:
    print(i)
    check=True

if check==False:
  print(-1)