A = input("Please enter a word:")# took input from user 

count = {"a": 0 , "e": 0 ,"i":0 , "o":0, "u":0 }# created a dict with a,e,i,o,u



for i in A:
# if found any vowel increment its value in count
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
            count[i] +=1
else:
                pass
# to print only those vowels that have been found in string with their values 
for element in count.items():
    if element[1]!=0:
        print(element[0],element[1])



