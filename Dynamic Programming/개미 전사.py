# ex 2 : 개미 전사


# < My solv >

import sys
input = sys.stdin.readline

n = int(input())
array = [0]+list(map(int, input().split()))

dp = [0]*(n+1)
# dp[i] : i번째 식량창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)

dp[1] = array[1] ; 
dp[2] = max(array[1],array[2])  # array[2]가 아니라 앞의 두 항 사이의 max값

for i in range(3,n+1):
  dp[i] = max( dp[i-2]+array[i], dp[i-1])

print(dp[n])


# < Solution >

'''

• a_i = i번째 식량창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)
  • 다이나믹 프로그래밍의 조건 : 
    • 최적 부분 구조 (optimal substructure)
      • 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
    • 중복되는 부분 문제 (overlapping subproblem)
      • 동일한 작은 문제를 반복적으로 해결해야 함
  • i번째 식량창고까지의 경우의 수 = max( (i-1)번째 식량창고를 털었을 때 , (i-2)번째 식량창고를 털었을 때 + i번째 식량수)
    • i-3번째 부터는 i-1번째 (i-3을 털었을 경우) & i-2번째 (i-3을 털지 않았을 경우)에 포함되어 있음
    
  • a_i = max(a_i-1 , a_i-2 + k_i)
    • k_i = i번째 식량창고에 있는 식량의 양
    
'''

n = int(input())
array = list(map(int, input().split()))

# 앞선 계산을 저장하기 위해 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 (Dynamic Programming) 진행 : 보텀업 방식
d[0] = array[0]
d[1] = max(array[1], array[0])
for i in range(2,n) : 
    d[i] = max( d[i-1], d[i-2]+ array[i])

# 계산된 결과 출력
print(d[n-1])
