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
