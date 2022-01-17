import sys
#input을 sys.std.readline으로 치환(더 빠르게 동작)
input=sys.stdin.readline
INF=int(1e9) #10억(무한)

def dijkstra(start):
  #시작 노드에 대해 초기화
  distance[start]=0
  visited[start]=True
  for j in graph[start]:
    distance[j[0]]=j[1]
  #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    #가장 짧은 거리의 노드 
    now=smallest_node()
    visited[now]=True
    for j in graph[now]:
      cost=distance[now]+j[1] #now에서 j[0]으로 가는 길을 더함
      #현재 노드를 거치는 것(cost)이 더 짧은 경우
      if cost< distance[j[0]]:
        distance[j[0]]=cost

#노드,간선의 개수
n,m=map(int,input().split())
#시작 노드 번호 입력
start=int(input())
#각 노드와 연결된 노드 정보 담는 리스트
graph=[[] for i in range(n+1)]
#방문한 적 있는지 체크하는 리스트
visited=[False]*(n+1)
#최단 거리 테이블 모두 무한으로 초기화
distance=[INF]*(n+1)

#모든 간선 정보 입력받기
for i in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c)) #a에서 b로가는 거리 c

#방문하지 않은 노드 중 거리가 가장 짧은 노드 번호 반환
def smallest_node():
  min_value=INF
  index=0
  for i in range(n+1):
    if distance[i]<min_value and not visited[i]:
      min_value=distance[i]
      index=i
  return index

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])