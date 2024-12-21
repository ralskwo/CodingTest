#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 두 빌딩이 서로 보이는지 여부를 판단하는 함수
bool is_visible(const vector<int>& heights, int i, int j) {
    // 두 빌딩 사이의 기울기 계산
    double slope = (double)(heights[j] - heights[i]) / (j - i);
    
    // i와 j 사이의 빌딩을 하나씩 확인
    for (int k = i + 1; k < j; k++) {
        // k번 빌딩이 i와 j를 잇는 직선 위에 있거나 직선보다 높으면 false 반환
        if (heights[k] >= heights[i] + slope * (k - i)) {
            return false;
        }
    }
    // 중간에 가리는 빌딩이 없다면 true 반환
    return true;
}

// 가장 많은 빌딩이 보이는 수를 계산하는 함수
int count_visible_buildings(int N, const vector<int>& heights) {
    int max_count = 0;

    // 각 빌딩을 기준으로 좌우의 빌딩 확인
    for (int i = 0; i < N; i++) {
        int visible_count = 0;

        // 왼쪽 빌딩 확인
        for (int j = i - 1; j >= 0; j--) {
            if (is_visible(heights, j, i)) {
                visible_count++;
            }
        }

        // 오른쪽 빌딩 확인
        for (int j = i + 1; j < N; j++) {
            if (is_visible(heights, i, j)) {
                visible_count++;
            }
        }

        // 최대 보이는 빌딩 수 갱신
        max_count = max(max_count, visible_count);
    }

    return max_count;
}

int main() {
    int N;
    // 빌딩 개수 입력
    cin >> N;
    vector<int> heights(N);

    // 빌딩 높이 입력
    for (int i = 0; i < N; i++) {
        cin >> heights[i];
    }

    // 결과 출력
    cout << count_visible_buildings(N, heights) << endl;

    return 0;
}
