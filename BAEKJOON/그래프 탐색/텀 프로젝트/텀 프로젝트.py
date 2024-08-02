import sys

def find_teams(n, choices):
    visited = [0] * (n + 1)  # 방문 상태를 저장하는 배열 초기화
    team = [0] * (n + 1)  # 팀에 속한 상태를 저장하는 배열 초기화
    team_count = 0  # 팀의 개수 초기화

    for student in range(1, n + 1):  # 모든 학생에 대해 탐색 시작
        if not visited[student]:  # 해당 학생이 방문되지 않은 경우
            stack = []  # 스택 초기화
            current = student  # 현재 학생을 현재 위치로 설정

            while not visited[current]:  # 현재 학생이 방문되지 않은 경우 반복
                visited[current] = student  # 현재 학생을 방문 상태로 설정
                stack.append(current)  # 현재 학생을 스택에 추가
                current = choices[current]  # 다음 학생으로 이동

            if visited[current] == student:  # 싸이클이 형성된 경우
                while stack and stack[-1] != current:  # 스택에서 싸이클의 시작점까지 팝
                    team[stack.pop()] = 1  # 싸이클에 속한 학생을 팀에 속한 것으로 설정
                team[stack.pop()] = 1  # 싸이클의 시작점을 팀에 속한 것으로 설정
                team_count += 1  # 팀의 개수 증가

            while stack:  # 남아있는 스택 요소 처리
                team[stack.pop()] = 0  # 싸이클에 속하지 않은 학생을 팀에 속하지 않은 것으로 설정

    return n - sum(team)  # 팀에 속하지 않은 학생의 수 반환

def main():
    input = sys.stdin.read  # 표준 입력을 읽어옴
    data = input().split()  # 입력 데이터를 공백으로 분리

    index = 0  # 데이터 인덱스 초기화
    T = int(data[index])  # 테스트 케이스의 수
    index += 1
    results = []  # 결과를 저장할 리스트 초기화

    for _ in range(T):  # 각 테스트 케이스에 대해
        n = int(data[index])  # 학생의 수
        index += 1
        choices = [0] + list(map(int, data[index:index + n]))  # 학생들이 선택한 학생 배열
        index += n
        result = find_teams(n, choices)  # 팀에 속하지 않은 학생의 수 계산
        results.append(result)  # 결과 리스트에 추가

    for res in results:  # 각 테스트 케이스의 결과 출력
        print(res)

if __name__ == "__main__":  # 메인 함수 실행
    main()
