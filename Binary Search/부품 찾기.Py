# ex 2 : 부품 찾기


# < My solv >

import sys
input= sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split()))) # binary search를 쓰기 위해 정렬 필요

m = int(input())
check_numbers = list(map(int, input().split()))

def binary_search(array,target) :
  
  start, end = 0, len(array)-1
  
  
  while start <= end :
    mid = start + (end-start)//2  # mid값을 계속해서 갱신해야 하므로 while문 안으로 들어가야 함!!
    
    if array[mid] > target :
      end = mid -1
    elif array[mid] < target :
      start = mid +1
    else :
      return mid
    
  return None

for i in check_numbers : 
  if not binary_search(array,i) :
    print("no", end = ' ')
  else :
    print("yes", end = ' ')


# < My solv2 >

import sys
input= sys.stdin.readline
from bisect import bisect_left,bisect_right

n = int(input())
array = sorted(list(map(int, input().split()))) # binary search를 쓰기 위해 정렬 필요

m = int(input())
check_numbers = list(map(int, input().split()))

def count_by_range(array,x) :
  return bisect_right(array,x) - bisect_left(array,x)

for i in check_numbers :
  if count_by_range(array,i) ==0 :
    print("no", end = ' ')
  else :
    print("yes", end = ' ')


# < Solution1 > : 이진탐색


# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        

# < Solution2 > : 계수정렬


# N(가게의 부품 개수) 입력
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# < Solution3 > : 집합 자료형 이용

#  세트/딕셔너리는 삽입,제거,탐색,포함여부 확인 메소드가 O(1)이라 O(N)인 리스트보다 유리하다.
#  반면 리스트는 순서가 있거나 index로 요소에 접근할 필요가 있을 때 활용하면 좋다.

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 입력 받아서 집합(Set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
