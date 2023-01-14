# ex1 : 1로 만들기


# < My solv >


import sys
input = sys.stdin.readline

n = int(input())
dp = [0]* (n+1)

for i in range(2,n+1) :
    dp[i] = dp[i-1]+1
    
    if i%5 ==0 :
        dp[i] = min(dp[i//5]+1 ,dp[i])
    if i%3 ==0 :
        dp[i] = min(dp[i//3]+1 ,dp[i])
    if i%2 ==0 :
        dp[i] = min(dp[i//2]+1 ,dp[i])
      
print(dp[n])
  
# < Solution > 


# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
