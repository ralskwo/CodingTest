using System;
using System.Collections.Generic;

class Program
{
    static bool CanSurvive(long maxHp, long initialAtk, List<(int, long, long)> rooms)
    {
        long curHp = maxHp;   // 현재 생명력은 최대 생명력으로 초기화
        long curAtk = initialAtk; // 현재 공격력은 초기 공격력으로 초기화

        foreach (var room in rooms)
        {
            int type = room.Item1;
            long a = room.Item2;
            long h = room.Item3;

            if (type == 1)  // 몬스터 방
            {
                long turnsToKillMonster = (h + curAtk - 1) / curAtk;  // 몬스터를 죽이는 데 필요한 턴 수
                long damageTaken = (turnsToKillMonster - 1) * a;  // 몬스터로부터 받는 총 피해
                curHp -= damageTaken;  // 생명력에서 피해를 차감
                if (curHp <= 0) return false;  // 생명력이 0 이하로 떨어지면 던전을 통과할 수 없음
            }
            else if (type == 2)  // 포션 방
            {
                curAtk += a;  // 공격력 증가
                curHp = Math.Min(maxHp, curHp + h);  // 생명력을 회복 (최대 생명력 초과 방지)
            }
        }
        return true;  // 던전을 무사히 통과한 경우
    }

    static long MinimumMaxHp(int n, long initialAtk, List<(int, long, long)> rooms)
    {
        long low = 1, high = (long)1e18;  // 이분 탐색 범위 설정
        long result = high;

        while (low <= high)
        {
            long mid = (low + high) / 2;  // 중간 값을 계산
            if (CanSurvive(mid, initialAtk, rooms))  // 중간 값으로 던전을 통과 가능한지 확인
            {
                result = mid;  // 가능한 경우 결과 갱신
                high = mid - 1;  // 더 작은 범위를 탐색
            }
            else
            {
                low = mid + 1;  // 불가능한 경우 더 큰 범위를 탐색
            }
        }
        return result;  // 최소 HMaxHP 반환
    }

    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        long initialAtk = long.Parse(input[1]);

        var rooms = new List<(int, long, long)>();
        for (int i = 0; i < n; i++)
        {
            var roomInput = Console.ReadLine().Split();
            int t = int.Parse(roomInput[0]);
            long a = long.Parse(roomInput[1]);
            long h = long.Parse(roomInput[2]);
            rooms.Add((t, a, h));  // 방 정보 저장
        }

        Console.WriteLine(MinimumMaxHp(n, initialAtk, rooms));  // 결과 출력
    }
}
