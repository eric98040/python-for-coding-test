
# ex 4 : 게임 개발

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 세로 크기, m : 가로 크기
x,y,direction = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left() :
  global direction
  direction-=1
  if direction <0 :
    direction = 3
  
# 처음 시작 좌표를 방문처리
visited[x][y] =1

# 각 방향 시도 횟수
try_cnt = 0
    
while True :
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  try_cnt+=1
  
  # 방문하지 않았을 경우 & 바다가 아니면 : 방문처리 및 이동
  if not visited[nx][ny] and not graph[nx][ny]:
    visited[nx][ny] = 1
    x,y = nx, ny
    try_cnt =0
  
  if try_cnt ==4 :
    # 네 방향 모두 이미 가본 칸이거나, 바다로 되어 있을 경우 : 바라보는 방향을 유지한채로 한 칸 뒤로 간다
    nx = x - dx[direction]
    ny = y - dy[direction]
    try_cnt = 0
    
    # 바다일 경우
    if graph[nx][ny] :
      break
    else : 
      x,y = nx, ny
      
res = 0
for i in visited : 
  res += i.count(1)
  
print(res)
  



# < Solution >



# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력

print(count)
    
