from itertools import combinations  # 궁수 배치의 가능한 조합을 구하기 위해 combinations 함수 임포트
import copy  # 격자판 상태를 복사하기 위해 copy 모듈 사용

def simulate_attack(N, M, D, board, archers):
    count = 0  # 제거한 적의 수를 세는 변수
    enemies = [row[:] for row in board]  # 원본 격자판을 복사하여 게임 중 변형되지 않게 하기 위함
    
    while any(sum(row) for row in enemies):  # 적이 남아 있는 동안 반복
        targets = set()  # 이번 턴에 공격할 적의 좌표를 저장하는 집합
        
        for archer in archers:  # 각 궁수에 대해
            min_dist = D + 1  # 궁수가 공격 가능한 최대 거리를 설정 (처음엔 무한대처럼 큰 값으로 시작)
            target = None  # 공격할 적의 위치를 저장할 변수
            
            for r in range(N):  # 모든 행에 대해
                for c in range(M):  # 모든 열에 대해
                    if enemies[r][c] == 1:  # 적이 있는 경우
                        dist = abs(N - r) + abs(archer - c)  # 궁수와 적 사이의 거리 계산 (맨해튼 거리)
                        if dist <= D:  # 궁수의 공격 범위 내에 있는 적이라면
                            if dist < min_dist or (dist == min_dist and c < target[1]):  # 가장 가까운 적 또는 왼쪽에 있는 적을 선택
                                min_dist = dist  # 가장 가까운 거리로 갱신
                                target = (r, c)  # 공격할 적의 위치 갱신
                                
            if target:  # 공격할 적이 있으면
                targets.add(target)  # 해당 적의 위치를 이번 턴 공격 대상에 추가
        
        for r, c in targets:  # 이번 턴에 공격받을 적들에 대해
            if enemies[r][c] == 1:  # 적이 아직 남아 있는 경우
                enemies[r][c] = 0  # 적을 제거
                count += 1  # 제거한 적의 수 증가
        
        enemies.pop()  # 마지막 행의 적들은 성에 도착했으므로 제거
        enemies.insert(0, [0] * M)  # 적들이 한 칸 아래로 이동 (첫 행은 빈 칸으로 추가)
    
    return count  # 제거한 적의 수 반환

def castle_defense(N, M, D, board):
    max_kills = 0  # 최대 제거할 수 있는 적의 수를 저장하는 변수
    for archers in combinations(range(M), 3):  # M개의 열에서 궁수 3명을 배치하는 모든 조합에 대해
        kills = simulate_attack(N, M, D, board, archers)  # 각 궁수 배치에 대해 시뮬레이션 수행
        max_kills = max(max_kills, kills)  # 제거한 적의 최대 수를 갱신
    
    return max_kills  # 최대 제거한 적의 수 반환

N, M, D = map(int, input().split())  # 격자판의 크기와 궁수의 공격 거리 입력 받기
board = [list(map(int, input().split())) for _ in range(N)]  # 격자판 상태 입력 받기

print(castle_defense(N, M, D, board))  # 궁수 배치 후 제거할 수 있는 최대 적의 수 출력