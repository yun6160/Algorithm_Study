import sys
sys.stdin = open('input.txt', 'r')
# 한 줄을 읽어서 정수로 변환
# N = int(input())
# print(N)
# 한 줄을 읽고 공백으로 구분된 문자를 배열로 
# print(input().split())
# 한 줄을 읽고 공백으로 구분된 문자를 정수로 변환한 배열
# print(list(map(int, input().split())))
# N행으로 이루어진 2차원 배열 입력
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
while True:
    A = int(input())
    arr = []
    if A != -1:
        num = 1
        while num < A:
            if A%num == 0:
                arr.append(num)
            num+=1
        if sum(arr) == A:
            text = ' + '.join(map(str, arr))
            print(f"{A} = {text}")
        else:
            print(f"{A} is NOT perfect.")
    else:
        break

        
