# ex 3 : 바닥 공사


# < My solv >

import sys
input = sys.stdin.readline

# a_i : 가로가 i일 때 바닥을 채울 수 있는 경우의 수
# a_i = a_i-1 + 2*a_i-2

dp = [0]*1001
dp[1] = 1 ; dp[2] = 3
n = int(input())

for i in range(3,n+1):
  dp[i] = (2*dp[i-2] + dp[i-1]) % 796796

print(dp[n])
  
  
# < Solution >

# 정수 n을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 dp table 초기화
d = [0] * 1001

# 상향식 방법으로 dynamic programming 진행
d[1] = 1
d[2] = 3
for i in range(3,n+1) : 
  d[i] = (d[i-1]*2 + d[i-2]) % 796796
  
# 계산된 결과 출력
print(d[n])
