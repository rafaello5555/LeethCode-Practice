class Solution:
    def merge(self, nums1, m, nums2, n):
        # Determine position of index of last valid element
        i = m - 1
        j = n - 1     
        k = m + n - 1 
        
        # Sort array by checking conditions of 1-dimensional vectors
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If any elements remain in nums2, they need to be copied into nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

def test_merge():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"Before merging Test Case 1: nums1 = {nums1[:m]}, nums2 = {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merging Test Case 1: nums1 = {nums1} -> Expected Output: [1, 2, 2, 3, 5, 6]")
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(f"\nBefore merging Test Case 2: nums1 = {nums1[:m]}, nums2 = {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merging Test Case 2: nums1 = {nums1} -> Expected Output: [1]")
    
    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(f"\nBefore merging Test Case 3: nums1 = {nums1[:m]}, nums2 = {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merging Test Case 3: nums1 = {nums1} -> Expected Output: [1]")
    
    # Test case 4: Additional case
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    print(f"\nBefore merging Test Case 4: nums1 = {nums1[:m]}, nums2 = {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merging Test Case 4: nums1 = {nums1} -> Expected Output: [1, 2, 3, 4, 5, 6]")
    
    # Test case 5: Duplicate values
    nums1 = [1, 2, 2, 0, 0, 0]
    m = 3
    nums2 = [2, 2, 3]
    n = 3
    print(f"\nBefore merging Test Case 5: nums1 = {nums1[:m]}, nums2 = {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merging Test Case 5: nums1 = {nums1} -> Expected Output: [1, 2, 2, 2, 2, 3]")

# Run the test cases
if __name__ == "__main__":
    test_merge()
