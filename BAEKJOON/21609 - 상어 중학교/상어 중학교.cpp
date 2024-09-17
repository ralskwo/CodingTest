#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const int EMPTY = -2; // 빈 공간을 나타내는 상수
const int BLACK = -1; // 검은색 블록을 나타내는 상수
const int RAINBOW = 0; // 무지개 블록을 나타내는 상수

// 네 방향 탐색을 위한 벡터 (상, 하, 좌, 우)
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

// BFS를 사용하여 블록 그룹을 찾는 함수
tuple<int, int, pair<int, int>, vector<pair<int, int>>> bfs(int N, vector<vector<int>>& grid, int startR, int startC, int color) {
    // BFS를 위한 큐와 방문 체크 배열
    queue<pair<int, int>> q;
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    
    // 블록 그룹 정보를 저장할 변수
    vector<pair<int, int>> group;
    int rainbowCount = 0;
    pair<int, int> standardBlock = {startR, startC}; // 기준 블록 (행, 열)

    // 시작점 초기화
    q.push({startR, startC});
    group.push_back({startR, startC});
    visited[startR][startC] = true;

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        // 네 방향 탐색
        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            // 격자 범위 내에 있고 방문하지 않은 경우
            if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc]) {
                // 같은 색상 블록이나 무지개 블록인 경우
                if (grid[nr][nc] == color || grid[nr][nc] == RAINBOW) {
                    visited[nr][nc] = true;
                    q.push({nr, nc});
                    group.push_back({nr, nc});
                    // 무지개 블록인 경우 카운트 증가
                    if (grid[nr][nc] == RAINBOW) {
                        rainbowCount++;
                    } else {
                        // 일반 블록인 경우 기준 블록 업데이트
                        if (make_pair(nr, nc) < standardBlock) {
                            standardBlock = {nr, nc};
                        }
                    }
                }
            }
        }
    }

    // 무지개 블록은 다른 그룹에서도 사용할 수 있도록 방문 표시를 초기화
    for (auto [r, c] : group) {
        if (grid[r][c] == RAINBOW) {
            visited[r][c] = false;
        }
    }

    return {group.size(), rainbowCount, standardBlock, group};
}

// 격자에서 가장 큰 블록 그룹을 찾는 함수
vector<pair<int, int>> findLargestBlockGroup(int N, vector<vector<int>>& grid) {
    vector<pair<int, int>> largestGroup;
    tuple<int, int, pair<int, int>, vector<pair<int, int>>> best = {0, 0, {0, 0}, {}};

    // 격자의 각 칸을 순회
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            // 일반 블록이면 BFS 실행
            if (grid[r][c] > 0) {
                auto [size, rainbowCount, standardBlock, group] = bfs(N, grid, r, c, grid[r][c]);
                // 그룹의 크기가 2 이상이어야 함
                if (size >= 2) {
                    // 조건에 따라 가장 큰 그룹 선택
                    best = max(best, {size, rainbowCount, standardBlock, group});
                }
            }
        }
    }

    // 가장 큰 그룹 반환
    return get<3>(best);
}

// 중력을 적용하여 블록을 아래로 떨어뜨리는 함수
void applyGravity(int N, vector<vector<int>>& grid) {
    // 각 열에 대해 아래에서 위로 탐색
    for (int col = 0; col < N; ++col) {
        int emptyRow = N - 1; // 블록이 내려올 빈 공간의 행 인덱스
        for (int row = N - 1; row >= 0; --row) {
            // 검은색 블록이면 빈 공간 업데이트
            if (grid[row][col] == BLACK) {
                emptyRow = row - 1;
            }
            // 일반 블록이나 무지개 블록인 경우
            else if (grid[row][col] >= 0) {
                // 블록을 아래로 이동
                if (emptyRow != row) {
                    grid[emptyRow][col] = grid[row][col];
                    grid[row][col] = EMPTY;
                }
                emptyRow--;
            }
        }
    }
}

// 격자를 90도 반시계 방향으로 회전하는 함수
vector<vector<int>> rotateCounterClockwise(int N, vector<vector<int>>& grid) {
    vector<vector<int>> newGrid(N, vector<int>(N, EMPTY)); // 새로운 격자 생성
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            // 회전한 위치에 값 할당
            newGrid[N - j - 1][i] = grid[i][j];
        }
    }
    return newGrid;
}

// 게임을 진행하여 총 점수를 계산하는 함수
int playGame(int N, vector<vector<int>>& grid) {
    int totalScore = 0;
    
    while (true) {
        // 1. 가장 큰 블록 그룹 찾기
        vector<pair<int, int>> largestGroup = findLargestBlockGroup(N, grid);
        if (largestGroup.empty()) {
            break; // 더 이상 블록 그룹이 없으면 종료
        }

        // 2. 블록 그룹 제거 및 점수 계산
        for (auto [r, c] : largestGroup) {
            grid[r][c] = EMPTY; // 블록 제거
        }
        totalScore += largestGroup.size() * largestGroup.size(); // 점수 누적

        // 3. 중력 적용
        applyGravity(N, grid);

        // 4. 격자를 90도 반시계 방향으로 회전
        grid = rotateCounterClockwise(N, grid);

        // 5. 중력 재적용
        applyGravity(N, grid);
    }

    return totalScore;
}

int main() {
    int N, M;
    cin >> N >> M;

    // 격자 입력
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    // 게임 진행 및 결과 출력
    int result = playGame(N, grid);
    cout << result << endl;

    return 0;
}
