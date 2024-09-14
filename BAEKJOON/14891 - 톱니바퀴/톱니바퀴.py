def rotate_gear(gear, direction):
    # 톱니바퀴를 시계 방향으로 회전
    if direction == 1:
        # 톱니바퀴를 오른쪽으로 한 칸씩 이동
        return [gear[-1]] + gear[:-1]
    # 톱니바퀴를 반시계 방향으로 회전
    elif direction == -1:
        # 톱니바퀴를 왼쪽으로 한 칸씩 이동
        return gear[1:] + [gear[0]]

def simulate_gears(gears, rotations):
    # 주어진 회전 명령들을 순차적으로 처리
    for gear_index, direction in rotations:
        # 각 톱니바퀴의 회전 방향을 저장하는 리스트 초기화
        rotation_directions = [0, 0, 0, 0]
        # 현재 회전시킬 톱니바퀴의 방향 설정
        rotation_directions[gear_index - 1] = direction
        
        # 현재 톱니바퀴의 왼쪽에 있는 톱니바퀴들에 대해 회전 영향 전파
        for i in range(gear_index - 1, 0, -1):
            # 현재 톱니바퀴와 왼쪽 톱니바퀴의 맞닿은 극이 다를 경우
            if gears[i][6] != gears[i - 1][2]:
                # 왼쪽 톱니바퀴는 현재 톱니바퀴와 반대 방향으로 회전
                rotation_directions[i - 1] = -rotation_directions[i]
            else:
                # 맞닿은 극이 같으면 더 이상 왼쪽으로 전파되지 않음
                break
        
        # 현재 톱니바퀴의 오른쪽에 있는 톱니바퀴들에 대해 회전 영향 전파
        for i in range(gear_index - 1, 3):
            # 현재 톱니바퀴와 오른쪽 톱니바퀴의 맞닿은 극이 다를 경우
            if gears[i][2] != gears[i + 1][6]:
                # 오른쪽 톱니바퀴는 현재 톱니바퀴와 반대 방향으로 회전
                rotation_directions[i + 1] = -rotation_directions[i]
            else:
                # 맞닿은 극이 같으면 더 이상 오른쪽으로 전파되지 않음
                break
        
        # 저장된 회전 방향에 따라 톱니바퀴들을 회전
        for i in range(4):
            if rotation_directions[i] != 0:
                gears[i] = rotate_gear(gears[i], rotation_directions[i])
    
    # 회전 후의 톱니바퀴 상태 반환
    return gears

def calculate_score(gears):
    # 최종 점수를 저장할 변수 초기화
    score = 0
    # 각 톱니바퀴의 12시 방향을 검사하여 점수 계산
    for i in range(4):
        if gears[i][0] == '1':
            # 톱니바퀴의 12시 방향이 S극('1')이면 점수를 추가
            score += 2 ** i
    # 최종 점수 반환
    return score

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 첫 4개의 줄을 통해 톱니바퀴의 초기 상태를 저장
    gears = [list(data[i]) for i in range(4)]
    
    # 회전 횟수 K를 입력받음
    K = int(data[4])
    
    # 회전 정보들을 저장할 리스트 초기화
    rotations = []
    # 회전 정보는 톱니바퀴 번호와 회전 방향으로 주어지므로 이를 파싱하여 저장
    for i in range(5, 5 + K * 2, 2):
        gear_index = int(data[i])
        direction = int(data[i + 1])
        rotations.append((gear_index, direction))
    
    # 주어진 회전 정보에 따라 톱니바퀴들을 회전시킴
    gears = simulate_gears(gears, rotations)
    
    # 회전이 모두 끝난 후 최종 점수를 계산
    score = calculate_score(gears)
    
    # 최종 점수 출력
    print(score)

if __name__ == "__main__":
    main()
