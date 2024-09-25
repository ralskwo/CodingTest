#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n; // 수업의 개수 입력

    vector<pair<int, int>> classes(n); // 수업의 시작 시간과 종료 시간을 저장할 벡터
    
    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end; // 각 수업의 시작 시간과 종료 시간 입력
        classes[i] = {start, end}; // 시작 시간과 종료 시간 쌍을 벡터에 저장
    }

    // 수업을 시작 시간 기준으로 정렬
    sort(classes.begin(), classes.end());

    // 최소 힙(우선순위 큐)을 사용하여 종료 시간을 추적
    priority_queue<int, vector<int>, greater<int>> pq;

    // 첫 번째 수업의 종료 시간을 힙에 넣음
    pq.push(classes[0].second);

    for (int i = 1; i < n; i++) {
        // 가장 빨리 끝나는 수업의 종료 시간과 현재 수업의 시작 시간을 비교
        if (pq.top() <= classes[i].first) {
            pq.pop(); // 수업이 끝났으므로 힙에서 제거
        }
        pq.push(classes[i].second); // 새로운 수업의 종료 시간을 힙에 추가
    }

    // 힙의 크기가 필요한 최소 강의실 수
    cout << pq.size() << endl;

    return 0;
}
