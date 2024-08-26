#include <iostream>  // 표준 입출력 사용
#include <vector>    // 벡터 자료구조 사용

using namespace std;

class SegmentTree {
private:
    vector<int> tree;  // 세그먼트 트리를 저장할 벡터
    int size;          // 트리의 크기 (사탕 맛 번호 범위)

    // 트리 업데이트 함수
    void update(int idx, int diff, int node, int nodeLeft, int nodeRight) {
        if (idx < nodeLeft || nodeRight < idx) {  // 업데이트할 인덱스가 범위 밖이면 종료
            return;
        }
        tree[node] += diff;  // 현재 노드에 diff를 더함 (사탕 개수 반영)
        if (nodeLeft != nodeRight) {  // 리프 노드가 아니면 자식 노드로 재귀 호출
            int mid = (nodeLeft + nodeRight) / 2;  // 중간 지점 계산
            update(idx, diff, 2 * node, nodeLeft, mid);        // 왼쪽 자식 노드 업데이트
            update(idx, diff, 2 * node + 1, mid + 1, nodeRight); // 오른쪽 자식 노드 업데이트
        }
    }

    // k번째 사탕의 맛 번호를 찾는 함수
    int query(int k, int node, int nodeLeft, int nodeRight) {
        if (nodeLeft == nodeRight) {  // 리프 노드에 도달한 경우
            return nodeLeft;  // 해당 노드의 인덱스 반환 (사탕 맛 번호)
        }
        int mid = (nodeLeft + nodeRight) / 2;  // 중간 지점 계산
        if (k <= tree[2 * node]) {  // k번째 사탕이 왼쪽 자식 노드에 있는 경우
            return query(k, 2 * node, nodeLeft, mid);  // 왼쪽 자식 노드로 이동
        } else {  // k번째 사탕이 오른쪽 자식 노드에 있는 경우
            return query(k - tree[2 * node], 2 * node + 1, mid + 1, nodeRight);  // 오른쪽 자식 노드로 이동
        }
    }

public:
    SegmentTree(int n) : size(n) {  // 세그먼트 트리 생성자
        tree.resize(4 * n, 0);  // 트리 크기 설정 및 초기화 (0으로 초기화)
    }

    // 사탕 개수를 추가하거나 제거하는 함수
    void add(int idx, int diff) {
        update(idx, diff, 1, 1, size);  // 루트 노드부터 시작하여 트리 업데이트
    }

    // k번째 사탕의 맛 번호를 찾는 함수
    int findKth(int k) {
        return query(k, 1, 1, size);  // 루트 노드부터 시작하여 k번째 사탕 찾기
    }
};

int main() {
    ios::sync_with_stdio(false);  // 입출력 속도 향상을 위한 설정
    cin.tie(nullptr);  // 입출력 동기화를 해제하여 속도 향상

    int n;  // 수정이가 사탕상자에 손을 댄 횟수
    cin >> n;

    SegmentTree segTree(1000000);  // 맛 번호의 최대값 1000000을 갖는 세그먼트 트리 생성

    for (int i = 0; i < n; ++i) {  // n개의 명령어 처리
        int a;  // 명령어 타입 (1: 사탕 꺼내기, 2: 사탕 추가/제거)
        cin >> a;
        if (a == 1) {  // 사탕 꺼내기 명령어 처리
            int b;  // 꺼낼 사탕의 순위
            cin >> b;
            int taste = segTree.findKth(b);  // b번째 사탕의 맛 번호 찾기
            cout << taste << "\n";  // 결과 출력
            segTree.add(taste, -1);  // 해당 맛의 사탕 1개 제거
        } else if (a == 2) {  // 사탕 추가/제거 명령어 처리
            int b, c;  // b: 사탕 맛 번호, c: 사탕 개수 (음수일 경우 제거)
            cin >> b >> c;
            segTree.add(b, c);  // 사탕 개수 업데이트
        }
    }

    return 0;  // 프로그램 종료
}
