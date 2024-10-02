using System; // 표준 입출력 및 기본 라이브러리 사용을 위한 네임스페이스
using System.Linq; // 정렬과 같은 LINQ 함수 사용을 위한 네임스페이스

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()); // 첫 번째 줄에서 저울추의 개수 입력 받기
        
        int[] weights = Array.ConvertAll(Console.ReadLine().Split(), int.Parse); // 두 번째 줄에서 저울추의 무게 배열을 공백 기준으로 분리하여 정수 배열로 변환
        
        Array.Sort(weights); // 저울추의 무게를 오름차순으로 정렬
        
        int target = 1; // 만들 수 없는 최소 무게를 추적하기 위한 변수, 초기값은 1

        foreach (int weight in weights) // 정렬된 저울추 배열을 순회
        {
            if (weight > target) // 현재 저울추의 무게가 target보다 크다면
                break; // 만들 수 없는 최소 무게는 target이므로 반복문 종료
            
            target += weight; // 현재 저울추의 무게를 target에 더해주어 누적
        }

        Console.WriteLine(target); // 최종적으로 계산된 만들 수 없는 최소 무게를 출력
    }
}