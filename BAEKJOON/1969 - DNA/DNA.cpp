#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

// 최소 Hamming Distance를 계산하는 함수
pair<string, int> findMinHammingDNA(int N, int M, vector<string> &dnaList) {
    string minDistanceDNA = ""; // 최소 거리 DNA를 저장할 변수
    int totalHammingDistance = 0; // Hamming Distance 총합을 저장할 변수

    // 각 열(column)에 대해 반복
    for (int col = 0; col < M; ++col) {
        map<char, int> freq; // 각 문자(A, T, G, C)의 빈도를 저장할 맵

        // 현재 열의 모든 DNA 문자열에서 문자 빈도를 계산
        for (int row = 0; row < N; ++row) {
            freq[dnaList[row][col]]++;
        }

        // 가장 빈번한 문자를 선택. 빈도가 같으면 사전순으로 선택
        char mostCommon = 'A';
        int maxFreq = 0;
        for (auto &entry : freq) {
            if (entry.second > maxFreq || (entry.second == maxFreq && entry.first < mostCommon)) {
                mostCommon = entry.first;
                maxFreq = entry.second;
            }
        }

        // 최소 거리 DNA에 가장 빈번한 문자 추가
        minDistanceDNA += mostCommon;

        // Hamming Distance 계산: 전체 문자 개수 - 가장 빈번한 문자 개수
        totalHammingDistance += N - maxFreq;
    }

    return {minDistanceDNA, totalHammingDistance}; // 최소 거리 DNA와 Hamming Distance 총합 반환
}

int main() {
    int N, M; // DNA 개수와 문자열 길이
    cin >> N >> M;

    vector<string> dnaList(N); // DNA 문자열 리스트
    for (int i = 0; i < N; ++i) {
        cin >> dnaList[i];
    }

    // 최소 거리 DNA와 Hamming Distance 계산
    auto result = findMinHammingDNA(N, M, dnaList);

    // 결과 출력
    cout << result.first << endl; // 최소 거리 DNA 출력
    cout << result.second << endl; // Hamming Distance 총합 출력

    return 0;
}