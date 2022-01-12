'''
- 문제 설명 - 

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

- 제한사항
    array의 길이는 1 이상 100 이하입니다.
    array의 각 원소는 1 이상 100 이하입니다.
    commands의 길이는 1 이상 50 이하입니다.
    commands의 각 원소는 길이가 3입니다.
'''
# 1차원 함수일 경우

def solution(array, commands):

    answer = []

    cut_li = array[commands[0] - 1 : commands[1]]
    print("자른 후 리스트:",cut_li)

    cut_li.sort()
    print("오름차순 정렬:",cut_li)

    answer.append(cut_li[commands[2] - 1])
    print("자른 후 %d번째 숫자:" % commands[2] , answer)
    
    return answer


print("결과는",solution([101, 215, 322, 46, 3, 71, 435], [2, 7, 2]))




# 2차원 배열일 경우


'''

def solution(array, commands):
    answer = []
    
    for n in range(len(commands)):
        
        a = commands[n][0]
        b = commands[n][1]

        cut_li = array[a - 1 : b]
        cut_li.sort()
        
        answer.append(cut_li[commands[n][2] - 1])
        
    return answer

print("결과는",solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

'''