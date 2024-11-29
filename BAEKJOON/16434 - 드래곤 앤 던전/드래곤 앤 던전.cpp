#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ll;

// 던전 통과 가능 여부 확인 함수
bool canSurvive(ll maxHp, ll initialAtk, const vector<tuple<int, ll, ll>>& rooms) {
    ll curHp = maxHp;   // 현재 생명력은 최대 생명력으로 초기화
    ll curAtk = initialAtk; // 현재 공격력은 초기 공격력으로 초기화

    for (const auto& room : rooms) {
        int type;
        ll a, h;
        tie(type, a, h) = room;

        if (type == 1) {  // 몬스터 방
            ll turnsToKillMonster = (h + curAtk - 1) / curAtk;  // 몬스터를 죽이는 데 필요한 턴 수
            ll damageTaken = (turnsToKillMonster - 1) * a;  // 몬스터로부터 받는 총 피해
            curHp -= damageTaken;  // 생명력에서 피해를 차감
            if (curHp <= 0) return false;  // 생명력이 0 이하로 떨어지면 던전을 통과할 수 없음
        } else if (type == 2) {  // 포션 방
            curAtk += a;  // 공격력 증가
            curHp = min(maxHp, curHp + h);  // 생명력을 회복 (최대 생명력 초과 방지)
        }
    }
    return true;  // 던전을 무사히 통과한 경우
}

ll minimumMaxHp(int n, ll initialAtk, const vector<tuple<int, ll, ll>>& rooms) {
    ll low = 1, high = 1e18;  // 이분 탐색 범위 설정
    ll result = high;

    while (low <= high) {
        ll mid = (low + high) / 2;  // 중간 값을 계산
        if (canSurvive(mid, initialAtk, rooms)) {  // 중간 값으로 던전을 통과 가능한지 확인
            result = mid;  // 가능한 경우 결과 갱신
            high = mid - 1;  // 더 작은 범위를 탐색
        } else {
            low = mid + 1;  // 불가능한 경우 더 큰 범위를 탐색
        }
    }
    return result;  // 최소 HMaxHP 반환
}

int main() {
    int n;
    ll initialAtk;
    cin >> n >> initialAtk;

    vector<tuple<int, ll, ll>> rooms(n);
    for (int i = 0; i < n; ++i) {
        int t;
        ll a, h;
        cin >> t >> a >> h;
        rooms[i] = make_tuple(t, a, h);  // 방 정보 저장
    }

    cout << minimumMaxHp(n, initialAtk, rooms) << endl;  // 결과 출력
    return 0;
}
