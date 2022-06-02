class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            for i in range(0, len(nums)):
                if nums[i] == target:
                    return i
#This could be improved by implementing binary search starting from the
#middle value in nums and using pointer indices. Suggested solution:

#class Solution:
    #def search(self, nums: List[int], target: int) -> int:
        #left, right = 0, len(nums) - 1
        #while left <= right:
            #pivot = left + (right - left) // 2
            #if nums[pivot] == target:
                #return pivot
            #if target < nums[pivot]:
                #right = pivot - 1
            #else:
                #left = pivot + 1
        #return -1
