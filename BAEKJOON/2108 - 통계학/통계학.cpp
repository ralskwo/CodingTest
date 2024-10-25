#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;

int main() {
    // 수의 개수 N 입력
    int N;
    cin >> N;

    // 입력된 수들을 저장할 벡터와 빈도를 저장할 map 선언
    vector<int> arr(N);
    map<int, int> frequency;

    // 수 입력 및 빈도 계산
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
        frequency[arr[i]]++;
    }

    // 벡터를 오름차순으로 정렬
    sort(arr.begin(), arr.end());

    // 산술평균 계산 및 출력
    double sum = 0;
    for (int num : arr) sum += num;
    // round 함수는 소수점 첫째 자리에서 반올림된 값을 반환
    int mean = round(sum / N);
    cout << mean << '\n';

    // 중앙값은 정렬된 벡터에서 가운데 값
    int median = arr[N / 2];
    cout << median << '\n';

    // 최빈값 찾기
    vector<pair<int, int>> freqVec(frequency.begin(), frequency.end());
    // 빈도수가 높은 순서로 정렬, 빈도가 같으면 숫자가 작은 순서로 정렬
    sort(freqVec.begin(), freqVec.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second > b.second;
    });

    // 최빈값이 여러 개일 경우 두 번째로 작은 값 출력
    int mode = (freqVec.size() > 1 && freqVec[0].second == freqVec[1].second) 
               ? freqVec[1].first 
               : freqVec[0].first;
    cout << mode << '\n';

    // 범위는 정렬된 벡터에서 최댓값과 최솟값의 차이
    int range = arr.back() - arr.front();
    cout << range << '\n';

    return 0;
}