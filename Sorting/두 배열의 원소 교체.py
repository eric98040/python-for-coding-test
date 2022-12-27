# ex 3 : 두 배열의 원소 교체


# < My solv >


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array_a = sorted(list(map(int, input().split)))
array_b = sorted(list(map(int, input().split)),reverse=True)

for i in range(k) : 
  if array_a[i] < array_b[i] :
    array_a[i], array_b[i] = array_b[i], array_a[i]
  
  else :
    break


# < Solution > 


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(revese=True)

for i in range(k) : 
    if a[i] < b[i] : 
        a[i], b[i] =  b[i], a[i]
    else :
        break
print(sum(a))

