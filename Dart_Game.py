def solution(dartResult):

    total = []
    i = ''
    score = 0

    for n in dartResult:

        if n == 'S':

            score = int(i)
            total.append(pow(score, 1))
            i = ''

        elif n == 'D':

            score = int(i)
            total.append(pow(score, 2))
            i = ''

        elif n == 'T':

            score = int(i)
            total.append(pow(score, 3))
            i = ''

        elif n == '*' or n == '#':
            if n == '#':
                total[len(total)-1] *= -1
            else:
                total.append(n)
        else:
            i += n

    print(total)

    if total[1] == '*':
        total[0] *= 2
        total.remove(total[1])

    if total[2] == '*':
        total[0] *= 2
        total[1] *= 2
        total.remove(total[2])
        print(total)

    if len(total) == 4:
        total[2] *= 2
        total[1] *= 2
        total.remove(total[3])
        return sum(total)
    else:
        return sum(total)


print(solution('1S*2T*3S'))
