import sys
from collections import defaultdict

def main():
    # 입력을 받기 위해 sys.stdin.read를 사용하여 전체 데이터를 읽음
    input = sys.stdin.read
    # 입력받은 데이터를 줄 단위로 나누어 리스트로 변환
    data = input().splitlines()

    # 첫 번째 줄에서 노드의 수 N과 1번 노드에 고인 물의 양 W를 추출
    N, W = map(int, data[0].split())
    
    # 트리의 연결 관계를 저장할 인접 리스트 형태의 딕셔너리를 생성
    tree = defaultdict(list)
    
    # 두 번째 줄부터 N-1줄까지의 간선 정보를 읽어와 트리 구성
    for line in data[1:]:
        U, V = map(int, line.split())
        tree[U].append(V)  # U 노드에 V 노드를 연결
        tree[V].append(U)  # V 노드에 U 노드를 연결
    
    # 리프 노드(자식이 없는 노드)의 개수를 셀 변수
    leaf_count = 0
    # 2번 노드부터 N번 노드까지 순회하여 리프 노드 찾기
    for node in range(2, N+1):
        # 각 노드의 연결된 노드 개수가 1개인 경우, 해당 노드는 리프 노드
        if len(tree[node]) == 1:
            leaf_count += 1
    
    # 리프 노드의 개수로 1번 노드의 물을 나누어 각 리프 노드에 고이는 물의 양을 계산
    result = W / leaf_count
    # 결과를 소수점 10자리까지 출력
    print(f"{result:.10f}")

if __name__ == "__main__":
    # main 함수 호출
    main()
