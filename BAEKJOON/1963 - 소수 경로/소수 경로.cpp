#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstring> // memset 함수 사용을 위한 헤더

using namespace std;

// 1000 이상 9999 이하의 소수를 판별하기 위한 배열
bool is_prime[10000];

// 에라토스테네스의 체를 사용하여 소수를 구하는 함수
void sieve_of_eratosthenes() {
    memset(is_prime, true, sizeof(is_prime)); // 배열을 true로 초기화
    is_prime[0] = is_prime[1] = false; // 0과 1은 소수가 아님
    
    for (int i = 2; i <= sqrt(9999); i++) { // 2부터 9999의 제곱근까지 반복
        if (is_prime[i]) { // i가 소수인 경우
            for (int j = i * i; j <= 9999; j += i) { // i의 배수를 모두 소수가 아님으로 설정
                is_prime[j] = false;
            }
        }
    }
}

// 한 자리만 바꿔서 나올 수 있는 이웃 소수들을 반환하는 함수
vector<int> get_neighbors(int num) {
    vector<int> neighbors;
    string num_str = to_string(num); // 숫자를 문자열로 변환

    for (int i = 0; i < 4; i++) { // 각 자리수에 대해
        char original = num_str[i]; // 원래 숫자를 저장

        for (char d = '0'; d <= '9'; d++) { // 각 자리수를 0부터 9로 바꾸어 봄
            if (num_str[i] != d) { // 다른 숫자로 변경 시도
                num_str[i] = d; // 해당 자리수를 변경
                int new_num = stoi(num_str); // 새로운 숫자를 정수로 변환
                
                // 1000 이상이고 소수인 경우만 이웃으로 추가
                if (new_num >= 1000 && is_prime[new_num]) {
                    neighbors.push_back(new_num);
                }
            }
        }

        num_str[i] = original; // 원래 자리수로 복원
    }

    return neighbors; // 가능한 이웃 소수들을 반환
}

// BFS를 사용하여 최소 변환 횟수를 계산하는 함수
int bfs(int start, int end) {
    if (start == end) return 0; // 시작과 목표가 같으면 0을 반환

    queue<pair<int, int>> q; // 큐에는 현재 소수와 그 소수까지의 변환 횟수를 저장
    bool visited[10000]; // 각 숫자에 대해 방문 여부를 저장
    memset(visited, false, sizeof(visited)); // 방문 배열을 false로 초기화

    q.push({start, 0}); // 시작 소수와 0번째 변환 횟수를 큐에 추가
    visited[start] = true; // 시작 소수 방문 처리

    while (!q.empty()) {
        int current = q.front().first; // 현재 소수
        int steps = q.front().second; // 현재까지의 변환 횟수
        q.pop();

        vector<int> neighbors = get_neighbors(current); // 이웃 소수들을 구함

        for (int neighbor : neighbors) { // 이웃 소수들을 하나씩 확인
            if (!visited[neighbor]) { // 방문하지 않은 소수인 경우
                if (neighbor == end) return steps + 1; // 목표 소수에 도달한 경우 변환 횟수 반환
                visited[neighbor] = true; // 방문 처리
                q.push({neighbor, steps + 1}); // 이웃 소수를 큐에 추가
            }
        }
    }

    return -1; // 목표 소수에 도달할 수 없는 경우 -1 반환
}

int main() {
    int T; // 테스트 케이스 수
    cin >> T;

    sieve_of_eratosthenes(); // 소수를 미리 계산

    while (T--) {
        int start, end;
        cin >> start >> end; // 시작 소수와 목표 소수를 입력받음
        int result = bfs(start, end); // BFS를 통해 변환 횟수 계산

        if (result == -1)
            cout << "Impossible" << endl; // 변환이 불가능한 경우
        else
            cout << result << endl; // 변환이 가능한 경우 최소 횟수 출력
    }

    return 0;
}
