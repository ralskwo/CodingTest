#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

// 트리 노드 구조체 정의
struct TreeNode {
    char val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(char x) : val(x), left(NULL), right(NULL) {}
};

// 프리오더와 인오더를 사용하여 트리를 구축하는 함수
TreeNode* buildTreeHelper(const string& preorder, int preStart, int preEnd, 
                          const string& inorder, int inStart, int inEnd, 
                          unordered_map<char, int>& inMap) {
    if (preStart > preEnd || inStart > inEnd) return NULL;
    
    // 프리오더의 첫 번째 요소는 루트 노드입니다.
    char rootVal = preorder[preStart];
    TreeNode* root = new TreeNode(rootVal);
    
    // 인오더 리스트에서 루트 노드의 인덱스를 찾습니다.
    int inRoot = inMap[rootVal];
    int numsLeft = inRoot - inStart;
    
    // 재귀적으로 왼쪽과 오른쪽 서브트리를 구축합니다.
    root->left = buildTreeHelper(preorder, preStart + 1, preStart + numsLeft, 
                                 inorder, inStart, inRoot - 1, inMap);
    root->right = buildTreeHelper(preorder, preStart + numsLeft + 1, preEnd, 
                                  inorder, inRoot + 1, inEnd, inMap);
    
    return root;
}

// 주어진 프리오더와 인오더를 사용하여 트리를 구축하는 함수
TreeNode* buildTree(const string& preorder, const string& inorder) {
    unordered_map<char, int> inMap;
    for (int i = 0; i < inorder.size(); ++i) {
        inMap[inorder[i]] = i;
    }
    return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, inMap);
}

// 트리를 후위 순회하는 함수
void postorderTraversal(TreeNode* root, string& result) {
    if (root == NULL) return;
    postorderTraversal(root->left, result);
    postorderTraversal(root->right, result);
    result += root->val;
}

int main() {
    string input;
    vector<string> results;

    while (getline(cin, input)) {
        // 입력 데이터를 공백으로 분할합니다.
        vector<string> data;
        size_t pos = 0;
        while ((pos = input.find(' ')) != string::npos) {
            data.push_back(input.substr(0, pos));
            input.erase(0, pos + 1);
        }
        data.push_back(input);

        for (size_t i = 0; i < data.size(); i += 2) {
            string preorder = data[i];
            string inorder = data[i + 1];
            TreeNode* tree = buildTree(preorder, inorder);
            string result;
            postorderTraversal(tree, result);
            results.push_back(result);
        }
    }

    for (const string& result : results) {
        cout << result << endl;
    }

    return 0;
}
