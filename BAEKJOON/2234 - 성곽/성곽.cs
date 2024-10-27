using System;
using System.Collections.Generic;

class Castle {
    // 방향 벡터 설정 (서, 북, 동, 남 순서)
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};

    // 벽의 방향을 비트마스킹으로 나타내는 값 (서쪽: 1, 북쪽: 2, 동쪽: 4, 남쪽: 8)
    static int[] DIRECTION_WALL = {1, 2, 4, 8};

    // BFS를 통해 방을 탐색하고 방의 크기를 반환하는 함수
    static int BFS(int startX, int startY, int roomId, int[,] castle, int[,] visited) {
        Queue<(int, int)> queue = new Queue<(int, int)>(); // BFS를 위한 큐
        queue.Enqueue((startX, startY)); // 시작 위치를 큐에 추가
        visited[startX, startY] = roomId; // 시작 위치를 현재 방 ID로 방문 표시
        int roomSize = 1; // 현재 방의 크기 (칸 수)

        // 큐가 빌 때까지 BFS 탐색을 수행
        while (queue.Count > 0) {
            (int x, int y) = queue.Dequeue();

            // 4방향(서, 북, 동, 남)을 순회하며 이동할 수 있는지 확인
            for (int direction = 0; direction < 4; ++direction) {
                int nx = x + dx[direction];
                int ny = y + dy[direction];

                // 성곽 크기 내에 있고, 아직 방문하지 않은 위치인지 확인
                if (nx >= 0 && nx < castle.GetLength(0) && ny >= 0 && ny < castle.GetLength(1) && visited[nx, ny] == 0) {
                    // 현재 위치에서 해당 방향에 벽이 없을 때만 이동
                    if ((castle[x, y] & DIRECTION_WALL[direction]) == 0) {
                        visited[nx, ny] = roomId; // 이동할 위치를 현재 방 ID로 표시
                        queue.Enqueue((nx, ny)); // 큐에 이동할 위치 추가
                        roomSize++; // 방 크기 증가
                    }
                }
            }
        }
        return roomSize; // 최종 방 크기 반환
    }

    static void Main() {
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]); // 성곽의 너비
        int M = int.Parse(input[1]); // 성곽의 높이

        int[,] castle = new int[M, N]; // 성곽의 벽 정보 저장
        int[,] visited = new int[M, N]; // 방문 여부와 방 ID 저장

        // 성곽의 각 칸의 벽 정보 입력
        for (int i = 0; i < M; ++i) {
            input = Console.ReadLine().Split();
            for (int j = 0; j < N; ++j) {
                castle[i, j] = int.Parse(input[j]);
            }
        }

        List<int> roomSizes = new List<int>(); // 각 방의 크기를 저장
        int roomCount = 0; // 방의 개수를 저장

        // 성곽의 각 칸을 순회하며 방 탐색 수행
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                // 아직 방문하지 않은 칸이면 새로운 방으로 간주하고 탐색
                if (visited[i, j] == 0) {
                    roomCount++; // 방의 개수 증가
                    int roomSize = BFS(i, j, roomCount, castle, visited); // BFS로 방 크기 계산
                    roomSizes.Add(roomSize); // 방 크기를 리스트에 추가
                }
            }
        }

        // 가장 넓은 방의 크기 계산
        int maxRoomSize = 0;
        foreach (int size in roomSizes) {
            maxRoomSize = Math.Max(maxRoomSize, size);
        }

        // 벽을 하나 제거하여 얻을 수 있는 최대 방 크기 계산
        int maxCombinedRoomSize = 0;

        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                int currentRoomId = visited[i, j]; // 현재 칸의 방 ID 저장

                // 4방향을 확인하여 인접 방과의 연결 시도
                for (int direction = 0; direction < 4; ++direction) {
                    int ni = i + dx[direction];
                    int nj = j + dy[direction];

                    if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
                        int neighborRoomId = visited[ni, nj]; // 인접 방의 ID 저장

                        // 인접 방이 다른 방일 경우에만 벽을 제거하고 방을 합친 크기 계산
                        if (currentRoomId != neighborRoomId) {
                            int combinedSize = roomSizes[currentRoomId - 1] + roomSizes[neighborRoomId - 1];
                            maxCombinedRoomSize = Math.Max(maxCombinedRoomSize, combinedSize); // 최대 크기 갱신
                        }
                    }
                }
            }
        }

        // 결과 출력: 방의 개수, 가장 넓은 방의 크기, 벽을 제거하여 얻을 수 있는 최대 방 크기
        Console.WriteLine(roomCount);
        Console.WriteLine(maxRoomSize);
        Console.WriteLine(maxCombinedRoomSize);
    }
}