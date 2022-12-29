'''
 < 이진 탐색 >
 
 
  • 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
  • 이진 탐색 : '정렬되어' 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    • 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함
  • 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산횟수는 log_2 N에 비례
  
• 즉 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)이다.
• 이진 탐색의 결과 : 해당 target의 '인덱스' 번호 + 1 (실제 '몇' 번째에 위치하는지)
  


• while 조건에 equal 포함 형태 & start = mid + 1 & end = mid -1
  • 이 경우 무조건 end + 1 == start 이 됨 --> end와 start가 크로스됨
  • start를 출력하면 : 이후 경계의 first 원소
  • end를 출력하면 : 이전 경계의 last 원소
  
• 함수 설정해서 sum+=i//mid 이렇게 쓰지 말 것
• 그냥 for문으로 sum+=i//mid 이렇게 세팅
  
1. 특정값 찾기
  
    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      
      if arr[mid] < target :
          start = mid + 1
      elif:
          end = mid - 1
      else : 
          return arr[mid]

    return arr[start]
  
  # 이 경우 무조건 end + 1 == start 이 됨 
  # start를 출력하면 : 이후 경계의 first 원소
  # end를 출력하면 : 이전 경계의 last 원소
  
2. 최대값 찾기 : 
- end를 반환 (이전 경계의 max값) 
- start = mid + 1을 넣는 조건에 =(등호)추가!! : 최대값을 찾으려면 일단 range 자체가 증가해야 함

    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      
      if arr[mid] <= target :
          start = mid + 1
      else : 
          end = mid -1
        
    return arr[end]
    
3. 최소값 찾기 : 
- start를 반환 (이후 경계의 min값) 
- end = mid - 1을 넣는 조건에 =(등호)추가!! : 최소값을 찾으려면 일단 range 자체가 감소해야 함

    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      
      if arr[mid] < target :
          start = mid + 1
      else : 
          end = mid -1
        
    return arr[start]


'''
# ----------------------------< 재귀함수 >---------------------------

# 이진 탐색 소스코드 (재귀함수)
  # start, end 모두 '인덱스' 번호로서 처리
def binary_search(array,target,start,end) : 
    if start > end : 
        return None # 탐색하고자 하는 범위에 데이터가 존재하지 않으므로 None 반환
    # 찾은 경우 중간점 인덱스 반환
    mid = start + (end - start) // 2 # 몫으로 처리 -> 소수점 내림
    if array[mid] == target : 
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target : 
        return binary_search(array,target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target, mid+1 , end)
    

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기

n, target = map(int,input().split())

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력 

result = binary_search(array,target,0,n-1)
if result == None : 
    print('원소가 존재하지 않습니다.')
else : 
    print(result+1)

# ----------------------------< 반복함수 >---------------------------

# 이진 탐색 소스코드 (재귀함수)
  # start, end 모두 '인덱스' 번호로서 처리
def binary_search(array,target,start,end) : 
    while start < end : 
        # 찾은 경우 중간점 인덱스 반환
        mid = start + (end - start) // 2
        if array[mid] == target : 
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] < target : 
             start =  mid +1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else : 
            end = mid -1
    return None
        
            
    

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기

n, target = map(int,input().split())

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력 

result = binary_search(array,target,0,n-1)
if result == None : 
    print('원소가 존재하지 않습니다.')
else : 
    print(result+1)


