'''
- 문제 설명

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

- 제한사항
    s는 길이가 1 이상, 100이하인 스트링입니다.
'''


def solution(s):
    answer = ''

    mid = len(s) // 2

    if len(s) % 2 == 0:
        answer += s[mid - 1: mid + 1]
    else:
        answer += s[mid]
    return answer


print("가운대 글자를 출력해드립니다.")
word = input("> ")

print("가운대 글자:", solution(word))
