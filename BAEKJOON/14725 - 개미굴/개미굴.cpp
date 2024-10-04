#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

// 트리 노드를 정의하는 클래스
class TrieNode {
public:
    map<string, TrieNode*> children;  // 자식 노드를 저장하는 map
};

// 트리를 깊이 우선 탐색(DFS)으로 출력하는 함수
void printTrie(TrieNode* node, int depth) {
    // 자식 노드를 사전 순서대로 출력하기 위해 map의 key를 순회
    for (auto it = node->children.begin(); it != node->children.end(); ++it) {
        // depth만큼 "--" 출력 후, 현재 노드의 key(먹이 이름) 출력
        for (int i = 0; i < depth; ++i) {
            cout << "--";
        }
        cout << it->first << endl;
        // 자식 노드를 깊이 우선 탐색으로 재귀 호출하여 출력
        printTrie(it->second, depth + 1);
    }
}

int main() {
    int N;  // 입력 개수 N
    cin >> N;  // N 입력 받기

    TrieNode* root = new TrieNode();  // 트리의 루트 노드 생성

    // N번 반복하여 각 로봇 개미의 경로 정보를 입력 받음
    for (int i = 0; i < N; ++i) {
        int K;  // 각 로봇 개미의 경로에 포함된 방의 개수 K
        cin >> K;

        TrieNode* currentNode = root;  // 루트 노드부터 시작
        for (int j = 0; j < K; ++j) {
            string food;  // 먹이 정보 저장
            cin >> food;

            // 현재 노드의 자식 중에 해당 먹이 정보가 없으면 새 노드 생성
            if (currentNode->children.find(food) == currentNode->children.end()) {
                currentNode->children[food] = new TrieNode();
            }

            // 해당 자식 노드로 이동
            currentNode = currentNode->children[food];
        }
    }

    // 루트 노드부터 깊이 0으로 시작하여 트리를 출력
    printTrie(root, 0);

    return 0;
}
