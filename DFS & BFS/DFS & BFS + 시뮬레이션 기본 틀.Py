
n,m = map(int, input().split())
# n : 세로길이, m : 가로길이
graph = [ list(map(int, input().split())) for _ in range(n)]
visited =[ [False]*m for _ in range(n)]


# DFS + 시뮬레이션 : 방문처리 1번 + append 사용 X

def DFS(x,y) : 
    
    if 0<=x<n and 0<=y<m and not visited[x][y] : 
        
        visited[x][y] = True
        
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        
        return True
    
    return False

cnt = 0
for i in range(m) : 
    for j in range(n) : 
        if DFS(i,j) :
            cnt+=1
            
            
            
# BFS + 시뮬레이션 : 방문처리 2번 + append 사용

dx = [0,0,1,-1]
dy = [1,-1,0,0]

from collections import deque

def BFS(a,b) :
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    
    while queue : 
        # x,y는 이미 queue에 들어있는 애 -> 다시 방문처리할 필요가 없음 (이미 append할 때 방문처리함)
        x,y = queue.popleft()
        
        # 1번 방법
        
        for i in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx<n and 0<=ny<m and not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx,ny))
                
        
        # 2번 방법
        
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            
            if 0<= nx<n and 0<=ny<m and not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx,ny))


cnt = 0
for i in range(m) : 
    for j in range(n) : 
        if not visited[i][j] :
            BFS(i,j)
            cnt+=1
