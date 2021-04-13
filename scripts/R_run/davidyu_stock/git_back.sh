#创建本地分支
git branch davidyu_2020
#切换到本地分支
git checkout davidyu_2020
# 添加所有变化
git add -A
# 注释
git commit -m "aa"
# 合并到远程分支
git push origin davidyu:new_hjx

#### 合并解决冲突
git clone git@code
git branch -a
git checkou new_training
git checkout new_train1

git merge new_training
git add src/main/java/impl
git ccommit -a
git push

