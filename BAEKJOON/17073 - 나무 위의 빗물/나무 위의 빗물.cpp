#include <iostream>
#include <vector>
#include <iomanip>
#include <unordered_map>
using namespace std;

int main() {
    // 트리의 노드 수와 1번 노드에 고인 물의 양을 저장할 변수
    int N;
    double W;
    cin >> N >> W;
    
    // 트리의 인접 리스트를 저장할 벡터 배열
    unordered_map<int, vector<int>> tree;
    
    // 간선 정보 입력
    for (int i = 0; i < N - 1; i++) {
        int U, V;
        cin >> U >> V;
        tree[U].push_back(V); // U에 V 연결
        tree[V].push_back(U); // V에 U 연결
    }
    
    // 리프 노드 개수를 저장할 변수
    int leaf_count = 0;
    
    // 2번 노드부터 N번 노드까지 확인하여 리프 노드인지 판단
    for (int node = 2; node <= N; node++) {
        if (tree[node].size() == 1) { // 연결된 노드가 하나라면 리프 노드
            leaf_count++;
        }
    }
    
    // 리프 노드에 고인 물의 양 계산
    double result = W / leaf_count;
    
    // 결과 출력, 소수점 10자리까지
    cout << fixed << setprecision(10) << result << endl;

    return 0;
}
