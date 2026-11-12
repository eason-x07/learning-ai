# Week 1 Notes

## 2026-11-08: GitHub basics
- Repository 简称repo 仓库 一个项目做在一个仓库
- README 是仓库的介绍 大家通过README知道你的仓库用来干嘛
- Commit 是提交 每一次对仓库的更改都需要提交
- Markdown 是在README使用的一种格式语言 (week01.md) #是大标题 ##是小标题 - 开头是列表 - [ ]空复选框 - [x]是打勾的复选框
- 2FA（两步验证）：第一层是密码，第二层是手机验证器 App 里的 6 位数字（30 秒刷新一次）
- 恢复码（Recovery codes）是手机丢失时的备用登录方式

## 2026-11-09: Python basics

### 字典 dict
- 字典和列表的区别：列表用位置编号找东西，比如nums[0]表示第0个；字典用（key，键）找对应的（value，值）
- 以后调用AI的API，发送收回的数据都是用字典格式（JSON）
```python
student = {
    "name": "Eason",
    "year": 1,
    "major": "CS"
}
print(student["name"])   # 输出 Eason
print(student["year"])   # 输出 1
```
- "在外面往字典里加东西"的写法:
```python
student["food"] = "nasi lemak"
```
### 函数 function
```python
def greet(name):
    print(f"Hello, {name}!")
greet("Eason")
```
- f-string 是用{ }让变量的值放进文字里
- 一个函数只做一件事，这样函数可以重复用，换一份名单也不用改函数

### for 循环
- 原则：缩进决定代码属于哪里
- 遍历列表的写法：
```python
names=["a", "b", "c"]
for name in names:
    print(name)
```
- 遍历字典的写法：
```python
student = {
    "name": "Eason",
    "year": 1,
    "major": "CS"
}
for key, value in student.items():
    print(f"{key}: {value}")
```

### 关于.items的解释
- 不同类型的数据有不同的方法：列表有 .append()，字典有 .items()
```python
student = {"name": "Eason", "year": 1, "major": "CS"}

# 写法 1：直接遍历字典
for x in student:
    print(x)
# 输出：name, year, major  ← 只有键

# 写法 2：用 .values()
for x in student.values():
    print(x)
# 输出：Eason, 1, CS  ← 只有值

# 写法 3：用 .items()
for x in student.items():
    print(x)
# 输出：('name', 'Eason'), ('year', 1), ...  ← 键和值成对出现
```
- scores 是字典本身，print(scores)打印出来是 {'Eason': 85, 'Alice': 92}
- scores.items() 是把字典拆成一对一对之后的东西，Python 叫它 dict_items。打印出来就是：dict_items([('Eason', 85), ('Alice', 92)])
- .items() 是给 for 循环用的，用来把键和值一对一对拿出来。单独打印它，就会看到这个"拆开后的原始样子"。

### 今天犯的错（很重要！）
- append之后列表的len增加了
- 区分python和c的写法，Python 用冒号 + 缩进； C 用大括号 { }, Python 60 <= score < 80 可以连着写，C 语言不行
- avg应该用在循环外，避免跑多次无效结果
- for 那一行和外面的代码对齐，循环里面的内容才要缩进
- 冷芝士：Python 习惯在运算符两边加空格：score >= 80、score < 60。这是 Python 官方的代码风格（叫 PEP 8）

## 2026-11-10: Grade_manager.py

### return的用法
- print 只显示，return 把结果交回给调用的地方，可以存进变量继续用
```python
def get_grade(score):
    if score >= 80:
        return 'A'
    elif 60 <= score < 80:
        return 'B'
    else:
        return 'C'
```

### if/elif/else
- Python 用 elif，C 用 else if
- 从上往下检查，碰到第一个成立的就停，后面的都跳过
- and / or / not 对应 C 的 && / || / !

### while 循环
- for 适合"知道要循环几次"的情况，比如遍历一个列表。不知道的情况用while。
```python
while True:
    name = input("学生名字（直接回车结束）：")
    if name == "":
        break
    print(f"你输入了 {name}")
```
- while True: 表示“一直重复，永不停止”
- break 表示“马上跳出循环”

### input（）
- input（）拿到的是文字
```python
score = int(input("分数："))   # int() 把文字转成整数  # 假设用户输入 85
print(score + 1)               # ✅ 输出 86
```

### 注意要点
- 平均分保留一位小数：f"{average:.1f}"，:.1f 的意思是"小数点后 1 位"
- 写完代码后，要专门去测试"奇怪"的情况：空的输入、零、负数
- 在 Git 里，"移动文件"本质上就是"改文件路径"，这在 Git 里叫 rename（重命名）
- 点文件名字最前面，Backspace，前面的文件夹名字就会被删掉，输入新名字会自动生成新文件夹

### 关于报错信息
- ZeroDivisionError 是除以零
- NameError 是用了不存在的变量
- ValueError 是输入了不被接受的值，比如在int输入“abc”。解法：try/except

### 文件读写
```python
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Eason!\n")
    f.write("第二行\n")
```
- with ... as f: 把打开的文件叫作 f。缩进里的代码执行完后，Python 会自动关闭文件。
- "w"：覆盖，打开文件那一刻清空，文件不存在时新建
- "a"：追加，文件不存在时新建
- "r"：读取，文件不存在时报错FileNotFoundError
- utf-8: 支持中文

### 冷芝士
- Ctrl + / 用来注释，每行前面自动加 # ,再按一次关掉
- pass 什么都不做
- 同一个文件夹不会有同名文件

## 2026-11-12 grade_manager_2.0.py

### JSON
- JavaScript Object Notation，意思是"JavaScript 对象表示法"
- JSON不是一种编程语言，它是一种数据格式，像是一个标准快递箱。
- 它的作用就是：把列表、字典变成文字存起来，读回来时再还原成列表、字典
- 快递箱的规格是全世界统一的，不同的语言、不同的程序，都能用它交换数据。
- 冷芝士：在 JSON 里，字典叫 object（对象），列表叫 array（数组）。
```python
import json    # 先导入 json 工具包，Python 自带，不用安装

scores = {"Eason": 85, "Alice": 92, "小明": 70}

# 存：字典 → 文件
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False, indent=2)

# 读：文件 → 字典
with open("scores.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["Eason"])    # 输出 85，真的变回字典了！
```

### json小工具
- json.load(文件)：从文件读出数据
- json.dump(数据，文件)：把数据存进文件
```python
json.dump(scores, f, ensure_ascii=False, indent=2)
#         ↑必填   ↑必填  ↑选填                ↑选填
```
- 必填的：要存的数据，加上要存进去的文件。数据不一定是列表，字典、列表、数字、文字都可以
- 选填的：写成 名字=值 的样子，叫关键字参数（keyword argument）。不写的话，Python 会用默认值
- ensure_ascii 默认是 True，也就是把非英文字符转成 \u 编码
- indent 默认是 None，也就是不缩进，全部挤在一行

### 关于报错信息
- Python 从上往下执行，一旦出错就立刻停下，后面的代码全部不会执行。
- FileNotFoundError "r" 模式在文件不存在时会报错。，解法：try/except
- 两个程序用同一个文件名会互相干扰 → 每个程序用专属的文件名
- 空文件 ≠ 空字典：空字典在 JSON 里是 {}，空文件会报 JSONDecodeError
- 文件损坏时，坏数据不是在读取时消失，而是在用 "w" 存档时被覆盖的
- json.JSONDecodeError不仅仅会在json文件什么都没有时出现。json文件损坏（比如说有人直接手动把文件数据或格式改掉）也会出现DecodeError，这个时候如果我的处理方式是像现在这样，使用时很容易会直接清空被损坏的文件
- 过程是这样：
1.读取损坏的文件 → JSONDecodeError → scores = {}。这时文件本身还没被动过，坏数据还在
2.用户输入新学生
3.用 "w" 存档 → 文件被清空，只写入新输入的学生 → 旧数据这时才真正消失

- 真实的程序会在发现文件损坏时，先备份一份再继续。

### try/except
```python
try:
    with open("scores.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = {}    # 文件不存在，就从空字典开始
```
- 试着做 try 里面的事；如果出现 FileNotFoundError，不要崩溃，改做 except 里面的事。
```python
try:
    with open("grade_data.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    scores = {}
```
- 把几种错误放进括号里，用逗号隔开，让 except 同时接住多种错误

### 心得
- 先自己运行测试，先自己找问题、自己修。
- 有地方出错：先试着读报错、自己改一次。改不好再把报错一起发给我，我们一起看
- 用户会做出各种你想不到的操作，比如手动清空文件。好的程序要能扛住这些情况。
- 以后写完程序，都可以试着这样故意"搞破坏"一下。
- 真实的程序会在发现文件损坏时，先备份一份再继续。

### continue, break, pass
- continue: 跳过这一轮剩下的代码，直接回到循环开头
- break: 跳出整个循环
- pass: 躺平（什么都不做）
```python
def save_report():
    pass    # 这个函数以后再写，先占个位置

if score > 100:
    pass    # 暂时不处理
```
- 三个放一起比较：
```python
for n in [1, 2, 3, 4]:
    if n == 2:
        ???
    print(n)
```

| 指令 | 作用 | 遇到 2 时的输出 |
|---|---|---|
| `pass` | 什么都不做，继续往下执行 | 1 2 3 4 |
| `continue` | 跳过这一轮剩下的代码，回到循环开头 | 1 3 4 |
| `break` | 直接结束整个循环 | 1 |

### Markdown
- Markdown 的表格是用 |（竖线）和 -（减号）画出来的。
- 基本格式：
```markdown
| 标题1 | 标题2 | 标题3 |
|---|---|---|
| 内容 | 内容 | 内容 |
| 内容 | 内容 | 内容 |
```
- 第一行是标题行，每一格用 | 隔开
- 第二行是分隔线，每一格写 ---，告诉 Markdown "上面那行是标题"
- 后面每一行是一行数据，格子数量要和标题行一样
- 表格的上面和下面最好各空一行，否则可能会和前后的文字粘在一起，显示不出表格
