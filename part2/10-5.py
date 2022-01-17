from collections import deque

v,e=map(int,input().split())
#모든 노드에 대한 진입차수 0으로 초기화
indegree=[0]*(v+1)
#각 노드에 연결된 간선 정보 담기 위한 연결리스트 초기화
graph=[[] for i in range(v+1)]
'''
indegree처럼 []안에 int들어간 경우는 [0]*(v+1) 가능
graph 같이 리스트 안의 값이 비어있는 경우는 다른 방식

'''

#방향 그래프의 모든 간선 정보 입력
for _ in range(e):
  a,b=map(int,input().split())
  graph[a].append(b) #정점 A에서 B로 이동가능
  #b의 진입차수 1 증가
  indegree[b] +=1

#위상정렬 함수
def topology_sort():
  result=[]
  q=deque()

  #처음 시작 시 진입차수가 0인 노드 큐에 삽입
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  #큐가 빌 때까지 반복
  while q:
    now=q.popleft()
    result.append(now)
    #해당 원소와 연결된 노드들의 진입차수 -1
    for i in graph[now]:
      indegree[i]-=1

      if indegree[i]==0:
        q.append(i)

  for i in result:
    print(i,end=' ')

topology_sort()