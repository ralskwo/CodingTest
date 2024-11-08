#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 각 지원자의 서류 성적과 면접 성적 정보를 저장하는 구조체
struct Candidate {
    int docRank;      // 서류 순위
    int interviewRank; // 면접 순위
};

// 서류 성적을 기준으로 오름차순 정렬하기 위한 비교 함수
bool compare(const Candidate& a, const Candidate& b) {
    return a.docRank < b.docRank;
}

// 최대 선발 인원을 계산하는 함수
int maxHires(vector<Candidate>& candidates) {
    // 서류 순위를 기준으로 지원자들을 오름차순 정렬
    sort(candidates.begin(), candidates.end(), compare);

    // 첫 번째 지원자는 무조건 선발되므로 초기 선발 인원을 1로 설정
    int maxCount = 1;
    // 첫 번째 지원자의 면접 순위를 기준 면접 순위로 설정
    int minInterviewRank = candidates[0].interviewRank;

    // 두 번째 지원자부터 마지막 지원자까지 순회하며 선발 여부 결정
    for (int i = 1; i < candidates.size(); i++) {
        // 현재 지원자의 면접 순위가 기준 면접 순위보다 높다면 선발
        if (candidates[i].interviewRank < minInterviewRank) {
            maxCount++; // 선발 인원 증가
            minInterviewRank = candidates[i].interviewRank; // 기준 면접 순위 갱신
        }
    }

    // 최종적으로 선발된 최대 인원수를 반환
    return maxCount;
}

int main() {
    int T; // 테스트 케이스 개수
    cin >> T; // 입력 받기
    while (T--) {
        int N; // 각 테스트 케이스의 지원자 수
        cin >> N;

        vector<Candidate> candidates(N); // 지원자 정보를 저장할 벡터

        // 각 지원자의 서류 및 면접 순위를 입력받아 벡터에 저장
        for (int i = 0; i < N; i++) {
            cin >> candidates[i].docRank >> candidates[i].interviewRank;
        }

        // 현재 테스트 케이스의 최대 선발 인원을 출력
        cout << maxHires(candidates) << endl;
    }

    return 0;
}