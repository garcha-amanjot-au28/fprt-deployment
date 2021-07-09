nums = [3,3,4]
count= {}

for i in nums :
    if not i in count:
        count[i] = 1
    else:
        count[i] +=1

max =0
maj = 0 
for i in count :
    
    
    if count[i] >  max :
        maj = i
        max  = count[i]

        # print(max)
    
print (maj)
