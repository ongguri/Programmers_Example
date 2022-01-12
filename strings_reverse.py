'''
- 문제 설명

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.


- 제한 사항

    str은 길이 1 이상인 문자열입니다.

'''

'''
def solution(s):
    answer = ''
    word = []
    for n in s:
        word.append(n)

        word.sort(reverse=True)

    for n in word:
        answer += n
    return answer


print(solution("AZbcdgfe"))
'''

'''
def solution(s):
    s = list(s)  # 바로 리스트에 담기
    s.sort(reverse = True)

    answer = ''
    for n in s:
        answer += n

    return answer

'''


def solution(s):

    return ''.join(sorted(s, reverse=True))


print(solution("AZbcdgfe"))
