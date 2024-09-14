#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 톱니바퀴 회전 함수
vector<int> rotate_gear(vector<int> gear, int direction) {
    // 시계 방향 회전
    if (direction == 1) {
        // 마지막 원소를 맨 앞으로 이동
        int last = gear.back();
        gear.pop_back();
        gear.insert(gear.begin(), last);
    }
    // 반시계 방향 회전
    else if (direction == -1) {
        // 첫 번째 원소를 맨 뒤로 이동
        int first = gear.front();
        gear.erase(gear.begin());
        gear.push_back(first);
    }
    return gear;
}

// 톱니바퀴 회전 시뮬레이션 함수
void simulate_gears(vector<vector<int>>& gears, vector<pair<int, int>>& rotations) {
    for (auto& rotation : rotations) {
        int gear_index = rotation.first - 1;
        int direction = rotation.second;

        // 각 톱니바퀴의 회전 방향을 기록하는 배열
        vector<int> rotation_directions(4, 0);
        rotation_directions[gear_index] = direction;

        // 현재 톱니바퀴의 왼쪽으로 영향 전파
        for (int i = gear_index; i > 0; i--) {
            if (gears[i][6] != gears[i - 1][2]) {
                rotation_directions[i - 1] = -rotation_directions[i];
            } else {
                break;
            }
        }

        // 현재 톱니바퀴의 오른쪽으로 영향 전파
        for (int i = gear_index; i < 3; i++) {
            if (gears[i][2] != gears[i + 1][6]) {
                rotation_directions[i + 1] = -rotation_directions[i];
            } else {
                break;
            }
        }

        // 기록된 회전 방향에 따라 톱니바퀴 회전
        for (int i = 0; i < 4; i++) {
            if (rotation_directions[i] != 0) {
                gears[i] = rotate_gear(gears[i], rotation_directions[i]);
            }
        }
    }
}

// 점수 계산 함수
int calculate_score(const vector<vector<int>>& gears) {
    int score = 0;
    for (int i = 0; i < 4; i++) {
        // 12시 방향이 S극인 경우
        if (gears[i][0] == 1) {
            score += (1 << i); // 2의 i승 더하기
        }
    }
    return score;
}

int main() {
    vector<vector<int>> gears(4, vector<int>(8)); // 4개의 톱니바퀴 상태를 저장
    vector<pair<int, int>> rotations; // 회전 정보

    // 톱니바퀴 초기 상태 입력
    for (int i = 0; i < 4; i++) {
        string input;
        cin >> input;
        for (int j = 0; j < 8; j++) {
            gears[i][j] = input[j] - '0'; // 문자열을 숫자로 변환하여 저장
        }
    }

    int K;
    cin >> K; // 회전 횟수 입력

    // 회전 명령 입력
    for (int i = 0; i < K; i++) {
        int gear_index, direction;
        cin >> gear_index >> direction;
        rotations.push_back({gear_index, direction});
    }

    // 시뮬레이션 실행
    simulate_gears(gears, rotations);

    // 점수 계산 및 출력
    int score = calculate_score(gears);
    cout << score << endl;

    return 0;
}
