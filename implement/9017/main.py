from sys import stdin

# 한 팀은 여섯명의 선수로 구성됨
# 팀 점수는 상위 네명의 주자의 점수 합
# 점수는 자격을 갖춘 팀의 주자들에게만 주어짐 -> 결승점을 통과한 순서대로 점수를 받는다.
# 점수 가장 낮은 팀이 우승
# 동점의 경우 다섯 번째 주자가 가장 빨리 들어온 팀이 우승하게 된다.

T = int(stdin.readline())

for _t in range(T):
    # print("test case# ", _t+1)
    N = int(stdin.readline())
    team_num = list(map(int, stdin.readline().split()))
    team_dic = {}

    team_set = set(team_num)
    # 팀원수 6명이 안되는 팀은 걸러버림
    not_count_team = []
    for _ in range(len(team_set)):
        target_team = team_set.pop()
        if team_num.count(target_team) != 6:
            not_count_team.append(target_team)

    # 점수 산정
    score = 1
    for i in range(len(team_num)):
        if team_num[i] not in not_count_team:
            if team_num[i] not in team_dic:
                team_dic[team_num[i]] = [score]
            else:
                team_dic[team_num[i]].append(score)
            score += 1
    # print(team_dic)
    scores = []
    # 팀들의 점수 합산
    keys = team_dic.keys()
    for key in keys:
        _sum = sum(team_dic[key][0:4])
        scores.append(_sum)
        team_dic[key].append(_sum)

    min_score = min(scores)
    if scores.count(min_score) > 1:
        # 동점자 있음
        same_score_key = []
        for key in keys:
            if team_dic[key][-1] == min_score:
                same_score_key.append(key)
        # 동점자들 점수 다시 비교
        scores = []
        for key in same_score_key:
            scores.append(team_dic[key][-1] + team_dic[key][4])
        min_score = min(scores)
        index = scores.index(min_score)
        print(same_score_key[index])
    else:
        for key in keys:
            if team_dic[key][-1] == min_score:
                print(key)
                break

