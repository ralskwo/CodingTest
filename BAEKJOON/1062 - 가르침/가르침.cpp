#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

// 함수: 특정 문자를 배울 때 읽을 수 있는 단어의 수를 계산
int count_readable_words(const vector<set<char>>& words, const vector<bool>& learned) {
    int count = 0; // 읽을 수 있는 단어의 수를 초기화
    for (const auto& word : words) {
        bool readable = true; // 현재 단어를 읽을 수 있는지 여부를 나타내는 변수
        for (char c : word) {
            if (!learned[c - 'a']) { // 문자를 배우지 않았다면
                readable = false; // 읽을 수 없는 것으로 표시
                break; // 더 이상 확인할 필요 없음
            }
        }
        if (readable) { // 모든 문자를 배웠다면
            count++; // 읽을 수 있는 단어 수 증가
        }
    }
    return count; // 총 읽을 수 있는 단어 수를 반환
}

// 함수: 주어진 단어 수 N과 가르칠 수 있는 문자 수 K를 고려하여 읽을 수 있는 최대 단어 수를 계산
int solve(int N, int K, const vector<string>& words_input) {
    if (K < 5) { // K가 5 미만이면 기본 "antic" 문자를 배울 수 없음
        return 0; // 읽을 수 있는 단어 수는 0
    } else if (K == 26) { // K가 26이면 모든 알파벳을 배울 수 있음
        return N; // 모든 단어를 읽을 수 있음
    }

    set<char> basic_letters = {'a', 'n', 't', 'i', 'c'}; // 기본적으로 알아야 하는 문자 집합
    set<char> all_letters; // 모든 문자의 집합
    for (char c = 'a'; c <= 'z'; ++c) {
        all_letters.insert(c);
    }
    set<char> letters_to_learn; // 추가로 배워야 하는 문자 집합
    set_difference(all_letters.begin(), all_letters.end(),
                   basic_letters.begin(), basic_letters.end(),
                   inserter(letters_to_learn, letters_to_learn.begin()));

    vector<set<char>> words; // 단어 리스트
    for (const auto& word : words_input) {
        set<char> word_set(word.begin(), word.end());
        for (char c : basic_letters) {
            word_set.erase(c);
        }
        words.push_back(word_set);
    }

    int max_readable = 0; // 최대 읽을 수 있는 단어 수를 저장하는 변수
    vector<char> letters_to_learn_vec(letters_to_learn.begin(), letters_to_learn.end());

    // letters_to_learn의 K-5개의 조합을 탐색
    vector<bool> comb(letters_to_learn_vec.size(), false);
    fill(comb.end() - (K - 5), comb.end(), true);

    do {
        vector<bool> learned(26, false); // 알파벳을 배웠는지 여부를 저장하는 리스트 초기화
        for (char c : basic_letters) { // 기본 문자를 배운 것으로 설정
            learned[c - 'a'] = true;
        }
        for (int i = 0; i < letters_to_learn_vec.size(); ++i) { // 현재 조합의 문자를 배운 것으로 설정
            if (comb[i]) {
                learned[letters_to_learn_vec[i] - 'a'] = true;
            }
        }
        max_readable = max(max_readable, count_readable_words(words, learned)); // 읽을 수 있는 최대 단어 수를 갱신
    } while (next_permutation(comb.begin(), comb.end()));

    return max_readable; // 최대 읽을 수 있는 단어 수를 반환
}

int main() {
    int N, K;
    cin >> N >> K; // 첫 번째 줄에서 단어 수 N과 가르칠 문자 수 K를 입력받음
    vector<string> words(N);
    for (int i = 0; i < N; ++i) {
        cin >> words[i]; // N개의 단어를 입력받아 리스트에 저장
    }

    // 결과 출력
    cout << solve(N, K, words) << endl; // 계산된 최대 읽을 수 있는 단어 수를 출력

    return 0;
}
