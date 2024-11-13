#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 각도를 받아서 간격을 계산하는 함수
vector<int> calculate_gaps(vector<int>& angles) {
    sort(angles.begin(), angles.end());  // 각도를 정렬하여 순서를 맞춤
    vector<int> gaps;
    int n = angles.size();
    for (int i = 1; i < n; ++i) {
        gaps.push_back(angles[i] - angles[i - 1]);  // 연속된 각도 간의 차이를 계산해 저장
    }
    gaps.push_back(360000 - angles[n - 1] + angles[0]);  // 마지막과 첫 번째 각도의 차이 추가
    return gaps;
}

// KMP 알고리즘을 이용해 패턴을 찾는 함수
bool kmp_search(const vector<int>& text, const vector<int>& pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> lps(m, 0);  // 패턴의 LPS 배열 생성
    int j = 0;

    // LPS 배열 생성 과정
    for (int i = 1; i < m; ++i) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = lps[j - 1];  // 불일치가 발생하면 이전 위치로 돌아감
        }
        if (pattern[i] == pattern[j]) {
            lps[i] = ++j;  // 일치할 경우 j를 증가시키며 LPS 배열 업데이트
        }
    }

    j = 0;
    for (int i = 0; i < n; ++i) {
        while (j > 0 && text[i] != pattern[j]) {
            j = lps[j - 1];  // 불일치가 발생하면 j를 LPS에 따라 이동
        }
        if (text[i] == pattern[j]) {
            if (++j == m) return true;  // 패턴이 완전히 일치할 경우 true 반환
        }
    }
    return false;
}

int main() {
    int n;
    cin >> n;  // 시계 바늘의 개수 입력
    vector<int> angles1(n), angles2(n);

    for (int i = 0; i < n; ++i) cin >> angles1[i];  // 첫 번째 시계의 각도 입력
    for (int i = 0; i < n; ++i) cin >> angles2[i];  // 두 번째 시계의 각도 입력

    vector<int> gaps1 = calculate_gaps(angles1);  // 첫 번째 시계의 간격 계산
    vector<int> gaps2 = calculate_gaps(angles2);  // 두 번째 시계의 간격 계산

    vector<int> doubled_gaps1 = gaps1;
    doubled_gaps1.insert(doubled_gaps1.end(), gaps1.begin(), gaps1.end());  // 두 배로 확장하여 회전 가능성 검사

    if (kmp_search(doubled_gaps1, gaps2)) {
        cout << "possible" << endl;  // 회전하여 동일한 간격이 가능할 경우
    } else {
        cout << "impossible" << endl;  // 불가능할 경우
    }

    return 0;
}