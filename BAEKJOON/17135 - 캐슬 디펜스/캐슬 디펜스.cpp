#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int SimulateAttack(int N, int M, int D, vector<vector<int>>& board, vector<int>& archers) {
    int count = 0; // 제거한 적의 수를 저장하는 변수
    vector<vector<int>> enemies = board; // 보드의 상태를 복사하여 적의 위치 정보 저장
    
    while (true) {
        // 적이 남아있는지 확인
        bool enemiesExist = false;
        for (const auto& row : enemies) {
            if (find(row.begin(), row.end(), 1) != row.end()) {
                enemiesExist = true;
                break;
            }
        }
        if (!enemiesExist) break; // 적이 없으면 시뮬레이션 종료

        set<pair<int, int>> targets; // 공격할 적의 좌표를 저장하는 집합
        
        // 각 궁수에 대해 공격할 적 선정
        for (int archer : archers) {
            int minDist = D + 1; // 최소 거리 초기화 (D보다 큰 값으로)
            pair<int, int> target = {-1, -1}; // 공격 대상 초기화
            
            // 모든 적의 위치를 검사
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    if (enemies[r][c] == 1) { // 적이 있는 칸이면
                        int dist = abs(N - r) + abs(archer - c); // 거리 계산
                        // 공격 가능 거리 내에 있고, 가장 가까우며, 가장 왼쪽에 있는 적 선택
                        if (dist <= D && (dist < minDist || (dist == minDist && c < target.second))) {
                            minDist = dist;
                            target = {r, c};
                        }
                    }
                }
            }
            
            if (target.first != -1) targets.insert(target); // 유효한 타겟이면 추가
        }
        
        // 선택된 타겟들 제거
        for (const auto& t : targets) {
            if (enemies[t.first][t.second] == 1) {
                enemies[t.first][t.second] = 0; // 적 제거
                count++; // 제거한 적의 수 증가
            }
        }
        
        // 적들을 한 칸씩 아래로 이동
        for (int r = N - 1; r > 0; r--) {
            enemies[r] = enemies[r - 1];
        }
        enemies[0] = vector<int>(M, 0); // 첫 행은 빈 칸으로 초기화
    }
    
    return count; // 제거한 총 적의 수 반환
}

int CastleDefense(int N, int M, int D, vector<vector<int>>& board) {
    int maxKills = 0; // 최대 제거 가능한 적의 수
    vector<int> archers(3); // 궁수 3명의 위치를 저장할 벡터
    
    // 가능한 모든 궁수 배치 조합에 대해 시뮬레이션
    for (int i = 0; i < M; i++) {
        for (int j = i + 1; j < M; j++) {
            for (int k = j + 1; k < M; k++) {
                archers[0] = i;
                archers[1] = j;
                archers[2] = k;
                // 현재 배치로 시뮬레이션 실행 후 최대값 갱신
                maxKills = max(maxKills, SimulateAttack(N, M, D, board, archers));
            }
        }
    }
    
    return maxKills; // 최대 제거 가능한 적의 수 반환
}

int main() {
    int N, M, D;
    cin >> N >> M >> D; // 격자판 크기와 공격 거리 입력 받기
    
    // 격자판 상태 입력 받기
    vector<vector<int>> board(N, vector<int>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }
    
    // 결과 출력
    cout << CastleDefense(N, M, D, board) << endl;
    
    return 0;
}