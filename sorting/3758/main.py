
import copy
from sys import stdin

T = int(stdin.readline())

for t in range(T):
    # test case
    log = []
    team_size, problem_size, my_team_id, log_size = map(int, stdin.readline().split())
    # 문제별 점수[0], total 점수[1], 마지막 제출[2], 제출 횟수[3]
    default_team = [[0 for _ in range(problem_size)], 0, 0, 0]
    team = []

    for i in range(team_size):
        my_team = copy.deepcopy(default_team)
        my_team.append(i)
        team.append(my_team)

    # log setting
    for idx in range(log_size):
        _log = list(map(int, stdin.readline().split()))
        log.append(_log)

        # 특정 팀 db 접근 team[team_id]
        team_id = _log[0]-1
        problem_id = _log[1]-1
        score = _log[2]
        team[team_id][0][problem_id] = max(team[team_id][0][problem_id], score) # 더 높은 점수로 업데이트
        team[team_id][2] = idx # 마지막 제출 언제인지 업데이트
        team[team_id][3] += 1 # 제출 횟수 업데이트


    # 팀별 total 점수 계산
    for i in range(team_size):
        total = 0
        for j in range(problem_size):
            total += team[i][0][j]
        team[i][1] = total

    # 순위 계산
    # -x[1] 점수 높은 순, x[3] 제출횟수 적은 순, x[2] 마지막 제출이 빠른 순
    team.sort(key=lambda x: (-x[1], x[3], x[2]))

    # 내팀 몇등인지 찾기
    for i in range(team_size):
        if team[i][4] == my_team_id-1:
            print(i+1)
            break