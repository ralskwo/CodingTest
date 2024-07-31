#include <iostream>
#include <vector>
#include <algorithm>

const int INF = 1e9;  // 무한대를 표현하기 위한 큰 수
int N;
std::vector<std::vector<int>> W;
std::vector<std::vector<int>> dp;

int tsp(int current, int visited) {
    if (visited == (1 << N) - 1) {  // 모든 도시를 방문한 경우
        return W[current][0] == 0 ? INF : W[current][0];  // 시작 도시로 돌아갈 수 있는지 확인
    }
    
    int &ret = dp[current][visited];
    if (ret != -1) return ret;  // 이미 계산된 값이 있으면 반환
    
    ret = INF;
    for (int i = 0; i < N; ++i) {
        if (visited & (1 << i)) continue;  // 이미 방문한 도시는 패스
        if (W[current][i] == 0) continue;  // 갈 수 없는 도시는 패스
        ret = std::min(ret, W[current][i] + tsp(i, visited | (1 << i)));  // 최솟값 갱신
    }
    
    return ret;
}

int main() {
    std::cin >> N;
    W = std::vector<std::vector<int>>(N, std::vector<int>(N));
    dp = std::vector<std::vector<int>>(N, std::vector<int>(1 << N, -1));
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cin >> W[i][j];
        }
    }
    
    int result = tsp(0, 1);
    if (result >= INF) result = -1;  // 결과가 무한대이면 경로가 없음을 의미
    
    std::cout << result << std::endl;
    return 0;
}
