# 🧩 LeetCode 49 - Group Anagrams
# 📌 題目說明
# 給定一組字串 strs，將**異位詞（Anagrams）**歸成一組。

# 異位詞定義：兩字串只要排序後字母相同，即為異位詞
# 例如 "eat"、"tea"、"ate" 都屬於同一組

# 🧠 解題思路
# 用一個 dict 做分組（群組 key 相同的字串）

# 每個字串排序後（如 "eat" → ('a','e','t')），當作 不可變 key

# 將原始字串丟進對應的 list 裡

# 最後輸出所有分組結果（dict 的 values）

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):  # ✅ 補上 self
        result = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            result[key].append(s)
        return list(result.values())

if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = s.groupAnagrams(strs)
    print(result)
    
    
# 🔍 補充說明
# 使用 tuple(sorted(s)) 作為 dict 的 key，因為：

# tuple 是 不可變（immutable），可以當 dict key

# list 是可變的，不能當 key

# 使用 defaultdict(list) 是為了避免先檢查 key 是否存在

# 📦 資料結構總結：
# {
#   ('a','e','t'): ['eat', 'tea', 'ate'],
#   ('a','n','t'): ['tan', 'nat'],
#   ('a','b','t'): ['bat']
# }
# 外層是 dict

# key 是排序後的 tuple

# value 是一個 list，裝入對應的異位詞群組