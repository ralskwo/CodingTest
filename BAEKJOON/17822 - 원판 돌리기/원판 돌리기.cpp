#include <iostream>
#include <deque>
#include <vector>
#include <tuple>
using namespace std;

// 입력을 위한 변수 선언
int N, M, T;
vector<deque<int>> board;
vector<tuple<int, int, int>> commands;  // 회전 명령을 저장할 튜플 리스트

// 인접한 수를 제거하는 함수
bool remove_adjacent() {
    vector<vector<bool>> to_remove(N, vector<bool>(M, false));  // 삭제할 좌표를 표시
    bool removed = false;  // 인접한 수가 삭제되었는지 여부
    
    // 모든 원판과 그 안의 수를 순회
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (board[i][j] == 0) continue;  // 0이면 이미 삭제된 수
            int cur = board[i][j];  // 현재 수
            
            // 같은 원판에서 좌우로 인접한 수 비교
            if (board[i][j] == board[i][(j + 1) % M]) {
                to_remove[i][j] = to_remove[i][(j + 1) % M] = true;
                removed = true;
            }
            if (board[i][j] == board[i][(j + M - 1) % M]) {
                to_remove[i][j] = to_remove[i][(j + M - 1) % M] = true;
                removed = true;
            }

            // 다른 원판과 상하로 인접한 수 비교
            if (i > 0 && board[i][j] == board[i - 1][j]) {
                to_remove[i][j] = to_remove[i - 1][j] = true;
                removed = true;
            }
            if (i < N - 1 && board[i][j] == board[i + 1][j]) {
                to_remove[i][j] = to_remove[i + 1][j] = true;
                removed = true;
            }
        }
    }

    // 인접한 수를 모두 0으로 변경
    if (removed) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (to_remove[i][j]) board[i][j] = 0;
            }
        }
    }
    
    return removed;
}

// 평균에 따른 수 조정 함수
void adjust_by_average() {
    int total_sum = 0, total_count = 0;

    // 모든 원판의 수를 합산하고 개수를 셈
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (board[i][j] != 0) {
                total_sum += board[i][j];
                total_count++;
            }
        }
    }

    if (total_count == 0) return;  // 남은 수가 없으면 함수 종료

    double average = (double)total_sum / total_count;  // 평균 계산

    // 평균에 따라 수를 조정
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (board[i][j] != 0) {
                if (board[i][j] > average) board[i][j]--;  // 평균보다 크면 1 감소
                else if (board[i][j] < average) board[i][j]++;  // 평균보다 작으면 1 증가
            }
        }
    }
}

// 원판을 회전시키는 함수
void rotate(int x, int d, int k) {
    for (int i = x - 1; i < N; i += x) {
        if (d == 0) {  // 시계 방향
            for (int j = 0; j < k; ++j) {
                board[i].push_front(board[i].back());  // 마지막 원소를 맨 앞에 추가
                board[i].pop_back();  // 마지막 원소 제거
            }
        } else {  // 반시계 방향
            for (int j = 0; j < k; ++j) {
                board[i].push_back(board[i].front());  // 첫 원소를 맨 뒤에 추가
                board[i].pop_front();  // 첫 원소 제거
            }
        }
    }
}

int main() {
    // 입력 받기
    cin >> N >> M >> T;
    board.resize(N);  // N개의 원판 공간 할당
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int num;
            cin >> num;
            board[i].push_back(num);  // 각 원판의 숫자 저장
        }
    }

    for (int i = 0; i < T; ++i) {
        int x, d, k;
        cin >> x >> d >> k;
        commands.push_back(make_tuple(x, d, k));  // 회전 명령 저장
    }

    // 회전 명령을 처리
    for (auto command : commands) {
        int x, d, k;
        tie(x, d, k) = command;
        rotate(x, d, k);  // 회전 수행
        
        // 인접한 수를 제거하거나 평균에 따라 조정
        if (!remove_adjacent()) {
            adjust_by_average();
        }
    }

    // 최종 결과 계산
    int result = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            result += board[i][j];  // 남아 있는 숫자들의 합 계산
        }
    }

    cout << result << endl;  // 결과 출력
    return 0;
}