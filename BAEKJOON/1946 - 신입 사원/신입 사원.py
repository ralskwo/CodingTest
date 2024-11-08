import sys
input = sys.stdin.read

def max_hires(candidates):
    # 서류 심사 성적 순위를 기준으로 지원자 목록을 오름차순 정렬
    candidates.sort()
    
    # 첫 번째 지원자는 무조건 선발되므로 최대 인원을 1로 초기화
    max_count = 1
    
    # 첫 번째 지원자의 면접 순위를 최소 면접 순위로 설정
    min_interview_rank = candidates[0][1]
    
    # 두 번째 지원자부터 마지막 지원자까지 순회하며 선발 여부 결정
    for i in range(1, len(candidates)):
        # 현재 지원자의 면접 순위가 이전까지의 최소 면접 순위보다 높으면 선발
        if candidates[i][1] < min_interview_rank:
            # 선발된 인원수를 1 증가
            max_count += 1
            # 최소 면접 순위를 현재 지원자의 면접 순위로 갱신
            min_interview_rank = candidates[i][1]
            
    # 선발된 최대 인원수를 반환
    return max_count

def main():
    # 전체 입력 데이터를 줄 단위로 읽어 리스트로 변환
    data = input().splitlines()
    
    # 첫 줄의 테스트 케이스 개수를 정수로 변환하여 저장
    T = int(data[0])
    
    # 현재 읽고 있는 줄 번호를 나타내는 인덱스 변수 초기화
    idx = 1
    
    # 각 테스트 케이스의 결과를 저장할 리스트 초기화
    results = []
    
    # 테스트 케이스 개수만큼 반복
    for _ in range(T):
        # 각 테스트 케이스의 첫 줄에 있는 지원자 수를 정수로 변환하여 저장
        N = int(data[idx])
        
        # 지원자들의 서류 심사 성적과 면접 순위를 저장할 리스트 초기화
        candidates = []
        
        # 지원자 수만큼 반복하며 지원자의 성적 정보를 읽어옴
        for j in range(1, N + 1):
            # 지원자의 서류 심사 성적과 면접 순위를 공백을 기준으로 분리하여 정수로 변환
            doc_rank, interview_rank = map(int, data[idx + j].split())
            # 변환된 성적 정보를 튜플로 저장하여 candidates 리스트에 추가
            candidates.append((doc_rank, interview_rank))
        
        # 각 테스트 케이스의 최대 선발 인원을 계산하여 결과 리스트에 추가
        results.append(max_hires(candidates))
        
        # 다음 테스트 케이스로 이동하기 위해 인덱스를 현재 케이스의 줄 수만큼 증가
        idx += N + 1
    
    # 모든 테스트 케이스에 대해 최대 선발 인원을 한 줄씩 출력
    for result in results:
        print(result)

# 이 모듈이 직접 실행될 때만 main 함수를 호출
if __name__ == "__main__":
    main()