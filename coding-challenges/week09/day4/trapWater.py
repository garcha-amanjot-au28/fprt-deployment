#Q-2 )Trapping Rain Water
# solving it by using a stack named index storing the index numbers 
# calculating the amount of trapped water from right highest to left highest one elemnet at time 
#and adding to result
# time complexity o(n) space complexity o(n)
def trapWater(height):

    result = 0
    index = []

    for i , val in enumerate(height):

        while index != [] and val > height[index[-1]]:

            top = index.pop()  # poping the last ele in index and storing it as top

            if index == []:
                break

            distance = i - index[-1] - 1  

            bounded_height = min ( val,height[index[-1]]) - height[top]
            # calculating bounded height by taking smaller of current height and last ele in index 
            # and subtracting height in middle 

            result += distance * bounded_height

        index.append(i)
        
    return result

print (trapWater([4,2,0,3,2,5]))

