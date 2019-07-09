import numpy as np

def LCS(s1, s2):
    sequence_memory = np.empty([len(s1), len(s2)], dtype = object)
    return LCS_re(s1, s2, 0, 0, sequence_memory)

def LCS_re(s1, s2, s1_index, s2_index, sequence_memory):
    if s1_index == len(s1) or s2_index == len(s2):
        return ""

    if sequence_memory[s1_index, s2_index] != None:
        return sequence_memory[s1_index, s2_index]

    if s1[s1_index] == s2[s2_index]:
        lcs = s1[s1_index] + LCS_re(s1, s2, s1_index+1, s2_index+1, sequence_memory)
    else:
        lcs_1 = LCS_re(s1, s2, s1_index+1, s2_index, sequence_memory)
        lcs_2 = LCS_re(s1, s2, s1_index, s2_index+1, sequence_memory)
        if len(lcs_1) > len(lcs_2):
            lcs = lcs_1
        else:
            lcs = lcs_2
        
    sequence_memory[s1_index, s2_index] = lcs
    return lcs
        

if __name__=="__main__":
    s1 = "123123123123123123"
    s2 = "7123812731237812935"

    lcs = LCS(s1, s2)
    print(lcs)
    