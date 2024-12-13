#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    // 입력값 처리
    int N, d, k, c;
    cin >> N >> d >> k >> c;  // N: 접시 수, d: 초밥 종류 수, k: 연속 접시 수, c: 쿠폰 번호

    vector<int> sushi(N);  // 초밥 벨트
    for (int i = 0; i < N; ++i) {
        cin >> sushi[i];  // 초밥 벨트 정보 입력
    }

    // 원형 벨트 처리를 위한 확장
    vector<int> extended_sushi = sushi;
    extended_sushi.insert(extended_sushi.end(), sushi.begin(), sushi.begin() + k - 1);

    // 슬라이딩 윈도우를 위한 변수 초기화
    unordered_map<int, int> sushi_count;  // 초밥 종류와 개수를 저장
    int current_variety = 0;  // 현재 초밥 종류 수
    int max_variety = 0;  // 최대 초밥 종류 수

    // 초기 윈도우 설정
    for (int i = 0; i < k; ++i) {
        if (sushi_count[extended_sushi[i]] == 0) {
            current_variety++;  // 새로운 초밥 종류 발견 시 증가
        }
        sushi_count[extended_sushi[i]]++;
    }

    // 쿠폰 초밥 포함 여부 확인 후 최대값 초기화
    max_variety = current_variety + (sushi_count[c] == 0 ? 1 : 0);

    // 슬라이딩 윈도우 이동
    for (int i = k; i < extended_sushi.size(); ++i) {
        // 윈도우에서 빠지는 초밥 처리
        int leaving_sushi = extended_sushi[i - k];
        sushi_count[leaving_sushi]--;
        if (sushi_count[leaving_sushi] == 0) {
            current_variety--;  // 초밥 종류 감소
        }

        // 윈도우에 새로 추가되는 초밥 처리
        int entering_sushi = extended_sushi[i];
        if (sushi_count[entering_sushi] == 0) {
            current_variety++;  // 새로운 초밥 종류 발견 시 증가
        }
        sushi_count[entering_sushi]++;

        // 쿠폰 초밥 포함하여 최대값 갱신
        max_variety = max(max_variety, current_variety + (sushi_count[c] == 0 ? 1 : 0));
    }

    // 결과 출력
    cout << max_variety << endl;

    return 0;
}
