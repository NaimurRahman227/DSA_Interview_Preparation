nums = [12 , 34 ,657 , 65 ,99 , 100]
target = 99

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums , target))
