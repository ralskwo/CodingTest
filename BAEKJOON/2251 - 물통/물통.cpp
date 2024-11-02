#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>
#include <algorithm>

using namespace std;

// 물을 옮기는 함수
pair<int, int> pour(int x, int y, int max_y) {
    if (x + y > max_y)  // 목표 물통이 가득 차는 경우
        return {x + y - max_y, max_y};  // 넘치는 양만큼 출발 물통에 남기고 목표 물통은 가득 채웁니다.
    else
        return {0, x + y};  // 그렇지 않으면 출발 물통을 비우고 목표 물통을 채웁니다.
}

// 가능한 물의 양 계산 함수
vector<int> possibleAmounts(int A, int B, int C) {
    set<tuple<int, int, int>> visited;  // 방문한 상태를 저장하는 집합
    set<int> result;  // 첫 번째 물통이 비어 있을 때 세 번째 물통의 물의 양을 저장하는 집합
    queue<tuple<int, int, int>> q;  // BFS 탐색을 위한 큐

    q.push({0, 0, C});  // 초기 상태 (0, 0, C)를 큐에 추가합니다.

    while (!q.empty()) {
        int a, b, c;
        tie(a, b, c) = q.front();
        q.pop();

        if (a == 0)  // 첫 번째 물통이 비어 있을 때
            result.insert(c);  // 세 번째 물통의 물의 양을 결과에 추가합니다.

        if (visited.count({a, b, c}))  // 이미 방문한 상태라면
            continue;  // 다음 상태로 넘어갑니다.
        visited.insert({a, b, c});  // 현재 상태를 방문 처리합니다.

        // 여섯 가지 물 옮기기 경우에 대해 BFS 큐에 추가
        int na, nb, nc;

        tie(na, nb) = pour(a, b, B);  // A → B
        q.push({na, nb, c});

        tie(na, nc) = pour(a, c, C);  // A → C
        q.push({na, b, nc});

        tie(nb, na) = pour(b, a, A);  // B → A
        q.push({na, nb, c});

        tie(nb, nc) = pour(b, c, C);  // B → C
        q.push({a, nb, nc});

        tie(nc, na) = pour(c, a, A);  // C → A
        q.push({na, b, nc});

        tie(nc, nb) = pour(c, b, B);  // C → B
        q.push({a, nb, nc});
    }

    vector<int> sorted_result(result.begin(), result.end());  // 결과를 벡터로 변환
    sort(sorted_result.begin(), sorted_result.end());  // 오름차순 정렬
    return sorted_result;
}

int main() {
    int A, B, C;
    cin >> A >> B >> C;  // 입력 받기
    vector<int> result = possibleAmounts(A, B, C);  // 결과 계산

    for (int amount : result)  // 결과 출력
        cout << amount << " ";
    cout << endl;

    return 0;
}