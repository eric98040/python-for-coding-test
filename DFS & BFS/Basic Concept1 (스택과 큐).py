# <DFS & BFS> 그래프 탐색 알고리즘
  # 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
  # 대표적인 그래프 탐색 알고리즘 : DFS & BFS
  # 코테에서 매우 자주 등장하는 유형
  
# 스택 (first-in, last-out = FILO)
  # 먼저 들어 온 데이터가 나중에 나가는 형식 (선입후출, 박스 쌓아올리기)
  # 입구와 출구가 동일한 형태 
  # ㄷ자 형태 <--- in, ---> out
  # 구현은 list 자료형으로 가능 (append,pop 함수 O(1)시간 복잡도)
  
  
# 삽입(5) - 삽입(2)  - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()  
 
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() 
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # stack의 최상단 원소부터 쭉 출력
print(stack) # stack의 최하단 원소부터 쭉 출력


# 큐 (first-in, first-out = FIFO)
  # 먼저 들어온 데이터가 먼저 나가는 형식 (선입선출)의 자료구조
  # 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 : (일종의 대기줄)
  # out <----------- in
  
from collections import deque


queue = deque()
# 원소 삽입 : append (list와 동일)
# 원소 삭제 : popleft (가장 왼쪽의 원소를 삭제)

# 삽입(5) - 삽입(2)  - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제() 
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue)


# Deque methods 정리 <list method에 존재여부>

  # q.append(item) : 오른쪽 끝에 삽입 <O>
  # q.appendleft(item) : 왼쪽 끝에 삽입 <X>
  # q.pop() : 가장 오른쪽으 요소 반환 및 삭제 <O>
  # q.popleft() : 가장 왼쪽의 요소 반환 및 삭제 <X>
  # q.extend(array) : 주어진 array를 q의 오른쪽에 추가 <O>
  # q.extendleft(array) : 주어진 array를 q의 왼쪽에 추가 <X>
  # q.remove(item) : 해당 item을 q에서 찾아 삭제 <O>
  # q.rotate(숫자) : 해당 숫자만큼 회전 (양수:->, 음수:<-) <X>

  
