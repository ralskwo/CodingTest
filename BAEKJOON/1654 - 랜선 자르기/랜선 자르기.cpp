#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 랜선 자르기의 최대 길이를 계산하는 함수
long long maxLanLength(int k, int n, vector<long long>& lengths) {
    long long start = 1; // 이분 탐색의 시작점
    long long end = *max_element(lengths.begin(), lengths.end()); // 랜선의 최대 길이
    long long result = 0; // 결과를 저장할 변수

    while (start <= end) {
        long long mid = (start + end) / 2; // 중간값 계산
        long long count = 0; // 현재 중간 길이로 만들 수 있는 랜선 개수

        for (long long length : lengths) {
            count += length / mid; // 각 랜선을 중간 길이로 잘라 만든 개수 합산
        }

        if (count >= n) {
            result = mid; // 랜선 개수가 N개 이상이면 결과 갱신
            start = mid + 1; // 더 긴 길이를 탐색
        } else {
            end = mid - 1; // 랜선 개수가 N개 미만이면 더 짧은 길이를 탐색
        }
    }

    return result; // 최종적으로 찾은 최대 길이를 반환
}

int main() {
    int k, n; // 입력받을 랜선 개수와 필요한 랜선 개수
    cin >> k >> n;

    vector<long long> lengths(k); // 랜선 길이를 저장할 벡터
    for (int i = 0; i < k; i++) {
        cin >> lengths[i]; // 각 랜선의 길이를 입력받음
    }

    cout << maxLanLength(k, n, lengths) << endl; // 최대 랜선 길이를 출력
    return 0;
}
