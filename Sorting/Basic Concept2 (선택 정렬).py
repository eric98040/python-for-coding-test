'''

• < 선택 정렬 > (selection sort)
  • 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꾸는 것을 반복
  • 남아있는 데이터 중 가장 작은 놈을 남아있는 놈들 중 가장 앞으로 보내기 (선형탐색)
  • 마지막 데이터는 처리하지 않아도 알아서 정렬됨
  • 전체 연산 횟수  = n + (n-1) + (n-2) + ....  = (n^2+n-2)/2 = O(N^2)
  
• 장점
  • 버블 정렬과 마찬가지로 알고리즘이 단순
  • 정렬을 위한 비교횟수는 많지만, 버블 정렬에 비해 실제 교환하는 횟수는 적기에 많은 교환이 일어나는 자료상태에서는 비교적 효율적
  • 버블 정렬과 마찬가지로 정렬하고자 하는 배열 안에서 교환하는 방식(제자리 정렬)이므로 다른 메모리 공간을 필요로 하지 않음

• 단점
  • 시간 복잡도가 O(N^2)이므로, 비효율적임
  • 불안정 정렬(Unstable Sort)임
'''  
  
  
array = [7,5,9,0,3,1,6,2,4,8]

# i : 처리하지 않은 데이터 중에서 최상단 index 번호
# j : min값의 인덱스 번호

for i in range(len(array)) : 
    min_index = i # 앞쪽 원소 = 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)) : 
      
      # min_index 보다 더 작은 j번째 수가 있다면 min_index를 array[j]로 박꾸기 
        if array[min_index] > array[j] : 
            min_index = j  # 가장 작은 수의 index를 j로 설정
            
    # 스와핑 with min_index & i번째 인덱스
    array[i], array[min_index] = array[min_index], array[i]

print(array) 



