class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        res=[]
        mid = n//2
        print("mid",mid)
        count,i,j=0,0,0
        while count<=mid:
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                print("COUNT NUMS1:",count,"=",nums1[i])
                res.append(nums1[i])
                i+=1
                    
            else:
                print("COUNT NUMS2:",count,"=",nums2[j])
                res.append(nums2[j])
                j+=1
                    
            count+=1
        
        if n%2 == 0:
            return (res[-1]+res[-2])/2
        else:
            return res[-1]
            


            