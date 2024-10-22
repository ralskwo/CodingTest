using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 8방향 정의 (↑, ↖, ←, ↙, ↓, ↘, →, ↗)
    static int[] dx = { -1, -1, 0, 1, 1, 1, 0, -1 };
    static int[] dy = { 0, -1, -1, -1, 0, 1, 1, 1 };

    // 물고기 클래스 정의
    class Fish
    {
        public int num, dir;
        public bool alive;
        public Fish(int num, int dir, bool alive)
        {
            this.num = num;
            this.dir = dir;
            this.alive = alive;
        }
        public Fish Clone()
        {
            return new Fish(this.num, this.dir, this.alive);
        }
    }

    static int answer = 0; // 최종 결과를 저장할 전역 변수

    // 물고기 이동 함수
    static void MoveFish(List<List<Fish>> space, int shark_x, int shark_y)
    {
        for (int i = 1; i <= 16; i++) // 1번부터 16번 물고기까지 순서대로 이동
        {
            int fish_x = -1, fish_y = -1;
            for (int x = 0; x < 4; x++)
            {
                for (int y = 0; y < 4; y++)
                {
                    if (space[x][y].num == i && space[x][y].alive)
                    {
                        fish_x = x;
                        fish_y = y;
                        break;
                    }
                }
                if (fish_x != -1) break;
            }

            if (fish_x == -1) continue; // 해당 번호의 물고기가 없으면 다음 물고기로

            int dir = space[fish_x][fish_y].dir;
            for (int d = 0; d < 8; d++) // 최대 8번 방향을 바꿔가며 이동 가능한 칸 찾기
            {
                int nx = fish_x + dx[dir];
                int ny = fish_y + dy[dir];
                if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4 && !(nx == shark_x && ny == shark_y))
                {
                    // 물고기 위치 교환
                    Fish temp = space[fish_x][fish_y];
                    space[fish_x][fish_y] = space[nx][ny];
                    space[nx][ny] = temp;
                    space[nx][ny].dir = dir;
                    break;
                }
                dir = (dir + 1) % 8; // 45도 반시계 회전
            }
        }
    }

    // DFS 함수
    static void DFS(List<List<Fish>> space, int shark_x, int shark_y, int total)
    {
        // 현재 위치의 물고기를 먹음
        total += space[shark_x][shark_y].num;
        int shark_dir = space[shark_x][shark_y].dir;
        space[shark_x][shark_y].alive = false;

        answer = Math.Max(answer, total); // 최대값 갱신

        // 물고기 이동
        MoveFish(space, shark_x, shark_y);

        // 상어 이동
        for (int i = 1; i < 4; i++)
        {
            int nx = shark_x + dx[shark_dir] * i;
            int ny = shark_y + dy[shark_dir] * i;
            if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4 && space[nx][ny].alive)
            {
                // 새로운 공간 생성 (깊은 복사)
                List<List<Fish>> newSpace = space.Select(row => row.Select(fish => fish.Clone()).ToList()).ToList();
                DFS(newSpace, nx, ny, total);
            }
        }
    }

    static void Main(string[] args)
    {
        List<List<Fish>> space = new List<List<Fish>>();

        // 입력 받기
        for (int i = 0; i < 4; i++)
        {
            List<Fish> row = new List<Fish>();
            int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            for (int j = 0; j < 4; j++)
            {
                row.Add(new Fish(input[j * 2], input[j * 2 + 1] - 1, true));
            }
            space.Add(row);
        }

        DFS(space, 0, 0, 0); // DFS 시작

        Console.WriteLine(answer); // 결과 출력
    }
}