# ex 1 : 떡볶이 떡 만들기


#  < My solv >

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = list(map(int, input().split()))

def sum_ricecake(array,x) :
  return sum([ i-x for i in array if i>x])

start, end = 0, max(array)-1

while start <= end :
  mid = start + (end-start)//2
  
  if sum_ricecake(array,mid) >= m :
    start = mid +1
    
  else :
    end = mid -1
  
print(end)



# < Solution >

  # 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 h를 반복해서 조정하면 됨
  # 현재 이 높이로 자르면 조건을 만족할 수 있는가? 를 확인한 후 조건의 만족 여부('예' 혹은 '아니오')에 따라 탐색범위를 좁혀서 해결할 수 있음
  # 절단기의 높이는 0부터 10억까지의 정수 중 하나 (이렇게 큰 탐색 범위를 보면 이진 탐색을 떠올려야 함)
  # 이러한 이진 탐색 과정을 반복하면 답을 도출할 수 있음
  
  # 중간점의 값은 시간이 지날수록 최적화된 값이 되기 때문에, 
  # 과정을 반복하면서 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 중간점의 값을 기록하면 됨


n,m = map(int, input().split()) # N : 떡의 개수, M : 요청한 떡의 길이

# 각 떡의 개별 높이 정보를 입력
array = list(map(int, stdin.readline().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0

while (start <= end) : 
  total = 0
  mid = (start + end) //2
  for i in array :
    # 잘랐을 때의 떡의 양 계산
    if i > mid : 
      total += (i - mid)
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < m :
    end = mid -1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else : 
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result를 기록 (ㅈㄴ중요!!!!)
    start = mid +1

# 정답 출력 : start == end == mid가 된 후 start가 end(mid-1)보다 커지는 순간 
print(result)
