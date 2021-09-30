class Palindrome:
    def __init__ (self):
        pass

    def shortestPalindrome(self, arr):
        dup = []
        
        for i in arr:
            if i in dup:
                dup.remove(i)
            else:
                dup.append(i)
        if len(arr) % 2 == 0:
            if dup != []:
                return -1
        else:
            if len(dup)>1:
                return -1
        arr = list(arr)
        result = self.makePalindrome(0,len(arr)-1,arr)
        return result   
        
    def makePalindrome(self,front,back,arr):
        count = 0
        while front < back:
            if arr[front] == arr[back]:

                front+=1
                back -= 1
            else:
                position = self.finder(arr,arr[back],front,back)
                if position == False:
                    arr[back] , arr[back-1] = arr[back-1] , arr[back]
                    count+=1
                else:
                    new = self.swap(position,arr,front)
                    count += int(new[0])
                    arr = new[1]
                    front+=1
                    back-=1
            result = self.isPalindrome(arr)
            if result == True:
                return count
            

        
        
            

        


                    

    def finder(self, arr,target,front,back):
        i = front+1
        while i < back-1:
            if arr [i] == target :
                return i
            i+=1
        return False
        
    
    def swap(self, target,arr,front):
        count = 0
        i = target
        mover = arr[target]
        while arr[front]  != mover:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            count += 1
            i-=1
        return [count,arr]




    def isPalindrome (self,arr):
        i = 0
        j = len(arr)-1
        while i < j :
            if arr[i] != arr[j]:

                return False
            i+=1
            j-=1

        return True
if __name__ == '__main__':
    d = Palindrome()
    print(d.shortestPalindrome("mamad"))
    print(d.shortestPalindrome("aabb"))

        
    

        