class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        i = 0
        while i in range(0, len(nums)):
            if runningSum:
                newSum = nums[i] + runningSum[i - 1]
                runningSum.append(newSum)
            else:
                runningSum.append(nums[i])
            i += 1
        return runningSum
