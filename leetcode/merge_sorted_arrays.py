class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2 = nums2[:n]
        i=0
        j=0
        k=0

        while i < m and j < n:
            #ako je broj iz num1 manji, ostavi kako je
            if nums1[i]<=nums2[j]:
                k+=1
                i+=1
            #
            else:
                nums1.insert(k, nums2[j]) #na indeks k dodat taj broj iz nums2
                k+=1
                j+=1
                i+=1
                m+=1

        #nadodaj ostatak
        if i >= m: #prva lista je dosla do kraja, dodaj drugu
            nums1.extend(nums2[j:])


nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
solution = Solution()

solution.merge(nums1, m, nums2, n)
print(nums1)

#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150