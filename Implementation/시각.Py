# ex2 : 시각


# < My solv >

import sys
input= sys.stdin.readline

n = int(input())
cnt = 0

for i in range(n+1)  :  # 범위를 n+1까지로 설정해야 'n시'까지로 고려됨
  for j in range(60) : 
    for k in range(60) :
      time = str(i)+str(j)+str(k)
      if '3' in time : 
        cnt+=1
        
print(cnt)


# < Solution >

import sys
input= sys.stdin.readline

# H를 입력받기
h = int(input())
count = 0

for i in range(h+1)  :  
  for j in range(60) : 
    for k in range(60) :
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in  str(i)+str(j)+str(k) :
        count+=1
        
print(count)
  
