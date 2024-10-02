#include <iostream>  // 입출력 처리를 위해 필요
#include <vector>    // 벡터 자료구조를 사용하기 위해 필요
#include <algorithm> // 정렬 함수 사용을 위해 필요
#include <queue>     // 우선순위 큐를 사용하기 위해 필요

using namespace std;

int main() {
    int n;  // 문제의 개수를 저장할 변수
    cin >> n;  // 문제의 개수 입력받기

    vector<pair<int, int>> problems(n);  // 문제의 데드라인과 컵라면 수를 저장할 벡터

    // 각 문제의 데드라인과 컵라면 수 입력 받기
    for (int i = 0; i < n; i++) {
        cin >> problems[i].first >> problems[i].second;
    }

    // 문제를 데드라인 기준으로 정렬
    sort(problems.begin(), problems.end());

    priority_queue<int, vector<int>, greater<int>> ramenHeap;  // 최소 힙 (우선순위 큐) 생성

    // 문제를 하나씩 처리
    for (auto& problem : problems) {
        int deadline = problem.first;  // 문제의 데드라인
        int ramen = problem.second;    // 문제를 풀었을 때 받을 수 있는 컵라면 수

        // 현재 문제를 최소 힙에 추가
        ramenHeap.push(ramen);

        // 힙의 크기가 데드라인을 초과하면 가장 작은 컵라면 수 제거
        if (ramenHeap.size() > deadline) {
            ramenHeap.pop();  // 가장 적은 컵라면 수 제거
        }
    }

    // 남아있는 컵라면 수 모두 더하기
    int totalRamen = 0;
    while (!ramenHeap.empty()) {
        totalRamen += ramenHeap.top();  // 힙의 가장 위(최소값) 요소를 더함
        ramenHeap.pop();  // 더한 요소 제거
    }

    cout << totalRamen << endl;  // 최종 컵라면 수 출력
    return 0;
}
