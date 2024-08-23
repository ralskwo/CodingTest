using System;
using System.Collections.Generic;

public class TreeNode {
    public char val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(char x) { val = x; }
}

public class Program {
    // 프리오더와 인오더를 사용하여 트리를 구축하는 함수
    public static TreeNode BuildTreeHelper(string preorder, int preStart, int preEnd, 
                                           string inorder, int inStart, int inEnd, 
                                           Dictionary<char, int> inMap) {
        if (preStart > preEnd || inStart > inEnd) return null;
        
        // 프리오더의 첫 번째 요소는 루트 노드입니다.
        char rootVal = preorder[preStart];
        TreeNode root = new TreeNode(rootVal);
        
        // 인오더 리스트에서 루트 노드의 인덱스를 찾습니다.
        int inRoot = inMap[rootVal];
        int numsLeft = inRoot - inStart;
        
        // 재귀적으로 왼쪽과 오른쪽 서브트리를 구축합니다.
        root.left = BuildTreeHelper(preorder, preStart + 1, preStart + numsLeft, 
                                    inorder, inStart, inRoot - 1, inMap);
        root.right = BuildTreeHelper(preorder, preStart + numsLeft + 1, preEnd, 
                                     inorder, inRoot + 1, inEnd, inMap);
        
        return root;
    }

    // 주어진 프리오더와 인오더를 사용하여 트리를 구축하는 함수
    public static TreeNode BuildTree(string preorder, string inorder) {
        Dictionary<char, int> inMap = new Dictionary<char, int>();
        for (int i = 0; i < inorder.Length; i++) {
            inMap[inorder[i]] = i;
        }
        return BuildTreeHelper(preorder, 0, preorder.Length - 1, inorder, 0, inorder.Length - 1, inMap);
    }

    // 트리를 후위 순회하는 함수
    public static void PostorderTraversal(TreeNode root, List<char> result) {
        if (root == null) return;
        PostorderTraversal(root.left, result);
        PostorderTraversal(root.right, result);
        result.Add(root.val);
    }

    public static void Main(string[] args) {
        List<string> results = new List<string>();
        string input;
        
        // 입력을 여러 줄로 받습니다.
        while ((input = Console.ReadLine()) != null && input != "") {
            string[] data = input.Split();
            for (int i = 0; i < data.Length; i += 2) {
                string preorder = data[i];
                string inorder = data[i + 1];
                TreeNode tree = BuildTree(preorder, inorder);
                List<char> result = new List<char>();
                PostorderTraversal(tree, result);
                results.Add(new string(result.ToArray()));
            }
        }

        // 결과를 출력합니다.
        foreach (string result in results) {
            Console.WriteLine(result);
        }
    }
}
