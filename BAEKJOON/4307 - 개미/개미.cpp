#include <iostream>
#include <vector>
#include <algorithm> // for max and min functions
using namespace std;

pair<int, int> ant_times(int l, const vector<int>& positions) {
    int min_time = 0; // 최소 시간을 저장할 변수
    int max_time = 0; // 최대 시간을 저장할 변수
    
    for (int position : positions) { // 각 개미의 위치에 대해 반복
        // 최소 시간 계산: 개미가 왼쪽 끝 또는 오른쪽 끝 중 더 가까운 쪽으로 가는 시간
        min_time = max(min_time, min(position, l - position));
        
        // 최대 시간 계산: 개미가 왼쪽 끝 또는 오른쪽 끝 중 더 먼 쪽으로 가는 시간
        max_time = max(max_time, max(position, l - position));
    }
    
    return {min_time, max_time}; // 최소 시간과 최대 시간을 페어로 반환
}

int main() {
    int test_cases;
    cin >> test_cases; // 테스트 케이스 수 입력
    
    while (test_cases--) { // 각 테스트 케이스마다 반복
        int l, n;
        cin >> l >> n; // 막대의 길이 l과 개미의 수 n 입력
        
        vector<int> positions(n); // 개미의 위치를 저장할 벡터
        for (int i = 0; i < n; ++i) {
            cin >> positions[i]; // 개미의 위치 입력
        }
        
        pair<int, int> result = ant_times(l, positions); // 최소, 최대 시간 계산
        cout << result.first << " " << result.second << endl; // 결과 출력
    }
    
    return 0;
}
