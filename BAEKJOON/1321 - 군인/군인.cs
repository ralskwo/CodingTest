using System;

class SegmentTree {
    public int size;           // 세그먼트 트리의 크기
    public int[] tree;         // 세그먼트 트리를 저장할 배열

    // 세그먼트 트리 초기화
    public SegmentTree(int n) {
        size = 1;
        // 주어진 n보다 크거나 같은 가장 가까운 2의 제곱수로 설정
        while (size < n) size *= 2;
        // 트리 배열을 0으로 초기화
        tree = new int[2 * size];
    }

    // 주어진 배열을 세그먼트 트리에 빌드
    public void Build(int[] arr) {
        // 입력 배열을 리프 노드에 삽입
        for (int i = 0; i < arr.Length; i++) {
            tree[size + i] = arr[i];
        }
        // 부모 노드들을 초기화
        for (int i = size - 1; i > 0; i--) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    // 특정 인덱스의 값을 value만큼 업데이트
    public void Update(int index, int value) {
        // 리프 노드의 위치로 이동
        index += size;
        tree[index] += value; // 값 변경
        // 부모 노드로 거슬러 올라가며 값 갱신
        while (index > 1) {
            index /= 2; // 부모 노드로 이동
            tree[index] = tree[2 * index] + tree[2 * index + 1]; // 자식 노드의 합으로 갱신
        }
    }

    // 특정 군번이 속한 부대를 찾는 함수
    public int Query(int soldier) {
        if (soldier > tree[1]) return -1; // 군번이 전체 군인 수를 초과하면 -1 반환
        int index = 1; // 루트 노드에서 시작
        // 리프 노드에 도달할 때까지 반복
        while (index < size) {
            if (soldier <= tree[2 * index]) {
                index = 2 * index; // 왼쪽 자식으로 이동
            } else {
                soldier -= tree[2 * index]; // 왼쪽 자식 노드의 군사 수를 soldier에서 뺌
                index = 2 * index + 1; // 오른쪽 자식으로 이동
            }
        }
        return index - size + 1; // 부대 번호 반환
    }
}

class Program {
    static void Main(string[] args) {
        // 부대의 개수 입력
        int n = int.Parse(Console.ReadLine());
        // 각 부대의 군사 수 입력
        int[] soldiers = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);

        // 세그먼트 트리 생성 및 초기화
        SegmentTree segTree = new SegmentTree(n);
        segTree.Build(soldiers);

        // 명령의 개수 입력
        int m = int.Parse(Console.ReadLine());
        for (int i = 0; i < m; i++) {
            // 명령어 입력
            string[] query = Console.ReadLine().Split(' ');
            if (query[0] == "1") {
                // "1 i a" 명령 처리
                int index = int.Parse(query[1]) - 1; // 0-based 인덱스 변환
                int value = int.Parse(query[2]);
                segTree.Update(index, value); // 업데이트 수행
            } else if (query[0] == "2") {
                // "2 i" 명령 처리
                int soldier = int.Parse(query[1]);
                Console.WriteLine(segTree.Query(soldier)); // 군번이 속한 부대 번호 출력
            }
        }
    }
}