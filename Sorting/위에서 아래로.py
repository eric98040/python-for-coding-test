# ex 1 : 위에서 아래로


# < My solv >

import sys
input = sys.stdin.readline
n = int(input())
array = sorted([ int(input()) for _ in range(n)],reverse=True)
print(*array)


# < Solution >

n = int(input())
array = []
for i in range(n) :
  array.append(int(input()))
  
array = sorted(array, reverse=True)

for i in array :
  print(i, end = ' ')
