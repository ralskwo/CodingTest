#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 꽃의 시작 날짜와 종료 날짜를 저장할 구조체
struct Flower {
    int start; // 시작 날짜 (MMDD 형식)
    int end;   // 종료 날짜 (MMDD 형식)
};

// 비교 함수: 꽃의 시작 날짜를 기준으로 오름차순 정렬, 시작 날짜가 같으면 종료 날짜 내림차순 정렬
bool compare(Flower a, Flower b) {
    if (a.start == b.start)
        return a.end > b.end; // 시작 날짜가 같으면 종료 날짜 내림차순
    return a.start < b.start; // 시작 날짜를 기준으로 오름차순 정렬
}

int main() {
    int N; // 꽃의 개수
    cin >> N;
    
    vector<Flower> flowers(N); // 꽃 정보를 저장할 벡터

    // 꽃의 정보를 입력받아 MMDD 형식으로 저장
    for (int i = 0; i < N; ++i) {
        int sm, sd, em, ed;
        cin >> sm >> sd >> em >> ed;
        flowers[i].start = sm * 100 + sd; // 시작 날짜를 MMDD 형식으로 변환
        flowers[i].end = em * 100 + ed;   // 종료 날짜를 MMDD 형식으로 변환
    }

    // 꽃을 정렬: 시작 날짜 오름차순, 같은 시작 날짜일 경우 종료 날짜 내림차순
    sort(flowers.begin(), flowers.end(), compare);

    int START = 301; // 3월 1일을 MMDD 형식으로 설정
    int END = 1130;  // 11월 30일을 MMDD 형식으로 설정

    int current_end = START; // 현재 커버할 수 있는 마지막 날짜
    int max_end = 0;         // 선택된 꽃들이 커버할 수 있는 최대 종료 날짜
    int count = 0;           // 선택된 꽃의 수
    int i = 0;               // flowers 벡터의 인덱스를 추적할 변수

    // 모든 꽃을 순회하거나, 커버할 수 있는 날짜가 END를 넘어갈 때까지 반복
    while (i < N && current_end <= END) {
        bool found = false; // 현재 커버할 수 있는 꽃을 찾았는지 여부
        while (i < N && flowers[i].start <= current_end) {
            // current_end 이하에서 피는 꽃들 중 가장 늦게 지는 꽃을 찾음
            if (flowers[i].end > max_end) {
                max_end = flowers[i].end;
                found = true; // 유효한 꽃을 찾았음을 표시
            }
            ++i; // 다음 꽃으로 이동
        }

        if (!found) // 만약 더 이상 커버할 수 있는 날짜를 연장할 수 없는 경우
            break;

        current_end = max_end; // 현재 커버 가능한 마지막 날짜를 갱신
        ++count; // 꽃을 하나 선택했으므로 count 증가
    }

    // 만약 11월 30일을 커버하지 못하면 0 출력
    if (current_end <= END)
        cout << 0 << endl;
    else
        cout << count << endl;

    return 0;
}
