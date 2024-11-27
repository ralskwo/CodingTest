#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    // 강의 개수 입력
    int N;
    cin >> N;

    // 강의 정보를 저장할 벡터 선언
    vector<pair<int, int>> lectures;

    // 강의 정보를 입력받아 벡터에 저장
    for (int i = 0; i < N; ++i) {
        int num, start, end;
        cin >> num >> start >> end;
        lectures.emplace_back(start, end); // (시작 시간, 종료 시간) 저장
    }

    // 강의 시작 시간을 기준으로 정렬
    sort(lectures.begin(), lectures.end());

    // 최소 강의실을 관리할 우선순위 큐 생성 (종료 시간 관리)
    priority_queue<int, vector<int>, greater<int>> minHeap;

    // 강의 정보를 순회하며 강의실 배정
    for (const auto& lecture : lectures) {
        int start = lecture.first;
        int end = lecture.second;

        // 현재 강의 시작 시간이 가장 빨리 끝나는 강의실의 종료 시간 이후라면
        if (!minHeap.empty() && minHeap.top() <= start) {
            minHeap.pop(); // 해당 강의실 재사용 가능하므로 종료 시간 제거
        }

        // 현재 강의의 종료 시간을 우선순위 큐에 추가
        minHeap.push(end);
    }

    // 최종적으로 우선순위 큐에 남아 있는 요소의 개수가 필요한 최소 강의실 개수
    cout << minHeap.size() << endl;

    return 0;
}
