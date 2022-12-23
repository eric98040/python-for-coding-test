# ex1 : 상하좌우


# < My solv >

import sys
input = sys.stdin.readline

n = int(input())
array = input().split()
# graph = [[0]*n for _ in range(n)] : 굳이 2차원 배열을 처음부터 만들 필요는 없었음

lst = ['R','L','D','U']

# 방향벡터 설정 (동,서,남,북)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 처음 출발점 (0,0) 설정
x ,y = 0,0

for i in array :
  k = lst.index(i)  # 해당 방향의 인덱스 번호 찾기
  
  nx = x + dx[k]
  ny = y + dy[k]
  
  if 0<= nx <=n-1 and 0<= ny<=n-1 :
    x,y = nx, ny
    
print(x+1,y+1)


# < Solution >

# n을 입력받기
n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동방향
move_types = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 이동 계획을 하나씩 확인
for plan in plans : 
  for i in range(len(move_types)) :
    if plan == move_types[i] : 
      nx = x + dx[i]
      ny = y + dy[i]
      
  # 공간을 벗어나는 경우 무시
  if nx<1 or ny<1 or nx >n or ny >n :
    continue
  
  # 이동 수행
  x, y = nx, ny
  
print(x,y)
