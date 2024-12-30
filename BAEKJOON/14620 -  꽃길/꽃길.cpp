#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // INT_MAX 사용을 위한 헤더 포함

using namespace std;

// 방향 벡터 (상, 하, 좌, 우)
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

// 꽃이 차지하는 5칸의 비용을 계산하는 함수
int calculateCost(vector<vector<int>>& board, int x, int y) {
    int cost = board[x][y]; // 중심 칸의 비용
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        cost += board[nx][ny]; // 상하좌우 비용 추가
    }
    return cost;
}

// 꽃이 화단 범위 내에 있는지 확인하는 함수
bool isValid(int x, int y, int N) {
    return x > 0 && x < N - 1 && y > 0 && y < N - 1;
}

// 꽃이 다른 꽃과 겹치는지 확인하는 함수
bool checkOverlap(vector<vector<bool>>& visited, int x, int y) {
    if (visited[x][y]) return false; // 중심 겹침 검사
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (visited[nx][ny]) return false; // 꽃잎 겹침 검사
    }
    return true;
}

// 꽃을 심고 방문 상태를 처리하는 함수
void placeFlower(vector<vector<bool>>& visited, int x, int y, bool place) {
    visited[x][y] = place; // 중심 칸 방문 처리
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        visited[nx][ny] = place; // 상하좌우 방문 처리
    }
}

// 문제 해결 함수
int solve(int N, vector<vector<int>>& board) {
    vector<pair<int, int>> candidates; // 가능한 꽃 중심 좌표 리스트
    int minCost = INT_MAX; // 최소 비용 초기화

    // 가능한 꽃 중심 좌표를 (1, 1)부터 (N-2, N-2)까지 저장
    for (int x = 1; x < N - 1; x++) {
        for (int y = 1; y < N - 1; y++) {
            candidates.push_back({x, y});
        }
    }

    // 세 개의 꽃 중심을 선택하는 모든 조합 탐색
    int C = candidates.size();
    for (int i = 0; i < C; i++) {
        for (int j = i + 1; j < C; j++) {
            for (int k = j + 1; k < C; k++) {
                vector<vector<bool>> visited(N, vector<bool>(N, false)); // 방문 상태 초기화
                bool valid = true;
                int totalCost = 0;

                // 조합으로 선택된 좌표에 꽃을 심기
                for (auto [x, y] : {candidates[i], candidates[j], candidates[k]}) {
                    if (!isValid(x, y, N) || !checkOverlap(visited, x, y)) {
                        valid = false; // 유효하지 않은 경우
                        break;
                    }
                    totalCost += calculateCost(board, x, y); // 비용 계산
                    placeFlower(visited, x, y, true); // 방문 처리
                }

                if (valid) { // 유효한 경우 최소 비용 갱신
                    minCost = min(minCost, totalCost);
                }
            }
        }
    }

    return minCost; // 최소 비용 반환
}

// 메인 함수
int main() {
    int N;
    cin >> N; // 화단 크기 입력
    vector<vector<int>> board(N, vector<int>(N)); // 화단 비용 배열

    // 화단 비용 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    // 최소 비용 계산 및 출력
    cout << solve(N, board) << endl;

    return 0;
}
