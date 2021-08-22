def subsetXORSum( nums: list[int]):
        
        
    bits = 0
    for a in nums:
        bits |= a
    return bits * int(pow(2, len(nums)-1))


if __name__ == '__main__':
    
    nums = [5,1,6]
    print(subsetXORSum(nums))
