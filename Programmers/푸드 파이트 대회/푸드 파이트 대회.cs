using System;
using System.Text;

class Solution {
    public string solution(int[] food) {
        // 왼쪽에 배치될 음식을 저장할 StringBuilder 객체 생성
        StringBuilder leftSide = new StringBuilder();  

        // 1번 음식부터 마지막 음식까지 반복
        for (int i = 1; i < food.Length; i++) {  
            // 각 음식의 절반만큼의 개수를 계산 (좌우 대칭을 위해)
            int count = food[i] / 2;  
            // 계산된 개수만큼 해당 음식 번호를 문자열로 추가
            leftSide.Append(new string((char)('0' + i), count));  
        }

        // leftSide를 문자열로 변환하여 rightSide로 복사
        string rightSide = new string(leftSide.ToString().ToCharArray());  
        // rightSide를 문자 배열로 변환
        char[] rightSideArray = rightSide.ToCharArray();  
        // 문자 배열을 뒤집어 오른쪽에 배치될 음식 순서를 결정
        Array.Reverse(rightSideArray);  
        // leftSide, 중앙의 물('0'), rightSide를 결합하여 최종 결과 문자열 생성
        string result = leftSide.ToString() + '0' + new string(rightSideArray);  
        // 최종 음식 배치 결과 문자열을 반환
        return result;  
    }
}
