# 📘 LeetCode 題解整理（Python + SQL）

這個專案是我從 2025/7 開始的 LeetCode 刷題紀錄，包含 Python 題解與 SQL 題目整理，並搭配個人理解與註解，幫助複習與展示解題思路。

---

## ✅ 題目列表

| 題號 | 題目名稱 | 類型 | 檔案 | 技術重點 |
|------|----------|------|------|------------|
| 1    | Two Sum | Array | `two_sum.py` | HashMap, Dict 查找 |
| 3    | Longest Substring Without Repeating Characters | Sliding Window | `longest_substring.py` | Dict + 滑動視窗 |
| 49   | Group Anagrams | Hash Table | `group_anagrams.py` | 使用 tuple(sorted) 當 key |
| 169  | Majority Element | Array | `majority_element.py` | Dict 統計, get(key, 0) |
| 176  | Second Highest Salary | SQL | `second_highest_salary.sql` | 子查詢 + LIMIT OFFSET |
| 1280 | Students and Examinations | SQL | `students_exams.sql` | CROSS JOIN + LEFT JOIN + COUNT + GROUP BY |
| 283  | Move Zeroes | Two Pointer | `move_zeroes.py` | Read-Write 指標, 原地操作 |

---

## 🧠 技術筆記補充

- ✅ **Python：**
  - `enumerate`：同時取得 index 與值
  - `dict.get(k, 0)`：簡化計數初始化
  - `tuple(sorted(s))`：不可變 key，適合用在 dict
  - `defaultdict(list)`：自動初始化 list，簡化分組操作
  - `Two Pointer`：移動資料或交換資料時常用技巧，例如一個指標掃描、一個指標寫入（如 Move Zeroes 題目中使用）
    - Move Zeroes 案例：`insert_pos` 作為非 0 元素的寫入位置，`i` 為掃描指標；非 0 元素向前搬移，剩餘位置補 0。

- ✅ **SQL：**
  - `CROSS JOIN`：產生所有組合（學生 × 科目）
  - `LEFT JOIN` + `COUNT(column)`：處理 NULL 計數正確性
  - `LIMIT 1 OFFSET 1`：找出第 N 高資料（常見面試技巧）

---

📂 所有題目都有附上完整程式註解與範例測試。
未來會持續更新更多題目與技術筆記，歡迎參考。
