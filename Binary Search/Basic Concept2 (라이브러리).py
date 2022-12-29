'''
• < 이진 탐색 라이브러리 >  : bisect 라이브러리에서 import를 해야함
  • 정렬된 데이터 속 값이 특정 범위 / 특정 값에 속하는 데이터 개수 구하기
  • bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
  • bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
  
• 파라메트릭 서치 (Parametric Search)
  • 파라메트릭 서치 : 최적화 문제를 결정 문제 ('예' 혹은 '아니오')로 바꾸어 해결하는 기법
  • 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
  • 일반적으로 코딩 테스트에서 파랄메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음 

'''
# ex 1
from bisect import bisect_left, bisect_right


array = [1,2,3,4,4,8]
x = 4

print(bisect_right(array,x))
print(bisect_left(array,x))

# ex 2 : 특정 범위에 속하는 데이터의 개수 구하기

from bisect import bisect_left, bisect_right

# 같이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value) :
    left_index = bisect_left(a,left_value)
    right_index = bisect_right(a,right_value)
    
    return right_index- left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))    
    
