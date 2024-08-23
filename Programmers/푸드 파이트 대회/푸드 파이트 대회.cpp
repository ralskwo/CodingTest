#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string solution(vector<int> food) {
    string left_side = "";

    // 1번 음식부터 food의 각 요소를 순회
    for (int i = 1; i < food.size(); i++) {
        int count = food[i] / 2;  // 각 음식의 절반만큼의 개수
        left_side += string(count, '0' + i);  // 음식 번호를 count만큼 추가
    }

    string right_side = left_side;  // right_side는 left_side와 동일하게 시작
    reverse(right_side.begin(), right_side.end());  // right_side를 뒤집음

    // left_side + '0' + right_side로 최종 문자열 생성
    string result = left_side + '0' + right_side;
    return result;
}