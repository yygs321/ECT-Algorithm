def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,a)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

#모든 간선을 담을 리스트
edges=[]
#최종 비용을 담을 변수
result=0

for i in range(1,v+1):
  parent[i]=i

#모든 간선에 대한 정보 받기
for _ in range(e):
  a,b,cost=map(int,input().split())
  #비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost,a,b)) 

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
  cost,a,b=edge
  #사이클이 형성되지 않으면(두 간선의 루트노드가 같지 않으면)
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost

print(result)