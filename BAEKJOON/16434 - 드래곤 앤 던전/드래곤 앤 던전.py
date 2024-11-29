def minimum_max_hp(n, initial_atk, rooms):
    # 특정 HMaxHP로 던전을 돌파할 수 있는지 확인하는 함수
    def can_survive(hp):
        # 현재 생명력을 HMaxHP로 설정
        cur_hp = hp
        # 현재 공격력을 초기 공격력으로 설정
        cur_atk = initial_atk
        # 각 방을 순회하며 처리
        for t, a, h in rooms:
            if t == 1:  # 몬스터 방일 경우
                # 몬스터를 처치하기 위해 필요한 용사의 공격 횟수를 계산
                damage_to_take = (h + cur_atk - 1) // cur_atk - 1
                # 해당 횟수 동안 용사가 받는 데미지를 계산하여 현재 생명력에서 감소
                cur_hp -= damage_to_take * a
                # 생명력이 0 이하가 되면 던전을 돌파할 수 없음
                if cur_hp <= 0:
                    return False
            elif t == 2:  # 포션 방일 경우
                # 공격력을 증가시키고 생명력을 회복
                cur_atk += a
                cur_hp = min(hp, cur_hp + h)  # 최대 생명력을 초과하지 않도록 처리
        # 모든 방을 무사히 통과한 경우 True 반환
        return True

    # 이분 탐색의 범위를 설정 (최소값은 1, 최대값은 매우 큰 값 10^18)
    low, high = 1, 10**18

    # 이분 탐색을 통해 최소 HMaxHP를 찾음
    while low < high:
        # 중간 값을 계산
        mid = (low + high) // 2
        # 현재 중간 값으로 던전을 돌파할 수 있는지 확인
        if can_survive(mid):
            # 가능하다면 더 작은 값에서 정답을 찾기 위해 상한값을 줄임
            high = mid
        else:
            # 불가능하다면 더 큰 값에서 정답을 찾기 위해 하한값을 늘림
            low = mid + 1

    # 최소 HMaxHP를 반환
    return low


# 입력을 받아 던전의 방 수와 초기 공격력을 저장
n, initial_atk = map(int, input().split())

# 각 방의 정보를 리스트로 저장
rooms = [tuple(map(int, input().split())) for _ in range(n)]

# 최소 HMaxHP를 계산하고 출력
print(minimum_max_hp(n, initial_atk, rooms))
