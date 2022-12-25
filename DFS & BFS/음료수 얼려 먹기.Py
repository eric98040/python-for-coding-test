# ex 1 : 음료수 얼려 먹기


# < My solv >


import sys
input = sys.stdin.readline

# 세로 길이 : n, 가로 길이 : m
n, m = map(int, input().split())
graph = [ list(map(int, input().rstrip())) for _ in range(n)]


def DFS(x,y) :
    
    # 주어진 범위를 넘어갈 경우 예외처리
    if x<0 or y<0 or x>=n or y>=m : 
        return False
    
    if graph[x][y] == 1 :
        return False
    
    # 0일 경우(구멍일 경우) 방문처리
    else :
        graph[x][y] = 1    
        DFS(x,y+1)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x-1,y)

        return True
        

cnt = 0

for i in range(n) : 
    for j in range(m) : 
        if DFS(i,j) :
            cnt+=1
            
print(cnt)


# < Solution >


# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y) :
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x>=n or y<=-1 or y>= m : 
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드 방문처리
        graph[x][y] =1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        # 0 only 블록의 최초 조사 지점 = True 반환 후 모든 블록들을 전부 1로 반환
        return True
    
    return False

# n,m을 공백을 기준으로 구분하여 입력받기
n, m = map(int,input().split())
 
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m) : 
        # 현재 위치에서 DFS 수행 : 방문처리가 됐다면(True) +1로 처리
        if dfs(i,j) :
            result+=1

print(result)
