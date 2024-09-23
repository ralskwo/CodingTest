#include <iostream>  // 입출력 처리
#include <vector>    // 벡터 자료형 사용
#include <queue>     // 우선순위 큐 사용
#include <algorithm> // min 함수 사용

using namespace std;

struct Shortcut {
    int start, end, length;  // 지름길의 시작점, 끝점, 지름길 길이
};

int main() {
    int N, D;  // N은 지름길의 개수, D는 고속도로의 길이
    cin >> N >> D;  // N과 D 입력받기

    vector<Shortcut> shortcuts(N);  // N개의 지름길 정보를 저장할 벡터
    for (int i = 0; i < N; ++i) {
        cin >> shortcuts[i].start >> shortcuts[i].end >> shortcuts[i].length;  // 각 지름길의 시작점, 끝점, 길이 입력받기
    }

    vector<int> dist(D + 1, D);  // 거리 배열을 고속도로 길이 D로 초기화 (최댓값은 직선으로 이동한 거리)
    dist[0] = 0;  // 시작점 0의 거리는 0으로 설정

    for (int i = 0; i <= D; ++i) {
        // 한 칸씩 직선 이동하는 경우를 먼저 처리
        if (i > 0) {
            dist[i] = min(dist[i], dist[i - 1] + 1);  // 직선으로 한 칸씩 이동하는 최소 거리 갱신
        }

        // 지름길을 사용하는 경우 처리
        for (const auto& shortcut : shortcuts) {
            if (shortcut.start == i && shortcut.end <= D) {
                dist[shortcut.end] = min(dist[shortcut.end], dist[i] + shortcut.length);  // 지름길을 이용한 이동 거리 갱신
            }
        }
    }

    cout << dist[D] << endl;  // 최종적으로 D 지점까지의 최소 거리를 출력
    return 0;
}
