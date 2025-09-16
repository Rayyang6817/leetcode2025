# 題目  
# 給定一個整數陣列 nums，將所有 0 移動到陣列的末尾，同時保持非零元素的相對順序。
# 請注意，必須在不使用額外數組的情況下進行操作，並且必須在原地修改輸入陣列。
# 解題思路  
# 1. 使用兩個指針，一個指向當前非零元素的位置，另一個遍歷整個陣列。
# 2. 當遇到非零元素時，將其移動到前面的位置。
# 3. 最後將剩餘的位置填充為零。


class Solution:
    def moveZeroes(self, nums):
        # 指針初始化
        insert_pos = 0
        
        # 遍歷整個陣列
        for i in range(len(nums)):
            if nums[i] != 0:
                # 將非零元素移到前面
                nums[insert_pos] = nums[i]
                insert_pos += 1 
        
        # 將剩餘的位置填充為零
        for i in range(insert_pos, len(nums)):
            nums[i] = 0

# 測試
test = Solution()      
test_case = [0, 1, 0, 3, 12]
test.moveZeroes(test_case)  
print(test_case)    
# 輸出結果應該是 [1, 3, 12, 0, 0]        

# 整個的解題思路詳細解釋：
# 先創造一個pointer 建立在陣列的第一個位置 目的是要判斷當他不是0時 我要把他往前移!!
# 所以他會跟著碰到非0的數量一直增長
# 最後你會知道總共到底跑了多少非0的數量 你再針對陣列長度最後的幾個非0數字去補0
