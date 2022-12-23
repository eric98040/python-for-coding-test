# ex2 : 숫자 카드 게임


# < my solv >

n,m = map(int, input().split())

# 2차원 배열안에 수를 저장 + 각 행마다 min 값을 찾아서 1차원 배열로 변환 + 그 후에 전체 min 값의 max 값을 구함
array = max([ min(list(map(int, input().split()))) for _ in range(n)])

print(array)



# < solution1 >


n,m = map(int, input().split())

result = 0
for i in range(n) : 
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result,min_value)
  
print(result) # 최종 답안 출력



# < solution2 >

import sys

n,m = map(int, input().split())

result = 0
for i in range(n) : 
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기  
  min_value = sys.maxsize
  for j in data :
    min_value = min(min_value,j)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(min_value,result)
  
print(result) # 최종 답안 출력
