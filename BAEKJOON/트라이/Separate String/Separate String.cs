using System;
using System.Collections.Generic;

class TrieNode
{
    public Dictionary<char, TrieNode> Children { get; set; }
    public bool IsEndOfWord { get; set; }

    public TrieNode()
    {
        Children = new Dictionary<char, TrieNode>();
        IsEndOfWord = false;
    }
}

class Trie
{
    public TrieNode Root { get; set; }

    public Trie()
    {
        Root = new TrieNode();
    }

    public void Insert(string word)
    {
        TrieNode node = Root;
        foreach (char c in word)
        {
            if (!node.Children.ContainsKey(c))
            {
                node.Children[c] = new TrieNode();
            }
            node = node.Children[c];
        }
        node.IsEndOfWord = true;
    }

    public List<int> Search(string s, int start)
    {
        TrieNode node = Root;
        List<int> results = new List<int>();
        for (int i = start; i < s.Length; ++i)
        {
            char c = s[i];
            if (!node.Children.ContainsKey(c))
            {
                break;
            }
            node = node.Children[c];
            if (node.IsEndOfWord)
            {
                results.Add(i + 1);
            }
        }
        return results;
    }
}

class Program
{
    const int MOD = 1_000_000_007;

    static int CountWays(int N, List<string> S, string t)
    {
        Trie trie = new Trie();
        foreach (string word in S)
        {
            trie.Insert(word);
        }

        int len_t = t.Length;
        int[] dp = new int[len_t + 1];
        dp[0] = 1;

        for (int i = 0; i < len_t; ++i)
        {
            if (dp[i] > 0)
            {
                List<int> matches = trie.Search(t, i);
                foreach (int j in matches)
                {
                    dp[j] = (dp[j] + dp[i]) % MOD;
                }
            }
        }

        return dp[len_t];
    }

    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        List<string> S = new List<string>();

        for (int i = 0; i < N; ++i)
        {
            S.Add(Console.ReadLine());
        }

        string t = Console.ReadLine();

        int result = CountWays(N, S, t);
        Console.WriteLine(result);
    }
}
