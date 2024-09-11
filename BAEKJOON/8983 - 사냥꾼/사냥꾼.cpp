#include <iostream>  // 입출력 처리를 위한 헤더
#include <vector>    // 동적 배열 사용을 위한 헤더
#include <algorithm> // 정렬과 이분 탐색을 위한 헤더
#include <cmath>     // abs 함수 사용을 위한 헤더

using namespace std;

int count_catchable_animals(int m, int n, int l, vector<int>& shooting_spots, vector<pair<int, int>>& animals) {
    sort(shooting_spots.begin(), shooting_spots.end());  // 사대 위치를 오름차순으로 정렬
    int catchable_count = 0;  // 잡을 수 있는 동물 수를 저장할 변수

    for (auto& animal : animals) {  // 모든 동물에 대해 반복
        int x = animal.first;  // 동물의 x 좌표
        int y = animal.second; // 동물의 y 좌표

        if (y > l) {  // y 좌표가 사정거리보다 크면 잡을 수 없음
            continue; // 이 동물은 건너뜀
        }

        // 이분 탐색으로 사대의 위치 중 동물의 x 좌표에 가장 가까운 사대를 찾음
        auto it = lower_bound(shooting_spots.begin(), shooting_spots.end(), x); 

        bool is_catchable = false;  // 해당 동물이 잡힐 수 있는지 여부

        // 가장 가까운 사대와의 거리가 유효한지 확인
        if (it != shooting_spots.end()) {
            if (abs(*it - x) + y <= l) {  // 찾은 사대와의 거리가 사정거리 이내인지 확인
                is_catchable = true;  // 잡을 수 있는 동물
            }
        }

        // 바로 이전 사대와의 거리도 확인
        if (it != shooting_spots.begin()) {
            --it;
            if (abs(*it - x) + y <= l) {  // 이전 사대와의 거리 확인
                is_catchable = true;  // 잡을 수 있는 동물
            }
        }

        if (is_catchable) {
            catchable_count++;  // 잡을 수 있는 동물의 수를 증가
        }
    }

    return catchable_count;  // 결과 반환
}

int main() {
    int m, n, l;
    cin >> m >> n >> l;  // 사대 수, 동물 수, 사정거리 입력
    vector<int> shooting_spots(m);  // 사대 위치를 저장할 벡터
    for (int i = 0; i < m; ++i) {
        cin >> shooting_spots[i];  // 사대 위치 입력
    }

    vector<pair<int, int>> animals(n);  // 동물 위치를 저장할 벡터
    for (int i = 0; i < n; ++i) {
        cin >> animals[i].first >> animals[i].second;  // 동물 위치 입력
    }

    int result = count_catchable_animals(m, n, l, shooting_spots, animals);  // 결과 계산
    cout << result << endl;  // 결과 출력

    return 0;
}
