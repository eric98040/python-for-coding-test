'''

• <DFS> (Depth-First Search)
  • 깊이 우선 탐색 (그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘)
  • 스택 자료구조 or 재귀함수를 이용 (스택을 세로로 세운 일자형 바구니로 생각)
  
    • 탐색 시작 노드를 스택에 삽입하고 방문처리를 함 & 삽일할 때 그 노드를 print
    • 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드(1개)를 스택에 넣고 방문 처리함 
    • = 그 인접한 노드가 최상단 노드가 된 후 다시 기준이 되어 동일한 알고리즘을 재귀적으로 반복
    • 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    • 더 이상 2번의 과정을 수행할 수 없을 때까지 반복함
    
'''
    
def DFS(v) : 
  
  visited[v] = True
  
  for i in graph[v] : 
    if not visited[v] :     
      DFS(v)
    
    
# DFS 메서드 정의

def dfs(graph, v, visited) : 
  # 현재 노드를 방문처리 -> 그 노드의 번호를 출력
  visited[v] = True 
  print(v, end = ' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v] : 
    if not visited[i] : 
      dfs(graph, i , visited)
      
# def dfs(graph, v, visited) : 
#   visited[v]= True
#   print(v, end = ' ')
#   for i in graph[v] : 
#     if visited[i] == False : 
#       dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
  # 노드가 시작하는 번호가 1번부터가 많으므로 0번 인덱스는 비워두기
  
graph = [
  [],
  [2,3,8],  # 1번 노드와 연결된 것은 2,3,8번
  [1,7],# 2번 노드와 연결된 것은 1,7번
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트 초기화)
  # 0번 인덱스 값을 쓰지 않기 위해서 원래 n개의 노드 -> n+1개의 1차원 리스트
visited = [False] * 9 

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)     

    
  
    
    
'''
• <BFS> (Breadth-First Search)
  • 너비 우선 탐색 (그래프에서 가까운 노드부터 우선적으로 탐색)
  • 큐 자료구조를 이용 (큐를 세로로 세운 통, 터널이라고 생각)
  
  • 탐색 시작 노드를 큐에 삽입하고 방문처리 & 큐에서 방출될 때 그 노드를 print
  • 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드(여러 개)를 모두 큐에 삽입하고 방문처리
  • 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
  
  • 특정 조건에서의 최단 경로 문제해결에도 꽤나 쓰임
  
'''


from collections import deque

# BFS 메서드 정의
def bfs (graph, start, visited) : 
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue : 
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i] : 
                queue.append(i)
                visited[i] = True
                 
                
                
                
graph = [
  [],
  [2,3,8],  # 1번 노드와 연결된 것은 2,3,8번
  [1,7], # 2번 노드와 연결된 것은 1,7번
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트 초기화)
  # 0번 인덱스 값을 쓰지 않기 위해서 원래 n개의 노드 -> n+1개의 1차원 리스트
visited = [False] * 9 

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)  

  
  
