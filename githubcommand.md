✅ Git 提交推送流程

加到暫存區 (stage)

git add .


git . 是錯的，要 git add . 才能把全部修改加進暫存區。

建立 commit

git commit -m "你的訊息"


推送到遠端
#如果你在 main 分支，就寫 git push origin main。
#如果之前已經設定好 tracking branch，單純 git push 也可以。

git push origin 分支名稱


開推
git push
