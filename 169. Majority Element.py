# 解題思路 其實都不管是什麼數字，只要出現次數超過一半的數字就可以了
# 用DICT來記錄次數就好
# 主要是練習於法 可以get當前key的值，沒有的話就給0
# 但如果已經有num 他預設就不會是0 再直接+1
# 所以就會有每個數字出現的次數
# 如果某個數字的次數大於len(nums) // 2 就回傳該數字

class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
            if count[num] > len(nums) // 2:
                return num
            
test = Solution()
# test_case = [3, 2, 3]
test_case2 = [2, 2, 1, 1, 1, 2, 2]
resutlt = test.majorityElement(test_case2)  
print(resutlt)  # 輸出結果