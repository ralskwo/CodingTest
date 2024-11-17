#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int maxFruitLength(int N, vector<int>& fruits) {
    unordered_map<int, int> fruitCount; // 과일 종류와 개수를 저장할 해시맵
    int left = 0; // 슬라이딩 윈도우의 시작 포인터
    int maxLength = 0; // 최대 길이를 저장할 변수

    for (int right = 0; right < N; ++right) { // 배열을 끝까지 탐색
        fruitCount[fruits[right]]++; // 현재 과일을 맵에 추가하고 개수를 증가

        while (fruitCount.size() > 2) { // 윈도우 내 과일 종류가 2개를 초과하면
            fruitCount[fruits[left]]--; // 왼쪽 포인터의 과일 개수를 감소
            if (fruitCount[fruits[left]] == 0) { // 개수가 0이면 맵에서 삭제
                fruitCount.erase(fruits[left]);
            }
            left++; // 왼쪽 포인터를 이동하여 윈도우 크기를 조정
        }

        maxLength = max(maxLength, right - left + 1); // 최대 길이를 갱신
    }

    return maxLength; // 가장 긴 길이를 반환
}

int main() {
    int N;
    cin >> N; // 과일 개수 입력
    vector<int> fruits(N);
    for (int i = 0; i < N; ++i) {
        cin >> fruits[i]; // 과일 배열 입력
    }

    cout << maxFruitLength(N, fruits) << endl; // 최대 과일 길이 출력
    return 0;
}