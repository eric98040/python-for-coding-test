'''
• <재귀함수> : Recursive Function
  • 자기자신을 다시 호출하는 함수
  • 재귀함수를 문제 풀이에서 사용할 경우 재귀 함수의 종료 조건을 명시해야 함
  • 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
  • 발산 구조 : 초기값 세팅(n=0,1등) + 재귀표현 사용
  • 수렴 구조 : 최종값 세팅(a가 b로 나누어질 때) + 재귀표현 사용
  
  • 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있음
  • 모든 재귀함수는 반복문을 활용하여 동일한 기능을 구현할 수 있음
  • 재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있음
  • 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
  • 따라서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많음
  

• return이 없는 함수 (print로 바로 출력) : 함수만 호출하면 바로 출력
• reuturn이 있는 함수 (print를 따로 써줘야함): return값을 받는 변수를 생성 -> 그 변수를 print해서 함수 호출 



• 함수의 return with 재귀함수
  
  • return문이 없으면 자동으로 return None을 하게 된다.
  • 보시다시피 리턴문이 없으면 함수는 제일 마지막 줄에서 끝이 나게 됩니다. 
  • 리턴문으로 인해 해당 함수를 실행한 결과를 반환하고 함수 실행이 종료 되는데, 
  • 리턴문이 없으면 결과를 반환하지 못한 채 함수가 종료되기 때문에 해당 함수는 아무것도 없는 빈 값인 None이 찍히게 되는 겁니다.


• return None을 사용해야 할 때
    • ~가 아닌경우이다. 예를들어 다음과 같은 경우이다.
    • 목적으로 하는 대상이 아닌경우에는 명시적으로 None값을 리턴해줘야 한다.
    
• return을 사용할때
    • early return의 경우 많이 사용한다.
    • 맥락 상 break와 유사한 효과를 내기 때문에, 무언가를 리턴하기 보다는 실행 중단의 의미가 더 크다.
    
• return을 사용하지 않을 때
    • 함수가 무언가를 반환하는게 목적이 아닌, 단순 연산의 목적일 경우이다.
    • 연산이 끝난 후 연산 성공이나 실패를 반환해야 한다면 달라지겠지만, 그게 아니라 단순히 글로벌 변수 연산이 목적이라면, 사용하지 않는 경우가 있다.


• def dfs():

	 if 재귀 종료 조건:
    		 return cnt
            
     dfs()


            return None
               /      \
        return None  return None   
            /           \
         재귀 종료       재귀 종료
       return cnt    return cnt



• def dfs():

	if 재귀 종료 조건:
    		return cnt
            
    return dfs() -> 이렇게 해줘야 된다.
    
    
              return cnt
               /      \
        return cnt  return cnt  
            /           \
         재귀 종료       재귀 종료
       return cnt    return cnt
       
       
위에 있는 노드들도 dfs()를 반환 -> 그 dfs()가 cnt를 반환 : 결국 위에 있는 노드들은 cnt를 반환

'''
# 팩토리얼 구현 예제

# 반복적으로 구현한 n!
def factorial_iterative(n) : 
    result =1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1) :
        result*=i
    return result

# 재귀적으로 구현한 n! 

def factorial_recursive(n) : 
    # n이 1이하인 경우 1을 반환
    if n <=1 : 
        return 1
    # n! = n * (n-1)!을 그대로 코드로 작성하기
    else : 
        return factorial_recursive(n-1) * n
    
# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))


# 유클리드 호제법 (최대공약수 계산)
  # 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
  # 두 자연수 a,b에 대하여 (a>b) a를 b로 나눈 나머지를 r이라 하자
  # 이때 gcd(a,b) = gcd(b,r) --> 결국 a가 b로 나누어질 때가지 무한히 시행하는 것
  # 유클리드 호제법의 아이디어를 그대로 재귀함수 작성 가능
  

def gcd(a,b) : 
    # a,b의 순서가 바뀌어도 괜찮음 -> 순서에 상관없이 넣어주면 정상 작동
    if a%b ==0 :
        return b
    else : 
        return gcd(b,a%b)
print(gcd(192,162))


    
