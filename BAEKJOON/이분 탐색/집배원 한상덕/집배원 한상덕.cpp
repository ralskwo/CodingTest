#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <climits>

using namespace std;

int N;
vector<string> village;
vector<vector<int>> altitude;
pair<int, int> post_office;
vector<int> heights;
int total_houses = 0;

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};

bool canDeliver(int min_height, int max_height) {
    if (altitude[post_office.first][post_office.second] < min_height || 
        altitude[post_office.first][post_office.second] > max_height) {
        return false;
    }

    vector<vector<bool>> visited(N, vector<bool>(N, false));
    queue<pair<int, int>> q;
    q.push(post_office);
    visited[post_office.first][post_office.second] = true;
    int delivered = 0;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (village[x][y] == 'K') {
            delivered++;
        }

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                if (altitude[nx][ny] >= min_height && altitude[nx][ny] <= max_height) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }

    return delivered == total_houses;
}

int main() {
    cin >> N;

    village.resize(N);
    altitude.resize(N, vector<int>(N));
    
    for (int i = 0; i < N; i++) {
        cin >> village[i];
    }

    set<int> height_set;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> altitude[i][j];
            height_set.insert(altitude[i][j]);
            if (village[i][j] == 'P') {
                post_office = {i, j};
            }
            if (village[i][j] == 'K') {
                total_houses++;
            }
        }
    }

    heights.assign(height_set.begin(), height_set.end());
    
    int left = 0, right = 0;
    int min_fatigue = INT_MAX;

    while (right < heights.size()) {
        if (left < heights.size() && canDeliver(heights[left], heights[right])) {
            min_fatigue = min(min_fatigue, heights[right] - heights[left]);
            left++;
        } else {
            right++;
        }
    }

    cout << min_fatigue << endl;
    
    return 0;
}
