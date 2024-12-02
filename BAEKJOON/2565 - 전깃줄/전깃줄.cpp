#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 이분 탐색을 사용해 LIS에서 적절한 위치를 찾는 함수
int binarySearch(vector<int>& dp, int target) {
    int low = 0, high = dp.size();
    while (low < high) {
        int mid = (low + high) / 2;
        if (dp[mid] < target)
            low = mid + 1;  // target보다 작은 값은 제외
        else
            high = mid;     // target 이상인 값으로 범위를 좁힘
    }
    return low; // target이 들어갈 위치 반환
}

int main() {
    int n;
    cin >> n; // 전깃줄의 개수를 입력받음

    vector<pair<int, int>> connections(n);
    for (int i = 0; i < n; ++i) {
        cin >> connections[i].first >> connections[i].second; // A, B 전봇대의 연결 정보 입력
    }

    sort(connections.begin(), connections.end()); // A 전봇대 기준으로 정렬

    vector<int> dp; // LIS를 저장하기 위한 배열
    for (const auto& conn : connections) {
        int b = conn.second; // B 전봇대의 연결 위치
        int idx = binarySearch(dp, b); // LIS에서 b가 들어갈 위치 찾기
        if (idx == dp.size())
            dp.push_back(b); // LIS 끝에 추가
        else
            dp[idx] = b;     // 기존 값을 갱신
    }

    cout << n - dp.size() << endl; // 제거해야 하는 전깃줄의 최소 개수 출력
    return 0;
}
