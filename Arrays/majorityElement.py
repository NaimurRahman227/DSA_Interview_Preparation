class Solution(object):
    def majorityElement(self, nums):
        count = 0
        final_result = None

        for num in nums:
            if count == 0:
                final_result = num
            count += (1 if num == final_result else -1)

        return final_result

        

if __name__ == '__main__':
    result = Solution()
    print(result.majorityElement([2 , 4 ,5 ,2, 2, 12 ]))
