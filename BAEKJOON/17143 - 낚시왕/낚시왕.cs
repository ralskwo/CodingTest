using System;
using System.Collections.Generic;

class Shark {
    public int speed;
    public int direction;
    public int size;
}

class Program {
    static int[] dr = { -1, 1, 0, 0 }; // 상하좌우 이동 방향
    static int[] dc = { 0, 0, 1, -1 };
    
    static int R, C, M; // 격자 크기와 상어 수
    static Dictionary<(int, int), Shark> sharks = new Dictionary<(int, int), Shark>(); // 상어 정보 저장
    
    // 상어 이동 함수
    static void MoveSharks() {
        Dictionary<(int, int), Shark> newSharks = new Dictionary<(int, int), Shark>(); // 이동 후 상어 저장

        foreach (var entry in sharks) {
            int r = entry.Key.Item1;
            int c = entry.Key.Item2;
            Shark shark = entry.Value;

            int speed = shark.speed;
            int direction = shark.direction;
            int size = shark.size;

            int nr = r, nc = c;

            // 위, 아래 이동 처리
            if (direction == 1 || direction == 2) {
                speed %= (R - 1) * 2; // 주기성을 이용한 속도
                for (int i = 0; i < speed; ++i) {
                    if (nr == 0 && direction == 1) direction = 2;
                    else if (nr == R - 1 && direction == 2) direction = 1;
                    nr += dr[direction - 1];
                }
            }
            // 좌우 이동 처리
            else {
                speed %= (C - 1) * 2; // 주기성을 이용한 속도
                for (int i = 0; i < speed; ++i) {
                    if (nc == 0 && direction == 4) direction = 3;
                    else if (nc == C - 1 && direction == 3) direction = 4;
                    nc += dc[direction - 1];
                }
            }

            // 상어가 이동 후 겹치면 가장 큰 상어만 남기기
            if (newSharks.ContainsKey((nr, nc))) {
                if (newSharks[(nr, nc)].size < size) {
                    newSharks[(nr, nc)] = new Shark { speed = speed, direction = direction, size = size };
                }
            } else {
                newSharks[(nr, nc)] = new Shark { speed = speed, direction = direction, size = size };
            }
        }

        sharks = newSharks; // 상어 상태 업데이트
    }

    static void Main() {
        string[] input = Console.ReadLine().Split();
        R = int.Parse(input[0]);
        C = int.Parse(input[1]);
        M = int.Parse(input[2]);

        // 상어 정보 입력
        for (int i = 0; i < M; i++) {
            input = Console.ReadLine().Split();
            int r = int.Parse(input[0]) - 1;
            int c = int.Parse(input[1]) - 1;
            int s = int.Parse(input[2]);
            int d = int.Parse(input[3]);
            int z = int.Parse(input[4]);
            sharks[(r, c)] = new Shark { speed = s, direction = d, size = z };
        }

        int totalSize = 0;

        // 낚시왕이 1번 열부터 마지막 열까지 이동
        for (int kingPos = 0; kingPos < C; kingPos++) {
            // 해당 열에서 가장 가까운 상어 잡기
            for (int row = 0; row < R; row++) {
                if (sharks.ContainsKey((row, kingPos))) {
                    totalSize += sharks[(row, kingPos)].size; // 상어 크기 합산
                    sharks.Remove((row, kingPos)); // 상어 제거
                    break;
                }
            }

            // 상어 이동 처리
            MoveSharks();
        }

        // 결과 출력
        Console.WriteLine(totalSize);
    }
}
