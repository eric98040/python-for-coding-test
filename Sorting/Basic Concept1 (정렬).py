# < 정렬 >
  # 데이터를 특정한 기준에 따라 순서대로 나열하는 것
  # 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용됨
  
  # 안정 정렬 : 동일한 값에 기존 순서가 유지 (버블, 삽입)
  # 불안정 정렬 : 동일한 값에 기존 순서가 유지X (선택, 퀵)
  
# 네 가지 정렬 알고리즘의 비교
  # 대부분의 프로그래밍 언어에서 제공하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계됨
  # 선택 정렬 / 평균 시간 복잡도 O(N^2) / 공간복잡도 O(N) / 아이디어가 매우 간단함
  # 선택 정렬 / 평균 시간 복잡도 O(N^2) / 공간복잡도 O(N) / 데이터가 거의 정렬되어 있을 때 가장 빠름
  # 퀵 정렬 / 평균 시간 복잡도 O(NlogN) / 공간복잡도 O(N) / 대부분의 경우에 가장 적합, 충분히 빠름
  # 선택 정렬 / 평균 시간 복잡도 O(N+K) / 공간복잡도 O(N+k) / 데이터의 크기가 한정되어 있는 경우에만 사용가능하지만 매우 빠르게 동작
  
  
  
# 버블 정렬 (오른쪽 끝에서부터 큰 원소로 정렬)
  # 연속한 2개의 인덱스끼리 비교하여 교환하는 방식
  # 가장 큰 원소가 오른쪽 끝까지 '버블'로 이동하기 때문에 버블정렬임
  # 셋 중에 제일 느리지만 단순함 (한 loop 안에서 모든 원소마다 swap을 해야함)
  
# 선택 정렬 (왼쪽 끝에서부터 작은 원소로 정렬)
  # 최솟값을 찾아서 맨 앞으로 이동하는 방식
  # 버블 정렬보다 좋음 (하나의 loop안에서 한번만 swap) :
  # 일반적으로 버블 정렬보다 2배 빠름
  
  
# 삽입 정렬 (왼쪽으로 원소 하나씩 이동하면서 비교)
  # 앞에서부터 차례대로 이미 정렬된 부분과 비교하여 교환하는 방식 
  # 필요한 부분까지만 탐색하므로 전부 탐색하는 선택배열에 비해 더 빠름
  # 셋 중에 제일 빠르지만 배열이 길어질수록 효율성이 떨어짐 
  # swap을 하는데, 모든 인덱스에 대해 실행하는 것이 아니라 '자신의 위치'를 찾기만 하면 ok
  
# 모두 시간 복잡도는 O(n²)
# 선택 정렬과 삽입 정렬은 사용할 메모리가 제한적인 경우에 사용하면 좋음

# 삽입 정렬 vs 선택 정렬
  # 삽입 정렬 : 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여 자신의 위치를 찾아 삽입
  # 선택 정렬 : 배열에서 해당 자리를 이미 선택하고 그 자리에 오는 값을 찾는 것
  

# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

from random import randint
import time

array = []
# 배열에 10,000개의 정수를 삽입
for _ in range(10000) : 
  # 1부터 100 사이의 랜덤한 정수
  array.append(randint(1,100))
  
# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)) : 
  min_index = i
  for j in range(i+1,len(array)) :
    if array[min_index] > array[j] : 
      min_index = j
  array[i], array[min_index] =  array[min_index], array[i]
  
# 측정 종료
end_time = time.time()
print('선택 정렬 성능 측정:', end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화

array = []
for _ in range(10000) : 
  array.append(randint(1,100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()
array.sort()
# 측정 종료
end_time = time.time()

print('기본 정렬 라이브러리 성능 측정:', end_time-start_time)
