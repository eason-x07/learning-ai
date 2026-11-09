# Week 1 Notes

## 2026-11-08: GitHub basics
- Repository 简称repo 仓库 一个项目做在一个仓库
- README 是仓库的介绍 大家通过README知道你的仓库用来干嘛
- Commit 是提交 每一次对仓库的更改都需要提交
- Markdown 是在README使用的一种格式语言 (week01.md) #是大标题 ##是小标题 - 开头是列表 - [ ]空复选框 - [x]是打勾的复选框
- 2FA (Two-Factor authentication) 二步验证 账号安全第一层是密码 第二层是恢复码(Recovery codes) 30秒刷新一次
- 
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
- 关于.items的解释：不同类型的数据有不同的方法：列表有 .append()，字典有 .items()
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

### 今天犯的错（很重要！）
- append之后列表的len增加了
- 区分python和c的写法，Python 用冒号 + 缩进； C 用大括号 { }
- avg应该用在循环外，避免跑多次无效结果
- for 不需要缩进，for的内容才要缩进
