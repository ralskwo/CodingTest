#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 우체국 최적 위치를 찾는 함수 정의 (마을 개수와 마을 정보를 입력받음)
int findPostOfficeLocation(int N, vector<pair<int, int>>& villages) {
    // 마을들을 x 좌표 기준으로 정렬
    sort(villages.begin(), villages.end());

    // 전체 마을 인구 계산
    long long total_population = 0;
    for (const auto& village : villages) {
        total_population += village.second;
    }

    // 현재까지의 누적 인구 초기화
    long long current_population = 0;

    // 정렬된 마을 리스트를 순회
    for (const auto& village : villages) {
        // 현재 마을의 인구를 누적 인구에 추가
        current_population += village.second;

        // 누적 인구가 전체 인구의 절반 이상이 되면
        if (current_population >= (total_population + 1) / 2) {
            // 해당 마을의 x 좌표를 우체국 위치로 반환
            return village.first;
        }
    }

    // 예외적인 경우 첫 번째 마을의 위치 반환
    return villages[0].first;
}

int main() {
    // 마을의 개수 입력
    int N;
    cin >> N;

    // 마을 정보를 저장할 벡터 초기화
    vector<pair<int, int>> villages(N);

    // N개의 마을 정보 입력 받기 (x 좌표와 인구)
    for (int i = 0; i < N; ++i) {
        cin >> villages[i].first >> villages[i].second;
    }

    // 우체국 최적 위치 계산 및 출력
    cout << findPostOfficeLocation(N, villages) << endl;

    return 0;
}
