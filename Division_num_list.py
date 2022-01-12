'''
- 문제 설명

array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.


- 제한사항

    arr은 자연수를 담은 배열입니다.
    정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
    divisor는 자연수입니다.
    array는 길이 1 이상인 배열입니다.
'''

# 내가 푼 문제
'''
def solution(arr, divisor):
    answer = []

    for n in arr:
        if n % divisor == 0:
            answer.append(n)

    if answer == []:
        answer.append(-1)

    answer.sort()

    return answer


li = []

print("*** 배열 추가하기 ***")

while True:

    inp = int(input("> "))

    if inp == -1:
        break

    li.append(inp)

print("*** 나눌 수 입력 ***")
div = int(input("> "))

print("나눠지는 수:", solution(li, div))
'''


# 함수 길이 줄이는 방식

def solution(arr, divisor):

    # for문을 돌려 i를 반환하되 i % divisor == 0 일 경우에만.
    arr = sorted([i for i in arr if i % divisor == 0])
    # 만약 arr 의 길이가 0이 아니라면 그대로 반환, 0이면 리스트 [-1]를 반환
    return arr if len(arr) != 0 else [-1]


li = []

print("*** 배열 추가하기 ***")

while True:

    inp = int(input("> "))

    if inp == -1:
        break

    li.append(inp)

print("*** 나눌 수 입력 ***")
div = int(input("> "))

print("나눠지는 수:", solution(li, div))
