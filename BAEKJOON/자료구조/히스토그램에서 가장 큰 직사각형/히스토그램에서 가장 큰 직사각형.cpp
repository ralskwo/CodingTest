#include <iostream>
#include <stack>
#include <vector>
using namespace std;

long long largestRectangleArea(vector<int>& hist) {
    stack<int> s; // 스택을 초기화합니다. 스택에는 히스토그램 막대의 인덱스가 저장됩니다.
    long long max_area = 0; // 최대 면적을 저장할 변수를 초기화합니다.
    int index = 0; // 현재 히스토그램의 인덱스를 가리키는 변수를 초기화합니다.

    // 히스토그램의 모든 막대를 순회합니다.
    while (index < hist.size()) {
        // 스택이 비어 있거나 현재 막대가 스택의 최상단 막대보다 높으면 인덱스를 스택에 추가합니다.
        if (s.empty() || hist[s.top()] <= hist[index]) {
            s.push(index++);
        } else {
            // 현재 막대가 스택의 최상단 막대보다 낮으면 스택에서 인덱스를 꺼냅니다.
            int top_of_stack = s.top();
            s.pop();
            // 꺼낸 막대의 높이를 기준으로 넓이를 계산합니다.
            long long area = (long long)hist[top_of_stack] * (s.empty() ? index : index - s.top() - 1);
            // 최대 면적을 갱신합니다.
            if (max_area < area) {
                max_area = area;
            }
        }
    }

    // 남아 있는 스택의 막대들에 대해 넓이를 계산합니다.
    while (!s.empty()) {
        int top_of_stack = s.top();
        s.pop();
        long long area = (long long)hist[top_of_stack] * (s.empty() ? index : index - s.top() - 1);
        if (max_area < area) {
            max_area = area;
        }
    }

    // 최대 면적을 반환합니다.
    return max_area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int n;
        cin >> n; // 각 테스트 케이스의 막대 수를 읽습니다.
        if (n == 0) break; // 막대 수가 0이면 종료합니다.

        vector<int> hist(n);
        for (int i = 0; i < n; ++i) {
            cin >> hist[i]; // 히스토그램의 높이를 벡터에 저장합니다.
        }

        // 가장 큰 직사각형의 넓이를 계산하여 출력합니다.
        cout << largestRectangleArea(hist) << '\n';
    }

    return 0;
}
