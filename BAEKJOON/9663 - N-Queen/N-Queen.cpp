#include <iostream>
using namespace std;

int N;  // 체스판의 크기 (퀸의 개수)
int count = 0;  // 가능한 배치 수를 저장

// 백트래킹을 통해 퀸을 배치하는 함수
void solve(int row, int cols, int diag1, int diag2) {
    // 모든 퀸을 배치한 경우, 카운트 증가
    if (row == N) {
        count++;
        return;
    }

    // 퀸을 놓을 수 있는 자리 계산 (가능한 열)
    int available_positions = (~(cols | diag1 | diag2)) & ((1 << N) - 1);

    // 가능한 자리에 퀸을 놓는 과정
    while (available_positions) {
        // 가장 오른쪽의 1비트를 추출 (퀸을 놓을 자리)
        int pos = available_positions & -available_positions;

        // 해당 자리에 퀸을 놓았으므로 그 자리를 제거
        available_positions -= pos;

        // 다음 행으로 넘어가면서 열, 좌하향 대각선, 우하향 대각선 상태를 갱신하여 재귀 호출
        solve(row + 1, cols | pos, (diag1 | pos) << 1, (diag2 | pos) >> 1);
    }
}

int main() {
    // 사용자로부터 N 입력받기
    cin >> N;

    // 초기 상태로 백트래킹 시작 (row = 0에서 시작)
    solve(0, 0, 0, 0);

    // 가능한 배치 경우의 수 출력
    cout << count << endl;

    return 0;
}
