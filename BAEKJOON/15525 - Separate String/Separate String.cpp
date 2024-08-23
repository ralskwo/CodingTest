#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

const int MOD = 1'000'000'007;

// TrieNode 클래스 정의
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool is_end_of_word;

    TrieNode() {
        is_end_of_word = false;
    }
};

// Trie 클래스 정의
class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    // 단어를 트라이에 삽입하는 함수
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->is_end_of_word = true;
    }

    // 트라이에서 부분 문자열을 검색하는 함수
    vector<int> search(const string& s, int start) {
        TrieNode* node = root;
        vector<int> results;
        for (int i = start; i < s.length(); ++i) {
            char c = s[i];
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            if (node->is_end_of_word) {
                results.push_back(i + 1);
            }
        }
        return results;
    }
};

// 문자열 분할 방법의 수를 계산하는 함수
int count_ways(int N, vector<string>& S, const string& t) {
    Trie trie;
    for (const string& word : S) {
        trie.insert(word);
    }

    int len_t = t.length();
    vector<int> dp(len_t + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < len_t; ++i) {
        if (dp[i] > 0) {
            vector<int> matches = trie.search(t, i);
            for (int j : matches) {
                dp[j] = (dp[j] + dp[i]) % MOD;
            }
        }
    }

    return dp[len_t];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<string> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    string t;
    cin >> t;

    int result = count_ways(N, S, t);
    cout << result << endl;

    return 0;
}
