#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

// 특정 노드의 최상위 부모 노드를 찾는 함수 (경로 압축 기법 적용)
int findParent(vector<int>& parent, int x) {
    if (parent[x] != x) {  // 현재 노드가 자기 자신을 부모로 가지고 있지 않으면
        parent[x] = findParent(parent, parent[x]);  // 부모 노드를 재귀적으로 찾아 최상위 부모로 업데이트
    }
    return parent[x];  // 최상위 부모 노드 반환
}

// 두 노드를 같은 그룹으로 합치는 함수
void unionNodes(vector<int>& parent, int a, int b) {
    int rootA = findParent(parent, a);  // a의 최상위 부모 노드 찾기
    int rootB = findParent(parent, b);  // b의 최상위 부모 노드 찾기
    if (rootA != rootB) {  // 부모 노드가 다르면 (다른 그룹에 속해 있으면)
        parent[rootB] = rootA;  // b의 부모를 a의 부모로 설정하여 두 그룹을 합침
    }
}

int main() {
    int N, M;  // N: 도시의 수, M: 여행 계획에 포함된 도시의 수

    // 도시의 수와 여행 계획에 포함된 도시의 수 입력 받기
    cin >> N >> M;

    vector<int> parent(N + 1);  // 각 도시의 부모 노드를 저장하는 배열 (1부터 N까지 사용)

    // 각 도시의 부모를 자기 자신으로 초기화
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
    }

    // 인접 행렬을 통해 도시 간의 연결 정보 입력 받기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int connection;
            cin >> connection;  // 도시 i와 도시 j의 연결 정보 입력 (0 또는 1)
            if (connection == 1) {  // 두 도시가 연결되어 있으면
                unionNodes(parent, i, j);  // 두 도시를 같은 그룹으로 합침
            }
        }
    }

    // 여행 계획 입력 받기
    vector<int> plan(M);
    for (int i = 0; i < M; i++) {
        cin >> plan[i];  // 여행 계획에 포함된 도시 입력
    }

    // 여행 계획의 첫 번째 도시의 최상위 부모를 기준으로 설정
    int root = findParent(parent, plan[0]);
    bool possible = true;

    // 여행 계획에 포함된 모든 도시가 같은 그룹에 속하는지 확인
    for (int i = 1; i < M; i++) {
        if (findParent(parent, plan[i]) != root) {  // 같은 그룹에 속하지 않는 도시가 있다면
            possible = false;  // 여행 계획이 불가능하므로 false로 설정
            break;  // 반복문 종료
        }
    }

    // 결과 출력
    if (possible) {
        cout << "YES" << endl;  // 여행 계획이 가능하면 YES 출력
    } else {
        cout << "NO" << endl;  // 여행 계획이 불가능하면 NO 출력
    }

    return 0;
}
