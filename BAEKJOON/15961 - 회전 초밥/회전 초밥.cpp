#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    // 입력을 빠르게 받기 위해서 사용
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 회전 초밥 벨트 정보와 관련된 변수 선언
    int N, d, k, c;
    cin >> N >> d >> k >> c;

    // 벨트에 놓인 초밥 종류를 저장할 벡터
    vector<int> sushi(N);
    for (int i = 0; i < N; ++i) {
        cin >> sushi[i];
    }

    // 슬라이딩 윈도우 내의 초밥 종류를 카운트할 맵
    unordered_map<int, int> eaten;

    // 초기 슬라이딩 윈도우 설정: 처음 k개의 초밥을 윈도우에 추가
    for (int i = 0; i < k; ++i) {
        eaten[sushi[i]]++;
    }

    // 쿠폰 초밥을 윈도우에 추가하여 시작 시점에 포함시키기
    eaten[c]++;

    // 현재 윈도우에 있는 서로 다른 초밥 종류 수를 최대값으로 초기화
    int max_variety = eaten.size();

    // 슬라이딩 윈도우를 통해 벨트의 모든 위치 순회
    for (int i = 0; i < N; ++i) {
        // 윈도우에서 빠지는 첫 번째 초밥 제거
        int remove_sushi = sushi[i];
        eaten[remove_sushi]--;
        if (eaten[remove_sushi] == 0) {
            eaten.erase(remove_sushi);
        }

        // 윈도우에 새로운 초밥 추가 (원형 배열 특성 고려)
        int add_sushi = sushi[(i + k) % N];
        eaten[add_sushi]++;

        // 최대 종류 수 갱신
        max_variety = max(max_variety, (int)eaten.size());
    }

    // 결과 출력
    cout << max_variety << endl;

    return 0;
}