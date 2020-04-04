class Solution:
    from itertools import permutations
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = len(nums) - 1
        for i in range(i, 0, -1):
            if nums[i-1] < nums[i]:
                flag = 1
                break
        i -= 1

        if flag == 0:
            self.reverse(nums, 0)
        else:
            j = len(nums) - 1
            for j in range(j, i, -1):
                if nums[j] <= nums[i]:
                    continue
                else:
                    break

            self.swap(nums, i, j)
            
            self.reverse(nums, i+1)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while(i<j):
            if nums[i] > nums[j]:
                self.swap(nums, i, j)
            i += 1
            j -= 1