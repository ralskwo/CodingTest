#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 박스 정보를 저장하기 위한 구조체 정의
struct Box {
    int start, end, num;
};

// 트럭 한 대로 배송할 수 있는 최대 박스 수를 계산하는 함수
int maxBoxesDelivered(int n, int c, vector<Box>& boxes) {
    // 받는 마을 번호를 기준으로 오름차순 정렬
    sort(boxes.begin(), boxes.end(), [](const Box& a, const Box& b) {
        return a.end < b.end;
    });

    // 각 마을에서 트럭 적재 상태를 저장하는 배열
    vector<int> deliveries(n + 1, 0);

    int totalDelivered = 0; // 최종 배송된 박스 수

    // 각 박스 정보를 순회
    for (const auto& box : boxes) {
        // 현재 구간에서 트럭 적재 가능한 최대 박스 수 계산
        int maxCapacity = c;
        for (int i = box.start; i < box.end; i++) {
            maxCapacity = min(maxCapacity, c - deliveries[i]);
        }
        maxCapacity = min(maxCapacity, box.num);

        // 구간 내 각 마을에 적재 상황 업데이트
        for (int i = box.start; i < box.end; i++) {
            deliveries[i] += maxCapacity;
        }

        // 누적 배송된 박스 수 갱신
        totalDelivered += maxCapacity;
    }

    return totalDelivered; // 최종 배송된 박스 수 반환
}

int main() {
    int n, c, m; // 마을 수, 트럭 용량, 박스 정보 개수
    cin >> n >> c;
    cin >> m;

    vector<Box> boxes(m); // 박스 정보를 저장할 벡터
    for (int i = 0; i < m; i++) {
        cin >> boxes[i].start >> boxes[i].end >> boxes[i].num;
    }

    // 결과 출력
    cout << maxBoxesDelivered(n, c, boxes) << endl;
    return 0;
}
