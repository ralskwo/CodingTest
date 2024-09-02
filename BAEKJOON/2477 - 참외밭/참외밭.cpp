#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 1m²당 자라는 참외의 개수를 입력 받음
    int K;
    cin >> K;

    // 변의 방향과 길이를 저장할 벡터 선언
    vector<pair<int, int>> edges(6);
    for(int i = 0; i < 6; i++) {
        cin >> edges[i].first >> edges[i].second; // 방향과 길이를 입력받아 저장
    }

    // 가장 긴 가로와 세로 길이를 찾기 위한 변수 초기화
    int max_width = 0;
    int max_height = 0;

    // 각 변을 순회하며 최대 가로와 세로 길이를 찾음
    for(int i = 0; i < 6; i++) {
        if(edges[i].first == 1 || edges[i].first == 2) { // 동쪽(1) 또는 서쪽(2) 방향일 경우
            if(edges[i].second > max_width) { // 현재 변의 길이가 최대 가로보다 크면
                max_width = edges[i].second; // 최대 가로 길이를 갱신
            }
        }
        else if(edges[i].first == 3 || edges[i].first == 4) { // 남쪽(3) 또는 북쪽(4) 방향일 경우
            if(edges[i].second > max_height) { // 현재 변의 길이가 최대 세로보다 크면
                max_height = edges[i].second; // 최대 세로 길이를 갱신
            }
        }
    }

    // 작은 직사각형의 가로와 세로 길이를 찾기 위한 변수 초기화
    int small_width = 0;
    int small_height = 0;

    // 각 변을 다시 순회하며 작은 직사각형의 길이를 찾음
    for(int i = 0; i < 6; i++) {
        if(edges[i].first == 1 || edges[i].first == 2) { // 동쪽(1) 또는 서쪽(2) 방향일 경우
            // 현재 변의 다음 변과 이전 변의 길이 합이 최대 세로와 같으면
            if(edges[(i+1)%6].second + edges[(i+5)%6].second == max_height) {
                small_width = edges[i].second; // 작은 직사각형의 가로 길이로 설정
            }
        }
        else if(edges[i].first == 3 || edges[i].first == 4) { // 남쪽(3) 또는 북쪽(4) 방향일 경우
            // 현재 변의 다음 변과 이전 변의 길이 합이 최대 가로와 같으면
            if(edges[(i+1)%6].second + edges[(i+5)%6].second == max_width) {
                small_height = edges[i].second; // 작은 직사각형의 세로 길이로 설정
            }
        }
    }

    // 전체 면적을 계산: 큰 직사각형 면적에서 작은 직사각형 면적을 뺌
    long long area = (long long)(max_width * max_height) - (long long)(small_width * small_height);

    // 전체 참외의 개수를 계산
    long long total_melons = area * (long long)K;

    // 결과 출력
    cout << total_melons;

    return 0; // 프로그램 종료
}
