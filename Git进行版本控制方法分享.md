# Git进行版本控制方法分享
## 1 环境准备

### 1.1 安装Git

**Windows：**

1. 从官网下载Git for Windows：https://git-scm.com/install/windows
  ![屏幕截图 2026-07-13 113920](./Git进行版本控制方法分享/image-20260713113920-1784080009329-2.png)
   接下来以下载的Git-2.55.0.2-64-bit.exe版本为例。

2. 双击下载后的Git-2.55.0.2-64-bit.exe，开始安装。
![image-20260715101759062](./Git进行版本控制方法分享/image-20260715101759062.png)

  点击[Next]到下一步。

3. 选择安装目录，可点击[Browse...]更换目录，也可以直接点击方框更改。
  ![image-20260715103236070](./Git进行版本控制方法分享/image-20260715103236070-1784082761920-4.png)
   点击[Next]到下一步。

4. 选择安装组件，根据需要勾选。
  ![image-20260713142020968](./Git进行版本控制方法分享/image-20260713142020968.png)
   点击[Next]到下一步。

5. 选择开始菜单文件夹。

  方框内Git可改为其他名字，也可点击“Browse...”选择其他文件夹或者给”Don't create a Start Menu folder“打勾不要文件夹，点击 [next] 到下一步。
  ![image-20260713142727069](./Git进行版本控制方法分享/image-20260713142727069.png)

6. 选择Git默认编辑器
  ![image-20260713143044964](./Git进行版本控制方法分享/image-20260713143044964.png)
   也可以选择别的编辑器，需要先去对应的官网安装完成后才能进行下一步。安装后还要配置在**`我的电脑->属性->高级系统设置->高级->环境变量->系统变量->Path->编辑添加对应编辑器的安装地址`**,如 **`C:\Program Files\notepad++`**。

7. 决定初始化新项目（仓库）的主干名字
  ![image-20260713144105826](./Git进行版本控制方法分享/image-20260713144105826.png)
   第一种是让Git自己选择，名字是master；第二种是自行决定，默认是main。点击[next]到下一步。

8. 选择Git的使用方式（调整path环境变量）
  ![image-20260713145058449](./Git进行版本控制方法分享/image-20260713145058449.png)
   一般选择第二种。点击[next]到下一步。

9. 选择SSH执行文件
  选择Git自带的OpenSSH。
    ![image-20260713145449918](./Git进行版本控制方法分享/image-20260713145449918.png)
   点击[next]到下一步。

10. 选择HTTPS后端传输
  ![image-20260713145831754](./Git进行版本控制方法分享/image-20260713145831754.png)
  点击[next]到下一步。

11. 配置行尾符号转换
  ![image-20260713150219616](./Git进行版本控制方法分享/image-20260713150219616.png)
  选择第一项，点击[next]到下一步。

12. 配置终端模拟器
  ![image-20260713150443481](./Git进行版本控制方法分享/image-20260713150443481.png)
  选择第一项，点击[next]到下一步。

13.选择默认的git pull行为
  ![image-20260713150730127](./Git进行版本控制方法分享/image-20260713150730127.png)
  选择第一项，点击[next]到下一步。

14. 选择一个凭证帮助程序和配置额外的选项
  ![image-20260713151058441](./Git进行版本控制方法分享/image-20260713151058441.png)
  点击[next]到下一步。
  ![image-20260713151148432](./Git进行版本控制方法分享/image-20260713151148432.png)
  选择第一项，然后点击[install]。

15. 安装完成
  ![image-20260713151428807](./Git进行版本控制方法分享/image-20260713151428807.png)

---
### 1.2 验证安装
打开命令行窗口（cmd或Git Bash），输入：```git --version```
如果显示版本号，说明安装成功：
在Git Bash中：
![image-20260713152753674](./Git进行版本控制方法分享/image-20260713152753674.png)
在终端中：
![image-20260713152833848](./Git进行版本控制方法分享/image-20260713152833848.png)

---
### 1.3 配置用户信息
使用Git之前，设置用户名和邮箱地址，这些信息会附加到每一次提交中。
打开终端或Git Bash，执行以下命令，将引号中的内容替换为自己的信息。
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```
通过以下命令检查配置是否成功：
```bash
git config --list
```
![image-20260713154924395](./Git进行版本控制方法分享/image-20260713154924395.png)

---
### 1.4 本地仓库操作

- 创建一个新项目文件夹（或进入已有项目文件夹）
```bash
mkdir my-project # 创建一个名为my-project的文件夹
cd my-project # 进入该文件夹
```
  ![image-20260713160653763](./Git进行版本控制方法分享/image-20260713160653763.png)
- 初始化Git仓库
在项目文件夹中,执行以下命令将其初始化为一个Git仓库:
```bash
git init
```
这会在当前目录下创建一个隐藏的`.git`子目录，它包含了Git仓库的所有元数据和对象数据库。
![image-20260713161155916](./Git进行版本控制方法分享/image-20260713161155916.png)

---



## 2 核心命令

### 2.1 查看状态（status）

```bash
git status
```
![image-20260713162550419](./Git进行版本控制方法分享/image-20260713162550419.png)
目前仓库的状态是没有提交任何文件。

---
### 2.2 添加文件到缓存区（add）

```bash
# 添加单个文件
git add 文件名.py

# 添加所有文件
git add .

# 添加指定类型的文件
git add *.py
```
在目录下创建一个新文件，例如python.py。

![image-20260713164237455](./Git进行版本控制方法分享/image-20260713164237455.png)

---
### 2.3 提交到版本库（commit）

```bash
git commit -m "本次提交说明"
```
![image-20260713164811910](./Git进行版本控制方法分享/image-20260713164811910.png)

---
### 2.4 查看提交日志（log）

```bash
git log
```

![image-20260713165103556](./Git进行版本控制方法分享/image-20260713165103556.png)

---
### 2.5 回退（reset）

将文件的历史切换到指定的某一个提交版本。

```bash
git reset --hard [commitID]
```

`commitID`可以通过上面的`git log`命令查到。

`--hard`参数会彻底重置工作区、暂存区和仓库到指定的提交状态，未保存的本地修改将会丢失。

---
### 2.6 撤销

- 将已经`git add`到暂存区的文件撤销回工作区。

```bash
git restore --staged [文件名] # 撤销指定文件
```
- 撤销在工作区对文件的修改，使其恢复到和暂存区域或上一次提交时的状态。

```bash
git restore [文件名] # 放弃对指定文件的修改
```

---
### 2.7 删除文件（rm）

- 从跟踪列表和工作目录中同时删除一个文件。

```bash
git rm [文件名]
git commit -m "删除指定文件"
```

- 恢复被删除的文件
```bash
git checkout -- [文件名]
```

- 仅从暂存区删除，把文件保留在工作区。

```bash
git rm --cached [文件名]
```

---
### 2.8 添加文件至忽略列表（.gitignore）

`.gitignore`文件用于告诉Git哪些文件或目录不需要被跟踪。

基本规则:
- `#`开头表示注释。
- 可以直接写文件名，如 `*.log`，表示忽略所有 `.log `文件。
- `build/`表示忽略整个` build `目录下的所有内容。
- `doc/*.txt`表示忽略`doc/`目录下的所有`.txt`文件，但不包括子目录。
- `doc/**/*.pdf`表示忽略`doc/`目录下及其所有子目录下的`.pdf`文件。
- `!`开头表示例外规则。例如，即使前面忽略了`*.a`，`!lib.a`也会让`lib.a`被跟踪.

---



## 3 关联到远程仓库

### 3.1 在GitHub网页上创建仓库
1. 点击GitHub官网并登录：https://github.com/

2. 点击右上角+ → New repository

   ![image-20260713173350995](./Git进行版本控制方法分享/image-20260713173350995.png)

3. Repository name填写项目名称
   Description填写描述（可选）
   选择公开（Public）或私有（Private）
   不要勾选“Add a README file”、“Add .gitignore” 或 “Choose a license”
   点击Create repository

   ![image-20260714095621757](./Git进行版本控制方法分享/image-20260714095621757.png)
4. 创建后会出现以下页面，上面有仓库地址，类似：
  `https://github.com/你的用户名/my-python-project.git`

![image-20260714100540891](./Git进行版本控制方法分享/image-20260714100540891.png)
复制该地址。

---
### 3.2 连接本地仓库到远程仓库
- 在本地项目的文件夹的终端中，执行：
```bash
git remote add origin https://github.com/你的用户名/仓库名.git
```
- 验证关联是否成功：

```bash
git remote -v
```
![image-20260714101734819](./Git进行版本控制方法分享/image-20260714101734819.png)

---
### 3.3 推送代码到远程仓库（`git push`）
```bash
git push -u origin master
```
`origin`:远程仓库的别名
`master`:推送的本地分支名

![image-20260714102355457](./Git进行版本控制方法分享/image-20260714102355457.png)

推送成功后，刷新在 GitHub 上的仓库页面，就能看到文件和提交历史了

![image-20260714102514146](./Git进行版本控制方法分享/image-20260714102514146.png)

---
### 3.4 克隆远程仓库（`git clone`)
- 在 GitHub 上找到想克隆的仓库。
点击绿色的 “Code” 按钮，复制 HTTPS 或 SSH URL。
![image-20260714105853336](./Git进行版本控制方法分享/image-20260714105853336.png)
- 打开终端，cd到想要存放项目的目录下，然后执行：
```bash
git clone http://github.com/SOMEONE_ELSE/SOME_REPOSITORY.git
```
这会将整个项目 (包括所有历史记录) 下载到该目录下，并自动设置好名为 origin 的远程仓库指向。


---
### 3.5 从远程仓库拉取更新(`git pull`)

如果远程仓库有了新的提交 (比如在 GitHub 网站上直接做了修改)，需要将这些更新拉取到本地仓库。
在本地项目文件夹中，确保在正确的分支上，执行：

```bash 
git pull origin master
```

如果之前推送时用了`-u`选项，可以执行：

```bash
git pull
```

---



## 4 分支管理

### 4.1 分支

- 查看分支

```bash
git branch
```

![image-20260714144011744](./Git进行版本控制方法分享/image-20260714144011744.png)

`*`表示当前所在的分支

- 创建新分支

```bash
git branch <分支名>
```

![image-20260714144508202](./Git进行版本控制方法分享/image-20260714144508202.png)

- 切换分支

```bash
git checkout <分支名> 或 git switch <分支名>
```

![image-20260714144836858](./Git进行版本控制方法分享/image-20260714144836858.png)

- 创建并切换分支

```bash
git checkout -b <分支名> 或 git switch <分支名>
```


---

### 4.2 合并分支

- 首先，切换回目标分支：

```bash
git checkout master
```
然后，执行合并命令：

```bash
git merge <分支名>
```
- 分支被合并且不再需要时可以删除(本地）：

```bash
git branch -d <分支名>
```

- 删除远程分支：

```bash
git branch -a # 可以看到所有分支，包括远程分支
或
git remote show origin # 查看远程仓库信息

git push origin --delete <分支名>
```

- 取消合并：
```bash
git merge --abort
```

---



## 5 实战示例

### 5.1 创建一个Git仓库

```bash
# 1. 创建项目目录
mkdir my-project
cd my-project

# 2. 初始化Git
git init

# 3. 创建文件
echo "Hello Git" > README.md

# 4. 添加到暂存区
git add README.md

# 5. 提交
git commit -m "初始化项目"

# 6. 查看状态
git status

# 7. 查看历史
git log
```

---

### 5.2 分支操作

```bash
# 1. 创建功能分支
git checkout -b feature-test

# 2. 修改文件
echo "新功能" >> README.md

# 3. 提交
git add .
git commit -m "添加新功能"

# 4. 切换回主分支
git checkout master

# 5. 合并功能分支
git merge feature-test

# 6. 删除功能分支
git branch -d feature-test
```

![image-20260714162055327](./Git进行版本控制方法分享/image-20260714162055327.png)

---

### 5.3 团队协作模拟

```bash
# 模拟两个开发者

# 开发者A
git checkout -b feature-a
echo "功能A" >> file.txt
git add .
git commit -m "完成功能A"

# 开发者B
git checkout -b feature-b
echo "功能B" >> file.txt
git add .
git commit -m "完成功能B"

# 合并两个功能
git checkout master
git merge feature-a
git merge feature-b
```

![image-20260714162823106](./Git进行版本控制方法分享/image-20260714162823106.png)

---



## 6 踩坑记录

- 想把克隆到本地仓库的别的仓库的文件内容连接到远程仓库上时出现报错

![image-20260714111859796](./Git进行版本控制方法分享/image-20260714111859796.png)
因为Agent-Learning-Hub文件夹里面有一个`.git`隐藏文件夹，说明它本身就是一个Git仓库。Git不允许在一个仓库里直接嵌套另一个仓库。

![image-20260714112047925](./Git进行版本控制方法分享/image-20260714112047925.png)

解决办法：删除 Agent-Learning-Hub 里的`.git`文件
```bash
# 从Git索引中移除（但保留本地文件）
git rm --cached Agent-Learning-Hub
# 删除子仓库里的.git文件
rm -rf Agent-Learning-Hub/.git
# 重新添加文件夹里的文件
git add Agent-Learning-Hub/
# 提交
git commit -m "将 Agent-Learning-Hub 转为普通文件夹并提交文件"
# 推送到Github
git push
```

此时的github界面可以正常打开查看文件夹内容

![image-20260714112633614](./Git进行版本控制方法分享/image-20260714112633614.png)

---

- 网络限制

![image-20260714143224484](./Git进行版本控制方法分享/image-20260714143224484.png)

解决方法：

1. 多刷新几次

2. 使用代理地址
```bash
# 临时替换远程地址为代理
git remote set-url origin https://ghproxy.com/<自己的仓库地址>

# 拉取
git pull

# 拉取成功后，换回正常地址
git remote set-url origin https://github.com/yu7-7ki/git.git
```