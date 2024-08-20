#include <vector>  // 벡터를 사용하기 위해 포함
using namespace std;

int solution(vector<int> ingredient) {
    vector<int> stack;  // 현재 재료들을 쌓아놓을 스택을 벡터로 초기화
    int count = 0;  // 완성된 햄버거의 개수를 세기 위한 카운트를 초기화
    
    for (int item : ingredient) {  // 재료 리스트를 순차적으로 처리
        stack.push_back(item);  // 현재 재료를 스택에 추가
        // 스택의 길이가 4 이상이어야 하며, 마지막 4개의 재료가 [1, 2, 3, 1]인지 확인
        if (stack.size() >= 4 && stack[stack.size()-1] == 1 && stack[stack.size()-2] == 3 
            && stack[stack.size()-3] == 2 && stack[stack.size()-4] == 1) {
            count++;  // 햄버거가 완성되었으므로 카운트를 1 증가
            stack.erase(stack.end() - 4, stack.end());  // 스택에서 완성된 햄버거의 재료 4개를 제거
        }
    }
    
    return count;  // 총 완성된 햄버거의 개수를 반환
}
