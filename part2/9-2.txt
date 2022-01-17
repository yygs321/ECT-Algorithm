import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

#간선 정보 입력
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  #시작 노드로 가기 위한 최단 경로 0으로 설정, 큐에 삽입
  heapq.heappush(q,(0,start)) #첫번 째 원소가 기준(우선순위: 거리)
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    #현재 노드가 이미 처리된 적 있으면 무시
    if distance[now]<dist:
      continue
    #현재 노드와 인접한 노드들 확인
    for i in graph[now]:
      cost=dist+i[1] #graph에는 거리가 두번째값
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q, (distance[i[0]],i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])