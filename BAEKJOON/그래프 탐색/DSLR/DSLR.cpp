#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int command(int n, char cmd) {
    switch(cmd) {
        case 'D':
            return (2 * n) % 10000; // D 명령어: 숫자를 두 배로 하고 10000으로 나눈 나머지
        case 'S':
            return (n == 0) ? 9999 : n - 1; // S 명령어: 숫자에서 1을 빼고 음수가 되면 9999로 설정
        case 'L':
            return (n % 1000) * 10 + n / 1000; // L 명령어: 자릿수를 왼쪽으로 한 칸 회전
        case 'R':
            return (n % 10) * 1000 + n / 10; // R 명령어: 자릿수를 오른쪽으로 한 칸 회전
        default:
            return n;
    }
}

string bfs(int start, int end) {
    queue<pair<int, string>> q;
    vector<bool> visited(10000, false);
    q.push({start, ""});
    visited[start] = true;

    while (!q.empty()) {
        int current = q.front().first;
        string path = q.front().second;
        q.pop();

        if (current == end) {
            return path;
        }

        for (char cmd : {'D', 'S', 'L', 'R'}) {
            int next_num = command(current, cmd);
            if (!visited[next_num]) {
                visited[next_num] = true;
                q.push({next_num, path + cmd});
            }
        }
    }

    return "";
}

int main() {
    int T;
    cin >> T;
    vector<string> results;
    
    for (int i = 0; i < T; ++i) {
        int A, B;
        cin >> A >> B;
        results.push_back(bfs(A, B));
    }
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
