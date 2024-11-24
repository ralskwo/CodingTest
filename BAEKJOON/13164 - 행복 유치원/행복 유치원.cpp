#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minimum_cost(int N, int K, vector<int>& heights) {
    // 인접한 키 차이를 저장할 벡터
    vector<int> differences(N - 1);
    
    // 인접한 키 차이를 계산하여 differences 벡터에 저장
    for (int i = 0; i < N - 1; ++i) {
        differences[i] = heights[i + 1] - heights[i];
    }
    
    // 키 차이를 내림차순으로 정렬
    sort(differences.rbegin(), differences.rend());
    
    // K-1개의 큰 차이를 제거한 뒤 나머지 합을 계산
    int total_cost = 0;
    for (int i = K - 1; i < differences.size(); ++i) {
        total_cost += differences[i];
    }
    
    // 최소 비용 반환
    return total_cost;
}

int main() {
    // 원생 수 N과 조의 개수 K 입력
    int N, K;
    cin >> N >> K;
    
    // 원생들의 키를 저장할 벡터 heights
    vector<int> heights(N);
    for (int i = 0; i < N; ++i) {
        cin >> heights[i];
    }
    
    // 최소 비용 계산 및 출력
    cout << minimum_cost(N, K, heights) << endl;
    return 0;
}
