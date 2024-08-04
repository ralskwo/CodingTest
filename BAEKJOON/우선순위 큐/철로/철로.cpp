#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int max_people_in_segment(int n, vector<pair<int, int>> positions, int d) {
    // 각 사람의 집과 사무실 위치에서 시작점과 끝점을 계산
    vector<pair<int, int>> segments;
    for (auto& pos : positions) {
        int start = min(pos.first, pos.second);
        int end = max(pos.first, pos.second);
        segments.push_back({start, end});
    }

    // 끝점을 기준으로 정렬
    sort(segments.begin(), segments.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;
    });

    int max_count = 0;  // 최대 사람 수를 저장할 변수 초기화
    priority_queue<int, vector<int>, greater<int>> pq;  // 우선순위 큐 초기화 (min-heap)

    for (auto& seg : segments) {
        int start = seg.first;
        int end = seg.second;

        // 현재 사람의 시작점을 우선순위 큐에 삽입
        pq.push(start);

        // 우선순위 큐의 첫 번째 요소가 현재 끝점에서 d를 뺀 값보다 작으면 큐에서 제거
        while (!pq.empty() && pq.top() < end - d) {
            pq.pop();
        }

        // 현재 우선순위 큐의 크기를 최대 사람 수와 비교하여 갱신
        max_count = max(max_count, (int)pq.size());
    }

    return max_count;  // 최대 사람 수 반환
}

int main() {
    int n;
    cin >> n;  // 첫 번째 줄에서 사람 수를 입력 받음

    vector<pair<int, int>> positions(n);
    for (int i = 0; i < n; i++) {
        cin >> positions[i].first >> positions[i].second;  // 각 사람의 집과 사무실 위치를 입력 받음
    }

    int d;
    cin >> d;  // 마지막 줄에서 선분의 길이를 입력 받음

    // 최대 사람 수를 계산하여 출력
    cout << max_people_in_segment(n, positions, d) << endl;

    return 0;
}
