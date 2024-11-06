#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>  // sqrt와 pow 함수 사용을 위한 라이브러리
using namespace std;

// 특정 점이 행성계 내부에 있는지 판단하는 함수
bool isInsideCircle(int x, int y, int cx, int cy, int r) {
    // 두 점 사이의 거리의 제곱이 반지름의 제곱보다 작은지 확인
    return (x - cx) * (x - cx) + (y - cy) * (y - cy) < r * r;
}

// 최소 진입/이탈 횟수를 계산하는 함수
int minimumPlanetEntryExitCount(int x1, int y1, int x2, int y2, const vector<tuple<int, int, int>>& planets) {
    int count = 0;  // 진입/이탈 횟수를 저장할 변수
    for (const auto& planet : planets) {  // 각 행성계에 대해 반복
        int cx, cy, r;
        tie(cx, cy, r) = planet;  // 행성계의 중심 좌표와 반지름을 추출

        // 출발점과 도착점이 각각 행성계 내부에 있는지 확인
        bool startInside = isInsideCircle(x1, y1, cx, cy, r);
        bool endInside = isInsideCircle(x2, y2, cx, cy, r);

        // 출발점과 도착점 중 하나만 내부에 있는 경우 진입/이탈 발생
        if (startInside != endInside) {
            count++;
        }
    }
    return count;  // 최종 진입/이탈 횟수 반환
}

int main() {
    int T;  // 테스트 케이스의 개수
    cin >> T;
    vector<int> results;  // 결과를 저장할 벡터

    while (T--) {  // 각 테스트 케이스에 대해 반복
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;  // 출발점과 도착점 입력

        int n;  // 행성계의 개수
        cin >> n;
        vector<tuple<int, int, int>> planets;  // 각 행성계의 정보를 저장할 벡터

        for (int i = 0; i < n; ++i) {
            int cx, cy, r;
            cin >> cx >> cy >> r;  // 행성계의 중심 좌표와 반지름 입력
            planets.push_back(make_tuple(cx, cy, r));  // 벡터에 행성계 추가
        }

        // 최소 진입/이탈 횟수를 계산하고 결과에 추가
        results.push_back(minimumPlanetEntryExitCount(x1, y1, x2, y2, planets));
    }

    for (const int& result : results) {
        cout << result << endl;  // 각 테스트 케이스의 결과 출력
    }

    return 0;
}
