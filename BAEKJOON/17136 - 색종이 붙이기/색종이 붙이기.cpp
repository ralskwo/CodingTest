#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int board[10][10]; // 10x10 보드
int papers[6] = {0, 5, 5, 5, 5, 5}; // 각 크기별 색종이의 남은 개수
int min_papers = INT_MAX; // 최소 색종이 개수 저장

// 특정 위치에서 주어진 크기의 색종이를 놓을 수 있는지 확인
bool canPlace(int x, int y, int size) {
    if (x + size > 10 || y + size > 10) return false; // 색종이가 범위를 벗어나면 배치 불가
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (board[x + i][y + j] == 0) return false; // 0이 있는 영역에는 배치 불가
        }
    }
    return true;
}

// 색종이를 배치하거나 제거
void placePaper(int x, int y, int size, int value) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            board[x + i][y + j] = value; // value가 0이면 배치, 1이면 제거
        }
    }
}

// 백트래킹으로 모든 경우 탐색
void solve(int count) {
    bool isComplete = true; // 모든 1이 덮였는지 확인
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (board[i][j] == 1) {
                isComplete = false; // 아직 덮이지 않은 1이 존재
                for (int size = 5; size >= 1; size--) {
                    if (papers[size] > 0 && canPlace(i, j, size)) {
                        placePaper(i, j, size, 0); // 색종이를 배치
                        papers[size]--;
                        solve(count + 1); // 재귀 호출로 다음 상태 탐색
                        papers[size]++;
                        placePaper(i, j, size, 1); // 상태 복구
                    }
                }
                return; // 탐색 후 더 이상 진행하지 않음
            }
        }
    }
    if (isComplete) min_papers = min(min_papers, count); // 모든 1을 덮었으면 최소값 갱신
}

int main() {
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cin >> board[i][j]; // 보드 입력
        }
    }
    solve(0); // 백트래킹 탐색 시작
    cout << (min_papers == INT_MAX ? -1 : min_papers) << endl; // 결과 출력
    return 0;
}
