
def merge(nums1: list[int], m: int, nums2: list[int],n):

    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m-=1
        else:
            nums1[m+n-1] = nums2[n-1]
            n-=1
    if n > 0 :
        nums1[:n]= nums2[:n]
    
    print(nums1)


    # """
    # Do not return anything, modify nums1 in-place instead.

    # """

    # nums1 = nums1[:m]
    # if nums1==[]:

    #     nums1==nums2
    #     print(nums1)
    #     return
    # if m == 0:
        

#     nums1 = nums1[:m]   
        
#     for i in range (n):

#         j=0
#         for index, n in enumerate(nums1):
            
            
#             if nums2[i] <= n :
#                 nums1.insert(index,nums2[i])
                
#                 break
#             j = index
#         if j  == len(nums1)-1:
#             nums1.append(nums2[i])
        
#     print (nums1)
        
merge([0],0,[1],1)
        




