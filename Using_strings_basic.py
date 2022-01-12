'''
- 문제 설명

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.


- 제한 사항

    s는 길이 1 이상, 길이 8 이하인 문자열입니다.

'''
# isdecimal() 함수를 이용한 방법


def solution(s):

    if len(s) == 4 or len(s) == 6:
        answer = s.isdecimal()
    else:
        answer = False
    return answer


'''
# 예외처리를 이용한 방법

def solution(s):

    try:
        int(s)
        if len(s) == 4 or len(s) == 6:
            return True

        else:
            return False

    except:
        return False


'''
s = '123a'

print(solution(s))
