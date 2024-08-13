#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> jewels(n);
    vector<int> bags(k);

    for (int i = 0; i < n; ++i) {
        cin >> jewels[i].first >> jewels[i].second;
    }

    for (int i = 0; i < k; ++i) {
        cin >> bags[i];
    }

    // 보석을 무게 기준으로 오름차순 정렬합니다.
    sort(jewels.begin(), jewels.end());
    // 가방을 무게 기준으로 오름차순 정렬합니다.
    sort(bags.begin(), bags.end());

    long long max_value = 0;
    priority_queue<int> possible_jewels;
    int jewel_index = 0;

    for (int bag : bags) {
        // 현재 가방에 담을 수 있는 모든 보석을 힙에 넣습니다.
        while (jewel_index < n && jewels[jewel_index].first <= bag) {
            possible_jewels.push(jewels[jewel_index].second);
            ++jewel_index;
        }

        // 가장 비싼 보석을 선택합니다.
        if (!possible_jewels.empty()) {
            max_value += possible_jewels.top();
            possible_jewels.pop();
        }
    }

    cout << max_value << '\n';

    return 0;
}
