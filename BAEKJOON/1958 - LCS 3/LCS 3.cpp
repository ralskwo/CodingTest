#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // std::max 사용을 위해 포함
using namespace std;

int longestCommonSubsequence(string str1, string str2, string str3) {
    int len1 = str1.length();
    int len2 = str2.length();
    int len3 = str3.length();

    vector<vector<vector<int>>> dp(len1 + 1, vector<vector<int>>(len2 + 1, vector<int>(len3 + 1, 0)));

    for (int i = 1; i <= len1; ++i) {
        for (int j = 1; j <= len2; ++j) {
            for (int k = 1; k <= len3; ++k) {
                if (str1[i - 1] == str2[j - 1] && str2[j - 1] == str3[k - 1]) {
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
                } else {
                    dp[i][j][k] = std::max(dp[i - 1][j][k], std::max(dp[i][j - 1][k], dp[i][j][k - 1]));
                }
            }
        }
    }

    return dp[len1][len2][len3];
}

int main() {
    string str1, str2, str3;
    getline(cin, str1);
    getline(cin, str2);
    getline(cin, str3);

    cout << longestCommonSubsequence(str1, str2, str3) << endl;

    return 0;
}
