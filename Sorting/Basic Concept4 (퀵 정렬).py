'''

•  < 퀵 정렬 >
  • 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
  • 일반적인 상황에서 가장 많이 사용하는 정렬 알고리즘 중 하나
  • 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘


• 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(pivot)으로 설정함
  • ----> 큰 값 찾기 & 작은 값 찾기 <-------  : 그 후 서로 위치를 바꾸기
  • 바꾼 원소 다음부터 화살표 시작점
  • 만약 -> 와 <- 가 엇갈린다면 : pivot과 '작은' 값의 위치를 서로 바꾸기
  •  (small_list) (pivot) (big_list) : 와 같은 형태가 나옴 & 재귀함수로 구현
  
• 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)를 기대할 수 있음
  • 너비 X 높이 = N x logN = NlogN 
  • (1줄 안에서 일어나는 연산 : N번) & (총 줄의 개수 = logN)
  
• 최악의 경우 o(N^2)의 시간 복잡도를 가질 수 있음 (N x N)
• 표준 정렬 라이브러리의 경우 : 최악의 경우에도 O(NlogN)을 보장

  
'''


def quick_sort(array, start, end) : 
    if start >= end : # 원소가 1개인 경우 종료
        return
    
    # start, end, pivot, left, right 전부 다 '인덱스' 번호로 인식
    
    pivot = start # 첫 번째 원소를 기준 pivot으로 설정
    left = start +1 # 두 번째 원소부터 small_lst 설정
    right = end
    while (left <= right) : # left : ---> , right : <---
        while (left<= end and array[pivot] >= array[left]) : 
          # pivot 보다 큰 값을 찾을 때까지 --> 오른쪽으로 탐색
            left +=1
        while (array[pivot] <= array[right] and right > start) : 
          # pivot보다 작은 값을 찾을 때까지 <--- 왼쪽으로 탐색
            right-=1
        # 두 개의 화살표가 겹칠 경우 : 겹치는 2개의 원소 중 작은 값을 pivot과 스와프
        if (left > right) : 
            array[right], array[pivot] =  array[pivot], array[right]
        # 두 개의 화살표가 겹치지 않을 경우 : 2개의 원소끼리 스와프
        else : 
            array[left], array[right] = array[right], array[left]
    
    # while문이 끝나고(첫 번재 loop 구별이 완료됨) 전체 재귀함수를 실행
    
     # right의 인덱스 자리에 pivot이 옴 : (start ~ pivot-1) & (pivot+1 ~ end)로 재귀실행
    quick_sort(array, start,right-1)
    quick_sort(array, right+1, end)

array = [5,7,9,0,3,1,6,2,4,8]

quick_sort(array,0,len(array)-1) 
# start, end 전부 인덱스 값으로 정의되므로 0, len(array)-1 로 실행
print(array)


# ---------------------------<파이썬 친화적 형식>-------------------------


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array) : 
  # array가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1 : 
    return array
  pivot = array[0] # pivot은 첫 번째 원소
  tail = array[1:] # tail은 피벗을 제외한 리스트
  
  left_side = [x for x in tail if x<=pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x>pivot] # 분할된오른쪽 부분
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
  # list 더하기이므로 pivot을 그냥 더하는 것이 아닌 []로 처리 : [pivot]
print(quick_sort(array))
  


  
