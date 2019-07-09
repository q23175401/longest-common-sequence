# longest-common-sequence
使用python 實現的 最長相同子序列

說明:
  1. 使用dynamic programming，完成Longest common sequence


程式說明:
  1. LCS_re(s1, s2, s1i, s2i)
  2. 將會從 s1[s1i] 和 s2[s2i] 開始逐一比對
  3. 當有重複字元出現，最長子序列為 c + LCS_re(s1, s2, s1i+1, s2i+1)  ， c為重複的字元
  4. 當兩個字元不重複時，最長子序列可能為
  
        a. LCS_re(s1, s2, s1i+1, s2i)  ， 有可能 s1[s1i] 不是子序列的一個字元
        
        b. LCS_re(s1, s2, s1i, s2i+1)  ， 有可能 s2[s2i] 不是子序列的一個字元
        
        c. 比較兩個出來的結果的長度，比較長的是我們要的
  5. 透過遞迴，最後可以找出LCS
  6. 並且透過 sequence_memory 動態的在遞迴時記住 已經出現過的 子序列組合，降低時間複雜度
  
  
時間複雜度: O(L * M),  L = len(s1) M = len(s2)

空間複雜度: O(L * M),  L = len(s1) M = len(s2)
