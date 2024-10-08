#include <iostream>
#include <vector>
using namespace std;

// 세그먼트 트리 클래스 정의
class SegmentTree {
public:
    int size;            // 세그먼트 트리의 크기
    vector<int> tree;    // 세그먼트 트리를 저장할 벡터

    // 세그먼트 트리 초기화
    SegmentTree(int n) {
        size = 1;
        // 트리 크기를 n 이상인 가장 가까운 2의 제곱수로 설정
        while (size < n) size *= 2;
        // 트리 크기만큼 0으로 초기화
        tree.assign(2 * size, 0);
    }

    // 주어진 배열을 세그먼트 트리에 빌드
    void build(const vector<int>& arr) {
        // 리프 노드에 입력 배열의 값을 채움
        for (int i = 0; i < arr.size(); i++) {
            tree[size + i] = arr[i];
        }
        // 부모 노드들을 초기화
        for (int i = size - 1; i > 0; i--) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    // 특정 인덱스의 값을 value만큼 업데이트
    void update(int index, int value) {
        // 리프 노드의 위치로 이동
        index += size;
        // 값을 더하거나 뺌
        tree[index] += value;
        // 부모 노드로 거슬러 올라가면서 값 갱신
        while (index > 1) {
            index /= 2; // 부모 노드로 이동
            tree[index] = tree[2 * index] + tree[2 * index + 1]; // 자식 노드의 합으로 갱신
        }
    }

    // 특정 군번이 속한 부대를 찾는 함수
    int query(int soldier) {
        if (soldier > tree[1]) return -1; // 주어진 군번이 전체 군인의 수를 초과하면 -1 반환
        int index = 1; // 루트 노드에서 시작
        while (index < size) {
            if (soldier <= tree[2 * index]) {
                index = 2 * index; // 왼쪽 자식으로 이동
            } else {
                soldier -= tree[2 * index]; // 왼쪽 자식 노드의 군사 수를 빼고
                index = 2 * index + 1; // 오른쪽 자식으로 이동
            }
        }
        return index - size + 1; // 부대 번호 반환
    }
};

int main() {
    int n, m;
    cin >> n; // 부대의 개수 입력
    vector<int> soldiers(n); // 부대의 군사 수를 저장할 벡터

    // 각 부대의 군사 수 입력
    for (int i = 0; i < n; i++) {
        cin >> soldiers[i];
    }

    // 세그먼트 트리 생성 및 초기화
    SegmentTree segTree(n);
    segTree.build(soldiers);

    // 명령의 개수 입력
    cin >> m;
    for (int i = 0; i < m; i++) {
        int cmd;
        cin >> cmd;
        if (cmd == 1) {
            // "1 i a" 명령 처리
            int index, value;
            cin >> index >> value;
            segTree.update(index - 1, value); // 0-based 인덱스로 변환하여 업데이트
        } else if (cmd == 2) {
            // "2 i" 명령 처리
            int soldier;
            cin >> soldier;
            cout << segTree.query(soldier) << endl; // 군번이 속한 부대 번호 출력
        }
    }

    return 0;
}
