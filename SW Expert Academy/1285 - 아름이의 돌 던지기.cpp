#include <iostream>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int N;
        cin >> N;

        vector<int> stones(N);
        for (int i = 0; i < N; ++i) {
            cin >> stones[i];
        }

        int min_distance = INT_MAX;
        int min_stones = 0;

        for (int i = 0; i < N; ++i) {
            if (abs(stones[i]) < min_distance) {
                min_distance = abs(stones[i]);
                min_stones = 1;
            } else if (abs(stones[i]) == min_distance) {
                min_stones++;
            }
        }

        cout << "#" << t << " " << min_distance << " " << min_stones << endl;
    }

    return 0;
}