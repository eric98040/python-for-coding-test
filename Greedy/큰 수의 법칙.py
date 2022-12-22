# ex2 : 큰 수의 법칙


# < my solv >

# m : 숫자가 더해지는 횟수 , k : 동일 숫자가 초과할 수 없는 횟수
n,m,k = map(int, input().split())
array = sorted(list(map(int, input().split())), reverse = True)
res = 0

# (가장 큰 값은 k번 & 그 다음 큰 값은 1번) 세트를 계속해서 주기적으로 더함
res += array[0]*(m//(k+1))*k 
res += array[1]*(m//(k+1))
m %= k+1
# 마지막에 m이 0이 아닐 경우 : 남은 가장 큰 값을 추가로 더해주면 됨
res+=array[0]*m

print(res)


# < solution1 >

n ,m , k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]
result = 0

while True : 
  for i in range(k) : # 가장 큰 수를 K번 더하기
    if m == 0 : # m이 0이라면 for 반복문 탈출
      break
    result += first
    m-=1 # 더할 때마다 1씩 빼기
  if m ==0  : # m이 0이라면 while 반복문 탈출
    break
  result += second  # 두 번째로 큰 수를 한 번 더하기
  m-=1 # 더할 때마다 1씩 빼기

print(result)

# < solution2 >

n ,m , k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 '횟수'를 계산
count = m//(k+1) *k
count += m%(k+1)
  
result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)

