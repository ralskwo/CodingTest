#include <iostream>  // 표준 입출력 사용을 위한 헤더 파일
#include <vector>    // 벡터 사용을 위한 헤더 파일
#include <algorithm> // 정렬을 위한 헤더 파일

using namespace std; // std 네임스페이스를 사용하여 코드 간결화

int main() {
    int N; // 저울추의 개수를 저장할 변수
    cin >> N; // 저울추의 개수 입력 받기
    
    vector<int> weights(N); // N개의 저울추 무게를 저장할 벡터 선언
    
    for (int i = 0; i < N; ++i) {
        cin >> weights[i]; // 각 저울추의 무게를 입력 받아 벡터에 저장
    }

    sort(weights.begin(), weights.end()); // 저울추의 무게들을 오름차순으로 정렬
    
    int target = 1; // 만들 수 없는 최소 무게를 추적할 변수, 초기값은 1로 설정

    for (int i = 0; i < N; ++i) { // 정렬된 저울추 무게들을 순회
        if (weights[i] > target) { // 현재 저울추의 무게가 target보다 크다면
            break; // 만들 수 없는 최소 무게는 target이므로 반복문 종료
        }
        target += weights[i]; // 현재 저울추의 무게를 target에 더해주어 누적
    }

    cout << target << endl; // 최종적으로 만들 수 없는 최소 무게를 출력

    return 0; // 프로그램 정상 종료
}
