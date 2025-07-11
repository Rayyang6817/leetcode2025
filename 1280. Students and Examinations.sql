-- LeetCode 1280. Students and Examinations
-- 題目：找出每位學生在每門科目的考試次數（就算沒考也要出現，次數為 0）

-- 🧠 解題思路：
-- 1️⃣ 題目要求每位學生 × 每門科目的完整組合 → 使用 CROSS JOIN 產生 Cartesian product（笛卡兒積）
-- 2️⃣ 使用 LEFT JOIN 把 Examinations 資料接上去，對齊學生與科目
--     為什麼要加 ON e.subject_name = su.subject_name？
--     因為只用 student_id 會造成所有考試紀錄都被對到，導致統計錯誤
--     正確邏輯是：某位學生「在這一門課」考試幾次 → 必須雙條件 JOIN
-- 3️⃣ 使用 COUNT(e.subject_name) 統計考試次數
--     為什麼不是 COUNT(*)？
--     因為 LEFT JOIN 可能會導致 NULL，COUNT(*) 會把 NULL 算進去，COUNT(column) 才能正確忽略 NULL
-- 4️⃣ 為什麼要 GROUP BY？
--     因為 SELECT 中有聚合函數 COUNT()，SQL 語法規定所有非聚合欄位都要寫在 GROUP BY 裡
--     如果沒有 COUNT()，其實不需要寫 GROUP BY，只是列出資料
-- 5️⃣ 最後依照 student_id 與 subject_name 排序

-- ✅ 最終解法如下：

SELECT 
    s.student_id, 
    s.student_name, 
    su.subject_name, 
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e 
   ON e.student_id = s.student_id AND e.subject_name = su.subject_name 
GROUP BY 
    s.student_id, 
    s.student_name, 
    su.subject_name
ORDER BY 
    s.student_id, 
    su.subject_name;
