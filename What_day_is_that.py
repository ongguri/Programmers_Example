
'''
- 문제 설명

2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

- 제한 조건

    2016년은 윤년입니다.
    2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
'''

# 처음 풀었을때

'''
month = 1
day = 1
yo = "금", "토", "일", "월", "화", "수", "목"
n = 0

mon = int(input("월 입력:"))
dayth = int(input("일 입력:"))

while True:

    if month == mon and day == dayth:
        print("%d월 %d일은 %s요일 입니다." % (mon, dayth, yo[n]))
        break

    day += 1

    if month in (1, 3, 5, 7, 8, 10, 12):
        if day == 32:

            month += 1
            day = 1

    elif month in (4, 6, 9, 11):
        if day == 31:

            month += 1
            day = 1

    elif month == 2:
        if day == 29:

            month += 1
            day = 1

    else:
        break

    if month != 13:
        n += 1
        if n == 7:
            n = 0
'''

# 두번째 풀었을때


def solution(a, b):

    day = 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'
    month = 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    return day[(sum(month[:a-1]) + b) % 7]


print(solution(5, 24))
