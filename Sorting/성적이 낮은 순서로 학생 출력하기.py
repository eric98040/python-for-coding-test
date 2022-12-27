# ex 2 : 성적이 낮은 순서로 학생 출력하기


# < My solv >

import sys
input = sys.stdin.readline

n = int(input())
array = [ list(input().rstrip().split()) for _ in range(n)]

for i in array :
    i[1] = int(i[1])

array = sorted(array, key = lambda x :x[1])
for i in array :
    print(i[0], end = ' ')

    


# < Solution >

# n을 입력받기
n= int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n) : 
  input_data = input().split()
  # 이름은 문자열 그래도, 점수는 int으로 변환하여 저장
  array.append((input_data[0],int(input_data[1])))
  
# key를 이용하여 점수를 기준으로 정렬

array = sorted(array, key = lambda student : student[1])

# 정렬이 수행된 결과를 출력
for student in array :
  print(student[0], end = ' ')
