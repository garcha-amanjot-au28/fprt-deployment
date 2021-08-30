class Solution :
    def flipAndInvert(self,image):
        return [[1^i for i in reversed(row)]for row in image]
if __name__ == '__main__':
    ans = Solution()
    print(ans.flipAndInvert([[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]))