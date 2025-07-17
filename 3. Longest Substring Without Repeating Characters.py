# LeetCode 3. Longest Substring Without Repeating Characters
# 解題思路：
# ---------------------------------------
# 這題的目標是找出「最長的不重複子字串長度」
# 我們會使用「滑動視窗」+「dict 紀錄每個字母出現的位置」
#
# ✅ 為什麼用 enumerate？
#    因為我們需要紀錄每個字母的 index，這樣才能計算長度。
#
# ✅ 為什麼用 dict？
#    用來記住每個字母「最後一次出現」的位置，當遇到重複時就能正確更新起始點。
#
# ✅ 為什麼要加 if c in index_dict and index_dict[c] >= start?
#    因為只有當這個字母已出現「而且出現在目前 window 內」時，才要滑動 window。
#
# ✅ 為什麼要更新 start？
#    因為要把滑動視窗的起點移到「重複字元的下一個位置」，才能保證子字串不重複。
#
# ✅ 為什麼最後用 max_len = max(max_len, i - start + 1)？
#    因為每一步都要計算目前視窗的長度，並保留最大值。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_dict = {}     # 紀錄字母最後一次出現的位置
        max_len = 0         # 紀錄最大長度
        start = 0           # 視窗的起始點

        for i, c in enumerate(s):
            # 若 c 出現過，且位置 >= start，代表視窗內出現重複字元，需要滑動視窗
            if c in index_dict and index_dict[c] >= start:
                start = index_dict[c] + 1  # 將視窗起點移到重複字元下一個位置

            index_dict[c] = i              # 更新字母出現的位置
            max_len = max(max_len, i - start + 1)  # 更新最大長度

        return max_len

# 範例測試
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
    print(s.lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
    print(s.lengthOfLongestSubstring("pwwkew"))     # Output: 3 ("wke")
    print(s.lengthOfLongestSubstring("abba"))       # Output: 2 ("ab" or "ba")
