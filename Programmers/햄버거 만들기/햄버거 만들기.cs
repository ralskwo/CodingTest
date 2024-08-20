using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] ingredient) {
        List<int> stack = new List<int>();
        int count = 0;
        
        foreach (int item in ingredient) {
            stack.Add(item);
            if (stack.Count >= 4 && stack[stack.Count-1] == 1 && stack[stack.Count-2] == 3 
                && stack[stack.Count-3] == 2 && stack[stack.Count-4] == 1) {
                count++;
                stack.RemoveRange(stack.Count - 4, 4);
            }
        }
        
        return count;
    }
}
