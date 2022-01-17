#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적 호출
  if parent[x]!=x:  #x: 노드번호
    parent[x]= find_parent(parent, parent[x])
  return parent[x] #반환되는 값은 루트노드 번호
    
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a= find_parent(parent,a)
  b= find_parent(parent,b)
  #더 작은 값으로 합치기
  if a<b: 
    parent[b]=a
  else:
    parent[a]=b  

#노드, 간선의 개수
v,e=map(int,input().split())
parent=[0]*(v+1) #부모테이블 초기화
#부모테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
  parent[i]=i

#간선의 개수만큼 union연산(간선) 각각 수행
#같은 집합으로 합치기
for i in range(e):
  a,b=map(int,input().split())
  union_parent(parent,a,b)

  

#각 원소가 속한 집합 출력(가장 끝, 루트 노드 번호)
print("각 원소가 속한 집합: ",end=' ')
#각 원소만큼 돌면 되니까 (1,노드+1)
for i in range(1,v+1):
  print(find_parent(parent,i), end=' ')
print()

#부모 테이블 내용 출력 (바로 위, 부모 노드 번호)
print("부모 테이블: ", end=' ')
for i in range(1,v+1):
  print(parent[i], end=' ')