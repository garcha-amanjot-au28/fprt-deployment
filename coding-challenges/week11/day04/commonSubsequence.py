# Q-3 ) Longest Common Subsequence - Solve using DP

def commonSub(text1,text2):

    def helper(text1,text2,i,j):
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i]  == text2[j] :
            return 1 + helper(text1,text2,i+1,j+1)

        else:
            return max (helper(text1,text2,i+1,j) , helper(text1,text2,i,j+1))








    return helper(text1,text2,0,0)

if __name__ == '__main__':
    print(commonSub('abcdef', 'bdf'))