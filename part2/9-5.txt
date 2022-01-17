import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q=[]
  #시작 노드로 가기 위한 최단 경로는 0
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: #큐가 비어있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist,now=heapq.heappop(q)
		#이미 방문한 코드인지 확인
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count=0
max_d=0
for d in distance:
  if d!=INF:
    count+=1
    max_d=max(max_d,d)

#시작노드는 제외해야 하므로 count-1 출력
print(count-1, max_d)