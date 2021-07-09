#Given a non-empty array of integers nums, every element appears twice except for one. 
# program to Find that single one.
nums = [4,1,2,1,2]

no_dups = []

for i in nums :
    if i in no_dups:
        no_dups.remove(i)
    else :
        no_dups.append(i)

no_dups=int("".join(map(str, no_dups)))
print(no_dups)