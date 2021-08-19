
def uniqueLetterString( s):
       res=lastdp=0
       letter=[[-1,-1] for _ in range(26)]#(rightmost,secondright)
       for i in range(len(s)):
           t,m=letter[ord(s[i])-ord('A')]
           lastdp+=i-2*t+m
           res+=lastdp#current dp[i]
           letter[ord(s[i])-ord('A')]=[i,t]#update letter 
       return res%(10**9 + 7)
       

if __name__ == '__main__':

    print(uniqueLetterString("ABC"))