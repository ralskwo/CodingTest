#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

// 상어의 정보를 담는 구조체
struct Shark {
    int speed, direction, size;
};

// 상하좌우 이동을 위한 방향 배열 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, 1, -1};

int R, C, M; // 격자판의 크기와 상어의 수
map<pair<int, int>, Shark> sharks; // 상어들의 위치와 정보를 저장할 맵

// 상어 이동 함수
void moveSharks() {
    map<pair<int, int>, Shark> newSharks; // 이동 후 상어를 저장할 맵

    // 모든 상어에 대해 이동 처리
    for (auto& entry : sharks) {
        int r = entry.first.first;
        int c = entry.first.second;
        Shark shark = entry.second;

        int speed = shark.speed;
        int direction = shark.direction;
        int size = shark.size;

        int nr = r, nc = c;

        // 위, 아래 이동일 때
        if (direction == 1 || direction == 2) {
            speed %= (R - 1) * 2; // 주기성을 이용한 속도 감소
            for (int i = 0; i < speed; ++i) {
                if (nr == 0 && direction == 1) direction = 2;
                else if (nr == R - 1 && direction == 2) direction = 1;
                nr += dr[direction - 1];
            }
        } 
        // 좌, 우 이동일 때
        else {
            speed %= (C - 1) * 2; // 주기성을 이용한 속도 감소
            for (int i = 0; i < speed; ++i) {
                if (nc == 0 && direction == 4) direction = 3;
                else if (nc == C - 1 && direction == 3) direction = 4;
                nc += dc[direction - 1];
            }
        }

        // 이동 후 상어 위치 처리
        if (newSharks.find({nr, nc}) != newSharks.end()) {
            if (newSharks[{nr, nc}].size < size) {
                newSharks[{nr, nc}] = {speed, direction, size};
            }
        } else {
            newSharks[{nr, nc}] = {speed, direction, size};
        }
    }

    sharks = newSharks; // 상어 상태 업데이트
}

int main() {
    cin >> R >> C >> M;

    // 상어 정보 입력 받기
    for (int i = 0; i < M; ++i) {
        int r, c, s, d, z;
        cin >> r >> c >> s >> d >> z;
        sharks[{r - 1, c - 1}] = {s, d, z}; // 0-based로 저장
    }

    int totalSize = 0;

    // 낚시왕이 1번 열부터 마지막 열까지 이동
    for (int kingPos = 0; kingPos < C; ++kingPos) {
        // 해당 열에서 가장 가까운 상어를 잡는다.
        for (int row = 0; row < R; ++row) {
            if (sharks.find({row, kingPos}) != sharks.end()) {
                totalSize += sharks[{row, kingPos}].size; // 상어 크기 합산
                sharks.erase({row, kingPos}); // 상어 삭제
                break;
            }
        }

        // 상어 이동
        moveSharks();
    }

    cout << totalSize << endl; // 결과 출력
    return 0;
}
