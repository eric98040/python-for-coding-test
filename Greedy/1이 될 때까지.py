# ex3 : 1이 될 때까지



# < my solv >

n, k = map(int, input().split())
cnt = 0

# % 연산 특성상 n < k이면 n을 반환
while  n >=k :
  # 1을 뺀 횟수 + k로 나눈 횟수 = 1사이클 당 1을 최대한 빼고 k로 나눔
  cnt += (n%k) + 1
  # n을 재설정
  n //= k
  
# n < k 인 경우도 고려
else : 
  cnt += n-1
  
print(cnt)


# < solution1 >

n, k = map(int, input().split())
result = 0

# n이 k이상이라면 k로 계속 나누기
while n >=k :
  # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
  while n%k != 0 :
    n-=1
    result+=1
  # k로 나누기
  n //= k
  result +=1
  
# 마지막으로 남은 수에 대하여 1씩 빼기
while n>1 :
  n-=1
  result+=1

print(result)


# < solution2 >

n, k = map(int, input().split())
result = 0

while True :
  
  # n == k의 배수가 될 때까지 1씩 빼기
  target = (n//k)*k
  result += n-target
  n = target
  
  # n이 k보다 작을 때 반복문 탈출 (더 이상 나눌 수 없을 때)
  if n < k :
    break
  
  # k로 나누기
  result +=1
  n//=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n-1
print(result)
