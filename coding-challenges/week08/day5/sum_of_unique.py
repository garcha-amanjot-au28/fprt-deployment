def sumOfUnique( nums: list[int]):
        dict= {}
        sum = 0
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        print(dict)
        
        for key , i in dict.items():
            if i == 1:
                
                sum = sum + key
        return sum
print(sumOfUnique([1,2,3,2]))