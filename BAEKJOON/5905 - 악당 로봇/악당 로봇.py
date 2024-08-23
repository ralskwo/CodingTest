from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        # 트라이의 상태 개수를 초기화합니다. 루트는 상태 1로 시작합니다.
        self.num_states = 1
        # 트라이의 상태 전이 테이블을 초기화합니다. 각 상태에서 'A', 'B', 'C'에 해당하는 인덱스는 0, 1, 2입니다.
        self.transition = defaultdict(lambda: [0] * 3)
        # 실패 링크 테이블을 초기화합니다.
        self.fail = [0] * (20 * 15 + 2)
        # 각 상태에서의 출력(패턴의 끝 여부)을 저장하는 테이블을 초기화합니다.
        self.output = [0] * (20 * 15 + 2)

    def insert(self, word):
        # 주어진 단어를 트라이에 삽입하는 함수입니다.
        current_state = 1  # 루트 상태에서 시작합니다.
        for char in word:
            index = ord(char) - ord('A')  # 문자를 인덱스로 변환합니다 ('A' -> 0, 'B' -> 1, 'C' -> 2).
            if self.transition[current_state][index] == 0:
                # 현재 상태에서 해당 문자의 전이 상태가 없으면 새 상태를 만듭니다.
                self.num_states += 1
                self.transition[current_state][index] = self.num_states
            # 다음 상태로 전이합니다.
            current_state = self.transition[current_state][index]
        # 단어의 끝을 표시하기 위해 출력 배열을 증가시킵니다.
        self.output[current_state] += 1

    def build_failure(self):
        # 트라이의 실패 링크를 구축하는 함수입니다.
        queue = deque([1])  # BFS를 위한 큐를 초기화합니다.
        self.fail[1] = 1  # 루트의 실패 링크는 자기 자신을 가리킵니다.

        while queue:
            current_state = queue.popleft()  # 큐에서 현재 상태를 꺼냅니다.
            for i in range(3):  # 'A', 'B', 'C' 각각에 대해 처리합니다.
                next_state = self.transition[current_state][i]
                if next_state == 0:
                    continue

                if current_state == 1:
                    # 루트 상태의 자식들은 실패 링크가 루트 상태를 가리킵니다.
                    self.fail[next_state] = 1
                    queue.append(next_state)
                    continue

                # 실패 링크를 따라가며 일치하는 상태를 찾습니다.
                failure_state = self.fail[current_state]
                while failure_state != 1 and self.transition[failure_state][i] == 0:
                    failure_state = self.fail[failure_state]

                if self.transition[failure_state][i] != 0:
                    failure_state = self.transition[failure_state][i]

                self.fail[next_state] = failure_state
                self.output[next_state] += self.output[failure_state]  # 출력 배열 갱신
                queue.append(next_state)

def main():
    import sys
    input = sys.stdin.read 
    data = input().split()

    # 입력을 파싱하여 변수에 저장합니다.
    N = int(data[0])  # 패턴의 수
    K = int(data[1])  # 문자열의 길이
    patterns = data[2:2 + N]  # 패턴 리스트
    ac = AhoCorasick()  # Aho-Corasick 인스턴스를 생성합니다.

    for pattern in patterns:
        ac.insert(pattern)  # 각 패턴을 트라이에 삽입합니다.

    ac.build_failure()  # 실패 링크를 구축합니다.

    # DP 배열을 초기화합니다. -1은 아직 도달하지 못한 상태를 의미합니다.
    dp = [[-1] * (20 * 15 + 2) for _ in range(K + 2)]
    dp[0][1] = 0  # 초기 상태 (루트)에서 시작합니다.

    # DP를 통해 최적의 해를 구합니다.
    for k in range(K + 1):
        for state in range(1, ac.num_states + 1):
            if dp[k][state] == -1:
                continue

            for i in range(3):  # 'A', 'B', 'C' 각각에 대해 처리합니다.
                current_state = state

                while current_state != 1 and ac.transition[current_state][i] == 0:
                    current_state = ac.fail[current_state]  # 실패 링크를 따라갑니다.
                if ac.transition[current_state][i] != 0:
                    current_state = ac.transition[current_state][i]

                dp[k + 1][current_state] = max(dp[k + 1][current_state], dp[k][state] + ac.output[current_state])

    # 가능한 최대 매칭 수를 구합니다.
    answer = 0
    for state in range(1, ac.num_states + 1):
        answer = max(answer, dp[K][state])

    print(answer)  # 정답을 출력합니다.

if __name__ == "__main__":
    main()
