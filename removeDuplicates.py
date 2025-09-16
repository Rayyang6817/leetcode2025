class Solution(object):
    def removeDuplicates(self, nums):
        #定義好起始位置讓他可以比較
        startpoint = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[startpoint]:
                startpoint += 1
                nums[startpoint] = nums[i]
        return startpoint + 1
    
    
# Input: nums = [1,1,2]
#testcase   

if __name__ == "__main__":
    s = Solution()
    result = s.removeDuplicates([1, 1, 2])
    print(result)  # ➜ 應該輸出 2
    

#做個小筆記 這就是考你array的處理方式
#不難其實蠻好理解的 你只要指向第一個(0)
#然後從1開始比較 如果不一樣就把startpoint往前移一格
#然後把不一樣的值放到startpoint的位置
#最後回傳startpoint+1(因為index是從0開始)
