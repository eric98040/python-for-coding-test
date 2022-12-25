# ex 2 : 미로 탈출


# < My solv >

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [ list(map(int,input().rstrip())) for _ in range(n)]

# 방향 벡터 설정
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def BFS(a,b) : 
    
    queue = deque()
    queue.append((a,b))
    # 1에서 시작하므로 방문처리 이미 선반영됨
    
    while queue : 
        x,y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
                
            # return None을 하면 반복문이 끝남 (early return) -> continue로 탈출
            if nx<0 or ny<0 or nx>=n or ny >= m : 
                continue
            
            if graph[nx][ny] == 0 :
                continue
            
            # 괴물이 없을 때 (1일 때)
            if graph[nx][ny] ==1 :
                
                graph[nx][ny]+=graph[x][y]
                queue.append((nx,ny))
       
    

BFS(0,0)
print(graph[n-1][m-1])
            
            

# < Solution >



from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
