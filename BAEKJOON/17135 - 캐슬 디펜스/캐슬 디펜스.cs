using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static int SimulateAttack(int N, int M, int D, int[][] board, int[] archers) {
        int count = 0;
        int[][] enemies = board.Select(row => row.ToArray()).ToArray(); // 보드 복사
        
        while (enemies.Any(row => row.Any(cell => cell == 1))) { // 적이 남아있으면 계속 진행
            HashSet<(int, int)> targets = new HashSet<(int, int)>(); // 공격할 적의 좌표를 저장
            
            foreach (int archer in archers) {
                int minDist = D + 1;
                (int r, int c) target = (-1, -1);
                
                for (int r = 0; r < N; r++) {
                    for (int c = 0; c < M; c++) {
                        if (enemies[r][c] == 1) {
                            int dist = Math.Abs(N - r) + Math.Abs(archer - c);
                            if (dist <= D && (dist < minDist || (dist == minDist && c < target.c))) {
                                minDist = dist;
                                target = (r, c);
                            }
                        }
                    }
                }
                
                if (target.r != -1) targets.Add(target);
            }
            
            foreach (var t in targets) {
                if (enemies[t.Item1][t.Item2] == 1) {
                    enemies[t.Item1][t.Item2] = 0;
                    count++;
                }
            }
            
            for (int r = N - 1; r > 0; r--) {
                enemies[r] = enemies[r - 1];
            }
            enemies[0] = new int[M]; // 첫 행은 빈 칸으로 초기화
        }
        
        return count;
    }

    static int CastleDefense(int N, int M, int D, int[][] board) {
        int maxKills = 0;
        var archers = new int[3];
        
        for (int i = 0; i < M; i++) {
            for (int j = i + 1; j < M; j++) {
                for (int k = j + 1; k < M; k++) {
                    archers[0] = i;
                    archers[1] = j;
                    archers[2] = k;
                    maxKills = Math.Max(maxKills, SimulateAttack(N, M, D, board, archers));
                }
            }
        }
        
        return maxKills;
    }

    static void Main(string[] args) {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0], M = input[1], D = input[2];
        
        int[][] board = new int[N][];
        for (int i = 0; i < N; i++) {
            board[i] = Console.ReadLine().Split().Select(int.Parse).ToArray();
        }
        
        Console.WriteLine(CastleDefense(N, M, D, board));
    }
}