#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

vector<int> findThreeSolutionsClosestToZero(int N, vector<int>& solutions) {
    sort(solutions.begin(), solutions.end());
    long long closestSum = numeric_limits<long long>::max();
    vector<int> answer(3);

    for (int i = 0; i < N - 2; ++i) {
        int left = i + 1, right = N - 1;

        while (left < right) {
            long long currentSum = (long long)solutions[i] + solutions[left] + solutions[right];

            if (abs(currentSum) < abs(closestSum)) {
                closestSum = currentSum;
                answer = {solutions[i], solutions[left], solutions[right]};
            }

            if (currentSum > 0) {
                --right;
            } else if (currentSum < 0) {
                ++left;
            } else {
                sort(answer.begin(), answer.end());
                return answer;
            }
        }
    }

    sort(answer.begin(), answer.end());
    return answer;
}

int main() {
    int N;
    cin >> N;
    vector<int> solutions(N);
    for (int i = 0; i < N; ++i) {
        cin >> solutions[i];
    }

    vector<int> result = findThreeSolutionsClosestToZero(N, solutions);
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}