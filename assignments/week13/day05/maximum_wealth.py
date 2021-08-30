class New:

    def maximumWealth(self , accounts):
        return max(map(sum , accounts))




if __name__ == '__main__':
    ans = New()
    print(ans.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))