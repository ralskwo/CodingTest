#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

// 펜윅 트리(Fenwick Tree) 클래스 정의
class FenwickTree {
public:
    FenwickTree(int size) : size(size) {
        tree.resize(size + 1, 0);
    }

    // 특정 인덱스에 값을 추가하는 함수
    void update(int index, int value) {
        while (index <= size) {
            tree[index] += value;
            index += index & -index;
        }
    }

    // 특정 인덱스까지의 누적 합을 계산하는 함수
    int query(int index) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index -= index & -index;
        }
        return result;
    }

private:
    int size;
    vector<int> tree;
};

// 좌표 압축을 수행하는 함수
vector<int> coordinate_compress(const vector<int>& values) {
    vector<int> sorted_unique = values;
    sort(sorted_unique.begin(), sorted_unique.end(), greater<int>());
    sorted_unique.erase(unique(sorted_unique.begin(), sorted_unique.end()), sorted_unique.end());
    
    map<int, int> rank;
    for (int i = 0; i < sorted_unique.size(); ++i) {
        rank[sorted_unique[i]] = i + 1;
    }

    vector<int> compressed(values.size());
    for (int i = 0; i < values.size(); ++i) {
        compressed[i] = rank[values[i]];
    }
    return compressed;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    
    vector<int> abilities(N);
    for (int i = 0; i < N; ++i) {
        cin >> abilities[i];
    }

    // 좌표 압축 수행
    vector<int> compressed_abilities = coordinate_compress(abilities);

    // 펜윅 트리 초기화
    int max_value = *max_element(compressed_abilities.begin(), compressed_abilities.end());
    FenwickTree fenwick_tree(max_value);
    
    vector<int> results(N);
    // 각 선수의 압축된 실력을 순회하며 등수를 계산
    for (int i = 0; i < N; ++i) {
        int ability = compressed_abilities[i];
        // 현재 선수보다 앞에 있는 더 높은 실력의 선수 수 쿼리
        int higher_count = fenwick_tree.query(ability - 1);
        results[i] = higher_count + 1;  // 현재 선수의 최선의 등수
        
        // 현재 선수의 능력을 펜윅 트리에 추가
        fenwick_tree.update(ability, 1);
    }

    // 결과 출력
    for (int i = 0; i < N; ++i) {
        cout << results[i] << '\n';
    }

    return 0;
}