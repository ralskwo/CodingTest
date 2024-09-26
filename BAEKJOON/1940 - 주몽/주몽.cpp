#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int count_armors(int N, int M, vector<int>& materials) {
    // 재료 번호 배열 정렬
    sort(materials.begin(), materials.end());

    // 투 포인터 초기화
    int left = 0;
    int right = N - 1;
    int count = 0;

    // 투 포인터 방식으로 갑옷을 만들 수 있는 경우의 수를 셈
    while (left < right) {
        int sum_value = materials[left] + materials[right];

        if (sum_value == M) {
            count++;
            left++;
            right--;
        } else if (sum_value < M) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

int main() {
    int N, M;
    // 재료의 개수 입력
    cin >> N;
    // 갑옷을 만들기 위해 필요한 수 입력
    cin >> M;

    vector<int> materials(N);
    // 재료 번호 입력
    for (int i = 0; i < N; i++) {
        cin >> materials[i];
    }

    // 갑옷을 만들 수 있는 개수 출력
    cout << count_armors(N, M, materials) << endl;

    return 0;
}
