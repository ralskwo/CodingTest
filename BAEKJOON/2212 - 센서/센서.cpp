#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 최소 수신 가능 거리의 합을 계산하는 함수
int min_total_distance(int N, int K, vector<int> sensors) {
    // 집중국의 수가 센서의 수 이상인 경우, 모든 센서를 개별적으로 커버 가능
    if (K >= N) return 0;

    // 센서 좌표를 오름차순으로 정렬
    sort(sensors.begin(), sensors.end());

    // 인접 센서 간의 거리를 저장할 벡터
    vector<int> distances;
    for (int i = 1; i < N; i++) {
        // 센서 간 거리 계산
        distances.push_back(sensors[i] - sensors[i - 1]);
    }

    // 거리 벡터를 내림차순으로 정렬
    sort(distances.rbegin(), distances.rend());

    // 가장 큰 K-1 개의 간격을 제거
    for (int i = 0; i < K - 1; i++) {
        distances[i] = 0; // 큰 간격 제거
    }

    // 남은 거리의 합을 계산
    int result = 0;
    for (int distance : distances) {
        result += distance;
    }
    return result;
}

int main() {
    // 입력 처리
    int N, K;
    cin >> N >> K;

    vector<int> sensors(N);
    for (int i = 0; i < N; i++) {
        cin >> sensors[i];
    }

    // 최소 거리 합 계산 및 출력
    cout << min_total_distance(N, K, sensors) << endl;
    return 0;
}