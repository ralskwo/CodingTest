#include <iostream>
using namespace std;

// 세 점의 좌표를 받아 방향을 계산하는 함수
int find_direction(int x1, int y1, int x2, int y2, int x3, int y3) {
    // 벡터 P1P2와 P2P3의 외적을 계산
    int cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2);

    // 외적 결과에 따라 방향을 판별
    if (cross_product > 0)
        return 1;  // 반시계 방향
    else if (cross_product < 0)
        return -1; // 시계 방향
    else
        return 0;  // 일직선
}

int main() {
    // 첫 번째 점의 좌표를 입력받기
    int x1, y1;
    cin >> x1 >> y1;

    // 두 번째 점의 좌표를 입력받기
    int x2, y2;
    cin >> x2 >> y2;

    // 세 번째 점의 좌표를 입력받기
    int x3, y3;
    cin >> x3 >> y3;

    // 방향을 계산하고 출력하기
    cout << find_direction(x1, y1, x2, y2, x3, y3) << endl;

    return 0;  // 프로그램 정상 종료
}
