#include <iostream>  // 표준 입출력 라이브러리
#include <deque>     // 덱을 사용하기 위한 라이브러리
#include <vector>    // 벡터를 사용하기 위한 라이브러리
#include <map>       // 맵을 사용하기 위한 라이브러리

using namespace std;

int n, k;  // 보드 크기와 사과 개수를 저장하는 변수
vector<vector<int>> board;  // 보드를 나타내는 2차원 벡터
deque<pair<int, int>> snake;  // 뱀의 위치를 저장하는 덱
map<int, char> changes;  // 시간과 방향 전환 정보를 저장하는 맵

int dx[4] = {0, 1, 0, -1};  // 오른쪽, 아래, 왼쪽, 위쪽 방향 벡터
int dy[4] = {1, 0, -1, 0};

int turn(int direction, char c) {
    if (c == 'L') {  // 왼쪽으로 90도 회전
        return (direction + 3) % 4;
    } else {  // 오른쪽으로 90도 회전
        return (direction + 1) % 4;
    }
}

int simulate() {
    int time = 0, direction = 0;  // 시작 시간과 초기 방향(오른쪽)
    snake.push_back({0, 0});  // 뱀의 초기 위치를 덱에 저장
    board[0][0] = 2;  // 보드에서 뱀의 위치를 표시 (2로 설정)

    while (true) {
        time++;  // 1초 경과
        int nx = snake.front().first + dx[direction];  // 새로운 머리 위치 계산 (x 좌표)
        int ny = snake.front().second + dy[direction];  // 새로운 머리 위치 계산 (y 좌표)

        // 벽에 부딪히거나 자기 자신과 부딪히면 게임 종료
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] == 2) {
            return time;
        }

        // 새로운 위치로 머리 이동
        if (board[nx][ny] == 1) {  // 사과가 있는 경우
            board[nx][ny] = 2;  // 사과를 먹고 뱀의 머리를 위치시킴
            snake.push_front({nx, ny});  // 뱀의 길이를 늘림
        } else {  // 사과가 없는 경우
            board[nx][ny] = 2;  // 머리를 새로운 위치로 이동
            snake.push_front({nx, ny});
            int tail_x = snake.back().first;  // 꼬리 위치
            int tail_y = snake.back().second;
            board[tail_x][tail_y] = 0;  // 꼬리를 비워줌
            snake.pop_back();  // 뱀의 길이 유지
        }

        if (changes[time]) {  // 시간에 맞춰 방향 전환
            direction = turn(direction, changes[time]);
        }
    }
}

int main() {
    cin >> n >> k;  // 보드 크기와 사과 개수 입력
    board = vector<vector<int>>(n, vector<int>(n, 0));  // 보드 초기화

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        board[x-1][y-1] = 1;  // 사과 위치 설정
    }

    int l;
    cin >> l;  // 방향 전환 횟수 입력
    for (int i = 0; i < l; i++) {
        int x;
        char c;
        cin >> x >> c;
        changes[x] = c;  // 방향 전환 정보 저장
    }

    cout << simulate() << endl;  // 게임 종료 시간 출력
    return 0;
}
