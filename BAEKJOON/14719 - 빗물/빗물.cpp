#include <iostream>
#include <vector>
#include <algorithm> // std::max, std::min 사용을 위해

using namespace std;

int calculateTrappedRainwater(int H, int W, vector<int>& heights) {
    // 왼쪽과 오른쪽 최대 높이를 저장할 벡터를 선언하고 0으로 초기화
    vector<int> left_max(W, 0);
    vector<int> right_max(W, 0);
    
    // 첫 번째 위치의 왼쪽 최대 높이는 그 위치의 높이로 설정
    left_max[0] = heights[0];
    // 각 위치에 대해 왼쪽 최대 높이를 계산
    for (int i = 1; i < W; ++i) {
        left_max[i] = max(left_max[i - 1], heights[i]);
    }
    
    // 마지막 위치의 오른쪽 최대 높이는 그 위치의 높이로 설정
    right_max[W - 1] = heights[W - 1];
    // 각 위치에 대해 오른쪽 최대 높이를 계산
    for (int i = W - 2; i >= 0; --i) {
        right_max[i] = max(right_max[i + 1], heights[i]);
    }
    
    // 총 고일 수 있는 빗물의 양을 저장할 변수
    int total_water = 0;
    // 각 위치에 대해 고일 수 있는 빗물의 양을 계산
    for (int i = 0; i < W; ++i) {
        // 현재 위치에서 고일 수 있는 물의 양을 계산
        int water = min(left_max[i], right_max[i]) - heights[i];
        // 양수인 경우에만 총 빗물 양에 더해줌
        if (water > 0) {
            total_water += water;
        }
    }
    
    return total_water;
}

int main() {
    int H, W;
    // 세로 길이(H)와 가로 길이(W) 입력 받기
    cin >> H >> W;
    vector<int> heights(W);
    // 각 위치의 높이 입력 받기
    for (int i = 0; i < W; ++i) {
        cin >> heights[i];
    }
    // 함수 호출 및 결과 출력
    cout << calculateTrappedRainwater(H, W, heights) << endl;
    return 0;
}