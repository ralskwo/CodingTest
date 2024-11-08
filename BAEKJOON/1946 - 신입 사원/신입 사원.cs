using System;
using System.Collections.Generic;

// 지원자의 서류 성적과 면접 성적 정보를 담는 클래스
class Candidate {
    public int DocRank;      // 서류 순위
    public int InterviewRank; // 면접 순위
}

class Program {
    // 서류 성적을 기준으로 오름차순 정렬하기 위한 비교 함수
    static int CompareByDocRank(Candidate a, Candidate b) {
        return a.DocRank.CompareTo(b.DocRank);
    }

    // 최대 선발 인원을 계산하는 함수
    static int MaxHires(List<Candidate> candidates) {
        // 서류 순위를 기준으로 지원자 목록을 오름차순 정렬
        candidates.Sort(CompareByDocRank);

        // 첫 번째 지원자는 무조건 선발되므로 초기 선발 인원을 1로 설정
        int maxCount = 1;
        // 첫 번째 지원자의 면접 순위를 기준 면접 순위로 설정
        int minInterviewRank = candidates[0].InterviewRank;

        // 두 번째 지원자부터 마지막 지원자까지 순회하며 선발 여부 결정
        for (int i = 1; i < candidates.Count; i++) {
            // 현재 지원자의 면접 순위가 기준 면접 순위보다 높다면 선발
            if (candidates[i].InterviewRank < minInterviewRank) {
                maxCount++; // 선발 인원 증가
                minInterviewRank = candidates[i].InterviewRank; // 기준 면접 순위 갱신
            }
        }

        // 최종적으로 선발된 최대 인원수를 반환
        return maxCount;
    }

    static void Main() {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스 개수 입력 받기

        while (T-- > 0) {
            int N = int.Parse(Console.ReadLine()); // 각 테스트 케이스의 지원자 수

            List<Candidate> candidates = new List<Candidate>(); // 지원자 정보를 저장할 리스트

            // 각 지원자의 서류 및 면접 순위를 입력받아 리스트에 추가
            for (int i = 0; i < N; i++) {
                string[] ranks = Console.ReadLine().Split();
                int docRank = int.Parse(ranks[0]);
                int interviewRank = int.Parse(ranks[1]);
                candidates.Add(new Candidate { DocRank = docRank, InterviewRank = interviewRank });
            }

            // 현재 테스트 케이스의 최대 선발 인원을 출력
            Console.WriteLine(MaxHires(candidates));
        }
    }
}