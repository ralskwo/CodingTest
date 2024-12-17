from collections import (
    deque,
)  # deque를 사용하기 위해 collections 모듈에서 deque를 가져옴


def bfs(S):  # 이모티콘 S개를 화면에 만드는데 걸리는 최소 시간을 구하는 BFS 함수
    queue = deque(
        [(1, 0, 0)]
    )  # 초기 상태: 화면에 이모티콘 1개, 클립보드에 0개, 시간은 0초
    visited = [
        [False] * (S + 1) for _ in range(S + 1)
    ]  # 방문 여부를 저장하는 2차원 리스트
    visited[1][0] = True  # 시작 상태인 (화면에 1개, 클립보드에 0개)를 방문 처리

    while queue:  # 큐가 비어있지 않는 동안 반복
        screen, clipboard, time = (
            queue.popleft()
        )  # 현재 상태를 큐에서 꺼냄 (화면 이모티콘 수, 클립보드 이모티콘 수, 시간)

        if screen == S:  # 화면에 있는 이모티콘 개수가 S에 도달하면 현재까지의 시간 반환
            return time

        # 연산 1: 화면에 있는 이모티콘을 복사해서 클립보드에 저장
        if not visited[screen][screen]:  # 복사한 상태를 방문하지 않았다면
            visited[screen][screen] = True  # 방문 처리
            queue.append(
                (screen, screen, time + 1)
            )  # 새로운 상태를 큐에 추가 (화면 그대로, 클립보드에 screen 저장, 시간 1초 추가)

        # 연산 2: 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if (
            clipboard > 0
            and screen + clipboard <= S
            and not visited[screen + clipboard][clipboard]
        ):
            # 클립보드에 이모티콘이 있고, 화면에 붙여넣은 결과가 S를 넘지 않으며, 방문하지 않았다면
            visited[screen + clipboard][clipboard] = True  # 방문 처리
            queue.append(
                (screen + clipboard, clipboard, time + 1)
            )  # 새로운 상태를 큐에 추가 (화면에 붙여넣기 결과, 클립보드 그대로, 시간 1초 추가)

        # 연산 3: 화면에 있는 이모티콘 중 하나 삭제
        if (
            screen > 0 and not visited[screen - 1][clipboard]
        ):  # 화면에 이모티콘이 있고, 삭제한 상태를 방문하지 않았다면
            visited[screen - 1][clipboard] = True  # 방문 처리
            queue.append(
                (screen - 1, clipboard, time + 1)
            )  # 새로운 상태를 큐에 추가 (화면에서 1개 삭제, 클립보드 그대로, 시간 1초 추가)


S = int(input())  # 목표 이모티콘 개수 S를 입력받음
print(bfs(S))  # 최소 시간을 출력
