# ex 5 : 금광


# < My solv >

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
  n,m = map(int, input().split())
  array = list(map(int, input().split()))
  dp = []
  
  for i in range(0,len(array),m):
    dp.append(array[i:i+m])
    
  
    
  # 바로 dp 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍 적용 가능 : dp 테이블 갱신
  for column in range(1,m):
    for row in range(n) :
        
      if row == 0 :
          dp[row][column] = dp[row][column] + max(dp[row][column-1],dp[row+1][column-1])
        
      elif row == n-1 :
          dp[row][column] = dp[row][column] + max(dp[row][column-1],dp[row-1][column-1])
    
      else:
          dp[row][column] = dp[row][column] + max(dp[row][column-1],dp[row-1][column-1],dp[row+1][column-1])
      
  print(max([list(x) for x in zip(*dp)][-1]))
  
  
  
# < Solution >

  
for tc in range(int(input())) : 
    # 금광 정보 입력 
    n,m = map(int, input().split())
    array = list(map(int,input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    dp = []
    idx = 0
    for i in range(n) : 
        dp.append(array[idx:idx+m])
        idx += m
    # 다이나믹 프로그래밍 진행
    for j in range(1,m) : 
        for i in range(n) : 
            # 왼쪽 위에서 오는 경우
            if i ==0 :
                left_up = 0
            else : 
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1 : 
                left_down = 0
            else : 
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = max(left,left_down,left_up) + dp[i][j]
    result = 0
    for i in range(n) :
        result = max(result, dp[i][m-1])
    print(result)
