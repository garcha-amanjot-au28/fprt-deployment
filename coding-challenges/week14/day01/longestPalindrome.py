class Solution :
    
    def longestPalindrome(self,s):

        hash = set()

        for c in s:

            if c in hash :

                hash.remove(c)

            else:

                hash.add(c)

        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

if __name__ == '__main__':

    res = Solution()

    print(res.longestPalindrome("abccccdd"))






