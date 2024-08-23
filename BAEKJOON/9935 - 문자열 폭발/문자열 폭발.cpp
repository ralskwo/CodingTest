#include <iostream>
#include <string>
#include <vector>

using namespace std;

string explodeString(const string& s, const string& bomb) {
    // 폭발 문자열을 처리하는 함수 정의
    // 이 함수는 문자열 s와 폭발 문자열 bomb를 입력으로 받아
    // 폭발 문자열을 모두 제거한 후의 최종 문자열을 반환합니다.
    
    vector<char> stack;
    // 스택 초기화
    // 스택은 주어진 문자열을 순차적으로 처리하면서 문자들을 저장하는 역할을 합니다.
    // 폭발 문자열이 감지되면 이 스택에서 그 부분을 제거합니다.

    int bomb_len = bomb.size();
    // 폭발 문자열의 길이를 계산
    // 폭발 문자열의 길이를 미리 계산해두어, 스택의 끝 부분에서 그 길이만큼 잘라내어
    // 비교하는 데 사용됩니다.

    for (char c : s) {
        // 문자열 순회
        // 주어진 문자열 s의 각 문자를 하나씩 순회합니다.
        
        stack.push_back(c);
        // 현재 문자를 스택에 추가
        // 순회하는 각 문자를 스택에 추가합니다. 이때 스택의 끝 부분에 문자가 추가됩니다.
        
        if (stack.size() >= bomb_len) {
            // 폭발 문자열 감지
            // 스택의 크기가 폭발 문자열의 길이보다 크거나 같을 때만 확인 가능
            bool match = true;
            for (int i = 0; i < bomb_len; ++i) {
                if (stack[stack.size() - bomb_len + i] != bomb[i]) {
                    match = false;
                    break;
                }
            }
            
            if (match) {
                // 폭발 문자열 제거
                // 스택의 끝 부분이 폭발 문자열과 일치하면, 그 부분을 스택에서 제거합니다.
                // 이렇게 하면 폭발 문자열이 제거된 후의 상태가 스택에 남게 됩니다.
                for (int i = 0; i < bomb_len; ++i) {
                    stack.pop_back();
                }
            }
        }
    }

    if (stack.empty()) {
        // 결과 문자열이 빈 문자열일 경우 처리
        // 만약 최종 문자열이 빈 문자열이라면, "FRULA"를 반환합니다.
        return "FRULA";
    } else {
        // 최종 문자열 반환
        // 빈 문자열이 아닌 경우, 스택에 남아 있는 문자들을 합친 문자열을 반환합니다.
        return string(stack.begin(), stack.end());
    }
}

int main() {
    // 입력 받기
    string s, bomb;
    cin >> s >> bomb;
    // 첫 번째 줄에서 문자열 s를 입력받습니다.
    // 두 번째 줄에서 폭발 문자열 bomb를 입력받습니다.

    // 결과 출력
    cout << explodeString(s, bomb) << endl;
    // 폭발 문자열 처리를 수행한 후, 결과를 출력합니다.

    return 0;
}
