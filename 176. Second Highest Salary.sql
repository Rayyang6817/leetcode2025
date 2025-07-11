-- LeetCode 176. Second Highest Salary
-- 題目：找出第二高的薪水，如果沒有第二高就回傳 null

-- 💡 解題筆記：
-- 第一直覺是用 DISTINCT 去掉重複薪水後，再做 ORDER BY DESC（由高到低）
-- 但困難點在於：要怎麼抓出「第二筆」？
-- 這在實務上比較少見，因為我們很少抓「第 N 筆值」
-- 通常是抓 Top 1，或是排名條件篩選

-- 🎯 解法說明：
-- 使用 LIMIT 1 OFFSET 1 的技巧：跳過第一高（OFFSET 1），再抓一筆（LIMIT 1）
-- 用子查詢包起來，這樣就算沒有第二高，也會回傳 null（符合題目要求）

-- ❌ 如果你不包在子查詢裡，當沒資料時，SQL 是不會回傳 row（空結果），這會造成 SQLCODE100 或空表
-- ✅ 子查詢可以讓結果成為一個單一欄位，值為 null

SELECT
    (
        SELECT DISTINCT salary 
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;
