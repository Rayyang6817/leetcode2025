
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [2,7,11,15]
# target = 9
# seen = {} # dic 看過的存起來(index跟num)

# if __name__ == "__main__":
#     s = Solution()
#     result = s.two_sum([2, 7, 11, 15], 9)
#     print(result)  # ➜ 應該輸出 [0, 1]


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            diff  = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index 
            
