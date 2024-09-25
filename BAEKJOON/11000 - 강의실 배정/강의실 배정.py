import heapq
import sys

def solve():
    input = sys.stdin.read  # 입력을 한 번에 읽어옴
    data = input().splitlines()  # 입력 데이터를 줄 단위로 분리하여 리스트로 저장

    n = int(data[0])  # 첫 번째 줄에서 수업의 개수를 입력받아 정수로 변환

    classes = []  # 수업의 시작 시간과 종료 시간을 저장할 리스트
    for i in range(1, n + 1):  # 각 수업에 대해 반복
        start, end = map(int, data[i].split())  # 시작 시간과 종료 시간을 정수로 변환하여 각각 저장
        classes.append((start, end))  # (시작 시간, 종료 시간) 형태로 리스트에 추가
    
    classes.sort(key=lambda x: x[0])  # 수업들을 시작 시간 기준으로 오름차순 정렬

    heap = []  # 수업의 종료 시간을 저장할 최소 힙 리스트

    heapq.heappush(heap, classes[0][1])  # 첫 번째 수업의 종료 시간을 힙에 추가

    for i in range(1, n):  # 두 번째 수업부터 처리
        if heap[0] <= classes[i][0]:  # 현재 가장 빨리 끝나는 수업의 종료 시간과 새 수업의 시작 시간을 비교
            heapq.heappop(heap)  # 겹치지 않으면 기존 수업의 종료 시간을 힙에서 제거

        heapq.heappush(heap, classes[i][1])  # 새로운 수업의 종료 시간을 힙에 추가

    print(len(heap))  # 힙에 남아 있는 종료 시간의 개수가 필요한 최소 강의실 수

if __name__ == "__main__":
    solve()  # 프로그램의 시작점을 명시하고 solve 함수를 호출
