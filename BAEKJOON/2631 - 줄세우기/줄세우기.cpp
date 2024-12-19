#include <iostream>
#include <vector>
#include <algorithm> // for lower_bound

using namespace std;

int main() {
    int n;
    cin >> n; // 아이들의 수를 입력받습니다.

    vector<int> children(n); // 아이들의 번호를 저장할 벡터를 선언합니다.
    for (int i = 0; i < n; i++) {
        cin >> children[i]; // 아이들의 번호를 입력받아 벡터에 저장합니다.
    }

    vector<int> lis; // 최장 증가 부분 수열(LIS)을 저장할 벡터를 선언합니다.

    for (int num : children) {
        // 현재 숫자가 LIS에 들어갈 위치를 이진 탐색으로 찾습니다.
        auto pos = lower_bound(lis.begin(), lis.end(), num);

        if (pos == lis.end()) {
            // 위치가 LIS의 끝이라면 현재 숫자를 추가합니다.
            lis.push_back(num);
        } else {
            // 그렇지 않으면 해당 위치 값을 현재 숫자로 대체합니다.
            *pos = num;
        }
    }

    // 최소 이동 수는 전체 아이들 수에서 LIS 길이를 뺀 값입니다.
    cout << n - lis.size() << endl;

    return 0;
}
