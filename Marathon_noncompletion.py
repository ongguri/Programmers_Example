'''
- 문제 설명 -

수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.



※ 제한사항
    마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    completion의 길이는 participant의 길이보다 1 작습니다.
    참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    참가자 중에는 동명이인이 있을 수 있습니다.
'''


'''
- 처음 풀었을때 - 


def solution(participant, completion):
    
    answer = ''
    
    for n in participant:
        
        count = participant.count(n)
        
        if count >= 2:
            more = n
            count1 = participant.count(more)
            count2 = completion.count(more)
            
            if count1 == count2:
                print("%s 동명이인 전부 완주하였습니다." % more)
            
            else:
                answer += more
                break
                
        elif count == 1:
            
            if n not in completion:
                answer += n
                break
                
    return answer
'''


# 두번째 풀었을때

'''
def solution(participant, completion):

    answer = ''

    for n in participant:
        if n in completion:
            completion.remove(n)

        else:
            answer += n

    return answer


participant = ["a", "v", "b", "helim", "c", "c"]
completion = ["a", "c", "v", "c", "b"]

participant_copy = participant.copy()


if len(participant) == len(completion):

    for n in participant:
        if n in completion:
            completion.remove(n)
            participant_copy.remove(n)

    if participant_copy == []:
        print("전부 완주하였습니다.")

    else:
        print("%s 선수가 %s 선수로 완주자 명단에 잘못 기재되어 있습니다." %
              (participant_copy[0], completion[0]))

else:
    print("%s 선수는 완주하지 못하였습니다." % solution(participant, completion))
'''


def solution(part, come):

    part.sort()
    come.sort()

    for a in range(len(part)):
        try:
            if part[a] != come[a]:
                return part[a]
        except:
            return part[len(part)-1]


print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], [
      'josipa', 'filipa', 'marina', 'nikola']))
