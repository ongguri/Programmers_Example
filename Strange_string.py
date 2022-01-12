'''
- 문제 설명

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.


- 제한 사항

    문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
    첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

'''


'''
# 공백이 하나일 경우에만 가능함

def solution(s):
    answer = ''
    string_li = []
    s_list = s.split()

    for n in s_list:
        for i in range(len(n)):
            if i % 2 == 0:
                answer += n[i].upper()
            else:
                answer += n[i].lower()

        string_li.append(answer)
        answer = ''

    return " ".join(string_li)
'''

# 공백이 여러개일 경우 가능한 코딩


def solution(s):

    answer = ''
    word = 0

    for i in range(len(s)):

        if s[i] == " ":
            answer += ' '
            word = 0
            continue

        if word % 2 == 0:
            answer += s[i].upper()
            word += 1
        else:
            answer += s[i].lower()
            word += 1

    return answer


print(solution('try  hello world'))

# 리스트에 "" 이거는 join 함수를 쓰게되면 공백으로 처리
