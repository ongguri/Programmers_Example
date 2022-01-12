'''
- 문제 설명 -
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

- 제한 조건
    시험은 최대 10,000 문제로 구성되어있습니다.
    문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
    가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요
'''

# 처음 풀었을때

'''
import random as r


def solution():

    num = 1
    number = []

    while num <= 10:

        how = r.randint(1, 5)

        number.append(how)
        num += 1

    
    return number



def p_cort(cort, num):
    
    count = 0

    for n in range(len(num)):

        if cort[n] == num[n]:
            count += 1
    
    return count


correct_num = solution().copy()
student1 = solution().copy()
student2 = solution().copy()
student3 = solution().copy()

print("문제  정답:",correct_num)
print("학생1 답안:",student1)
print("학생2 답안:",student2)
print("학생3 답안:",student3)

print("학생1이 맞춘 갯수:",p_cort(correct_num, student1))
print("학생2이 맞춘 갯수:",p_cort(correct_num, student2))
print("학생3이 맞춘 갯수:",p_cort(correct_num, student3))



if p_cort(correct_num, student1) < p_cort(correct_num, student2):

    if p_cort(correct_num, student2) < p_cort(correct_num, student3):

        print("학생3이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student3))

    elif p_cort(correct_num, student2) > p_cort(correct_num, student3):
        print("학생2가 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student2))

    else:
        print("학생2와 3이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student2))


elif p_cort(correct_num, student1) > p_cort(correct_num, student2):
    if p_cort(correct_num, student1) < p_cort(correct_num, student3):
        print("학생3이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student3))

    elif p_cort(correct_num, student1) > p_cort(correct_num, student3):
        print("학생1이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student1))

    else:
        print("학생1과 학생3이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student1))


elif p_cort(correct_num, student1) == p_cort(correct_num, student1):
    if p_cort(correct_num, student1) < p_cort(correct_num, student3):
        print("학생3이 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student3))
        print("학생1, 2는 %d개로 같은 갯수를 맞췄습니다." % (p_cort(correct_num, student1)))

    elif p_cort(correct_num, student1) > p_cort(correct_num, student3):
        print("학생1, 2가 %d개로 가장 많이 맞췄습니다." % p_cort(correct_num, student1))

    else:
        print("학생 모두가 %d개로 같은 갯수를 맞췄습니다." % p_cort(correct_num, student1))
'''

# 두번째 풀었을때

'''
def solution(answers):

    idx = 0

    a = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    while True:
        num = 0
        count = 0

        for i in answers:

            if i == a[idx][num]:
                count += 1
                num += 1
            else:
                num += 1

                if num == len(a[idx]):
                    num = 0
        a[idx] = count
        idx += 1

        if idx == 3:

            return [j+1 for j in range(len(a)) if a[j] == max(a)]

'''


def solution(answers):

    a = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for j in range(len(a)):

        num = 0
        count = 0

        for i in answers:

            if num == len(a[j]):
                num = 0

            if i == a[j][num]:
                count += 1
                num += 1
            else:
                num += 1

        a[j] = count
    print(a)

    return [j+1 for j in range(len(a)) if a[j] == max(a)]


print(solution([1, 2, 3, 4, 5, 2, 4]))
