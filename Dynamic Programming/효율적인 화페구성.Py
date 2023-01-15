# ex 4 : 효율적인 화폐 구성


# < My solv >

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = [ int(input()) for _ in range(n)]

# a_i = i원을 만들 수 있는 최소한의 화폐 개수
# k = 화폐의 단위
# a_i = min(a_i, a_i-k +1) : i-k원이 존재한다면

INF = 1e9
dp = [INF]*(m+1)
dp[0] = 0

for i in array :
  # 각 화폐단위에서 search -> dp 테이블을 다 돌면서 찾기
  for j in range(i,m+1) :
    if dp[j-i] != INF :
      dp[j] = min(dp[j],dp[j-i]+1) 
    
print(dp[m]) if dp[m] != INF else print(-1)

  
# < Solution >

  # a_i = 금액 i를 만들 수 있는 최소한의 화폐 개수
  # k = 각 화폐의 단위
  # 점화식 = 각 화폐 단위인 k를 하나씩 확인하여
    # a_i-k를 만드는 방법이 존재하는 경우 (i-k원) : a_i = min(a_i,a_i-k + 1)
    # a_i-k를 만드는 방법이 존재하지 않는 경우 :a_i = INF (임의의 무한대값)
  
  # 이중 for문을 사용해도 N*M으로 시간초과 판정이 나지 않음

  # 0단계
    # 각 인덱스에 해당하는 값으로 INF(무한)의 값을 설정
    # INF = 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않음 = 해당 화폐를 만들 수 x
    # 본 문제에서는 10,001을 사용할 수 있음 (1로 10000개를 사용 -> 10,000이 max)

  # 1단계
    # 첫 번째 화폐단위인 2를 확인
    # 점화식에 따라서 리스트를 갱신 : 인덱스 0인 숫자 0에서 시작 -> 인덱스 2에 값 1을 갱신
  # 2단계
    # 두 번째 화폐단위인 3을 확인
    # 점화식에 따라서 리스트를 갱신 
  # 3단계
    # 세 번째 화폐단위인 5를 확인
    # 점화식에 따라서 최종적으로 리스트를 갱신 
    
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
