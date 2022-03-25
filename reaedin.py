# 10줄의 입력을 받아 리스트로 저장하기
#N = list(input() for _ in range(3))
#print(N[1])
import sys
def my_function(x):
    x = x.replace("234", "98765apples")
    print(x)
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
my_function(data)