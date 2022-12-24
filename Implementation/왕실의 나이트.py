# ex 3 : 왕실의 나이트


# < My solv > 


import sys
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]


position = input()
x = int(position[1])
y = ord(position[0])-96
cnt = 0

for i in range(8) : 
  nx = x + dx[i]
  ny = y + dy[i]
  
  if 1<= nx <=8 and 1<= ny <=8 : 
    cnt+=1
    
print(cnt)


# < Solution >

import sys
input = sys.stdin.readline

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-ord('a'))+1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps : 
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[0]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if 1<= next_column<=8 and 1<= next_row <=8 :
    result+=1
    
print(result)
