'''


• 그래프 : 노드(Node) or 정점(Vertex) + 에지(Edge)로 구성된 집합
• 노드 : 데이터를 표현하는 단위 , 에지 : 노드를 연결함
• 연결 요소 : 에지로 연결된 노드의 집합
• 그래프를 구현하는 3가지 방법

import sys
input = sys.stdin.readline
print = sys.stdout.write

• 얕은 복사 : 세로값들이 전부 동시에 변경됨
• array_new의 [0],[1],...,[n-1]들이 각각 하나의 객체를 바라봄
array_new = [[0]*y]*x 



• z <- y <- x 방향으로 xyz

• 2차원 리스트 초기화
y,x,z = map(int, input().split())
array = [[0]*y for _ in range(x)]

원소 접근 : array[x][y]


• 3차원 리스트 초기화
array = [[[0]*z for _ in range(y)] for _ in range(x)]

원소 접근 : array[x][y][z]



       Z
       |
       |
       |
       |
       |
       | -----------------> Y
      /
     /
    /
   /
  /
 /
X
 
'''


'''


# 1. 에지 리스트 (edge list) : 노드 사이의 최단 거리를 구하는 벨만-포드 or 최소 신장 트리를 찾는 크루스칼 알고리즘에 사용 & 노드 중심 알고리즘에는 잘 사용 X

- 에지를 중심으로 그래프를 표현
- 방향이 있는 그래프는 순서에 맞게 노드를 리스트에 저장하는 식으로 표현!
1. 에지 리스트는 출발 노드, 도착 노드를 저장하여 가중치가 없는 에지를 표현 : 열2개면 충분
- [[출발 노드1, 도착노드1], [출발노드1, 도착노드2], [출발노드2, 도착노드1], ...] 이렇게 표현

2. 출발 노드, 도착 노드, 가중치를 저장하여 가중치가 있는 에지를 표현 : 열 3개면 충분
- [[출발 노드1, 도착노드1, 가중치], [출발노드1, 도착노드2, 가중치], [출발노드2, 도착노드1, 가중치], ...] 이렇게 표현





# 2. 인접 행렬 (adjacency matrix) : 2차원 리스트를 자료구조로 이용하여 그래프를 표현 / 노드 중심으로 그래프를 표현 

1. 인접 행렬로 가중치 없는 그래프 표현하기
- 행 index : 출발 노드, 열 index : 도착 노드
- array[출발 노드][도착 노드] = 1 (가중치가 없으므로)

2. 인접 행렬로 가중치 있는 그래프 표현하기
- 행 index : 출발 노드, 열 index : 도착 노드
- array[출발 노드][도착 노드] = 가중치

3. 연결이 되어 있지 않은 노드끼리는 infinity(INF)의 비용이라고 작성함

장점 : 두 노드를 연결하는 에지의 여부와 가중치 값은 리스트에 직접 접근하면 바로 확인할 수 있는 것
단점 : 노드와 관련되어 있는 에지를 탐색하려면 N번 접근해야 하므로 시간 복잡도가 인접 리스트에 비해 느리고, 노드 개수에 비해 에지가 적을 때는 공간 효율성이 떨어짐





# 3. 인접 리스트 (adjacency list) : 파이썬의 리스트를 이용하여 그래프를 표현 
- 노드 개수만큼 리스트를 선언
- 리스트의 Input data 형태는 문제의 조건에 맞게 설정
- 2차원 리스트 안의 각 리스트 번호(index) : 출발 노드 / 그 리스트 안의 원소들 (value) : 도착 노드 or (도착 노드, 가중치)
- 방향이 없는 그래프면 양쪽 방향으로 모두 저장, 방향이 있는 그래프면 한 쪽 방향으로만 저장

1. 인접 리스트로 가중치 없는 그래프 표현하기 : 출발 노드의 원소들 = input data는 1개 (int)
- array = [ [] for _ in range(n+1) ] : 1,2,..,i,..,n번 인덱스(array[i])가 연결되어 있는 노드들을 모두 리스트에 append

2. 인접 리스트로 가중치 있는 그래프 표현하기 : 출발 노드의 원소들 = input data 2개 (도착 노드, 가중치)
- array = [ [] for _ in range(n+1) ] : 1,2,..,i,..,n번 인덱스(array[i])가 연결되어 있는 노드들 & 가중치까지 모두 리스트에 append

장점 : 노드와 연결된 에지를 탐색하는 시간은 매우 뛰어남 / 노드 개수가 커도 공간 효율이 좋아 메모리 초과 에러도 발생하지 않음 -> 실제 코테에서도 이를 선호
단점 : 그래프 구현이 꽤나 복잡함  / 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림





- 방향이 없는 그래프에 'index 번호를 이용한' 인접 리스트 만들기
• graph[i].append(array[i])
• graph[array[i]].append(i)

- 방향이 없는 그래프에 인접 리스트 만들기
• a,b = map(int, input().split())
• graph[a].append(b)
• graph[b].append(a)


- 새로운 check_variable 만들기
• arrive 변수, iseven 변수 등 True / False 값으로 설정

- 기존의 visited list를 업데이트
• visited = [-1]*(n+1)
• visited[i] = visited[node] + 1

- graph, visited 를 제외한 새로운 check list 만들기
• 부모 노드 저장 리스트, 특정 조건 체크 리스트 등

• check = [0] * (n+1)
• check [i]+=1 : 하나씩 누적해서 더하기
• check[i] = (check[v]+1)%2 : check list에 기록시 0이면 1, 1이면 0으로 처리해주는 tool





'''

