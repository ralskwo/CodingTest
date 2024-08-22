#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 부분 집합의 합을 계산하는 함수
vector<long long> get_subsets(const vector<int>& weights) {
    int n = weights.size();
    vector<long long> subsets;
    
    // 모든 부분 집합을 계산하여 그 합을 저장
    for (int i = 0; i < (1 << n); i++) {
        long long sum = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                sum += weights[j];
            }
        }
        subsets.push_back(sum);
    }
    
    return subsets;
}

// 가능한 조합의 수를 계산하는 함수
long long count_valid_combinations(int N, long long C, const vector<int>& weights) {
    // 리스트를 반으로 나누기
    vector<int> left_weights(weights.begin(), weights.begin() + N / 2);
    vector<int> right_weights(weights.begin() + N / 2, weights.end());
    
    // 각각의 부분 집합의 합을 계산
    vector<long long> left_subsets = get_subsets(left_weights);
    vector<long long> right_subsets = get_subsets(right_weights);
    
    // 이진 탐색을 위한 정렬
    sort(right_subsets.begin(), right_subsets.end());
    
    long long count = 0;
    
    // 왼쪽 부분 집합의 합을 순회하면서, C를 넘지 않는 조합을 찾기
    for (long long left_sum : left_subsets) {
        if (left_sum <= C) {
            // C - left_sum 보다 작거나 같은 값을 갖는 오른쪽 부분 집합의 개수를 구함
            count += upper_bound(right_subsets.begin(), right_subsets.end(), C - left_sum) - right_subsets.begin();
        }
    }
    
    return count;
}

int main() {
    int N;
    long long C;
    
    // 입력 받기
    cin >> N >> C;
    vector<int> weights(N);
    for (int i = 0; i < N; i++) {
        cin >> weights[i];
    }
    
    // 가능한 조합의 수를 계산하여 출력
    cout << count_valid_combinations(N, C, weights) << endl;
    
    return 0;
}
