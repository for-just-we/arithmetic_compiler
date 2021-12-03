# arithmetic_compiler
解析算术运算表达式的编译器，此编译器功能在于解析输入表达式并输出运算结果，有错误就报错，通过python实现，希望以此为示例写出一个简单的基于python的编译器。
参考了这位大佬的博客[手把手教你构建 C 语言编译器](https://lotabout.me/2015/write-a-C-interpreter-0/)
支持中间插入空格，比如`1 + ( 3 - 2) `这种，空格不影响效果，但是目前不要在开头插入空格，比如`  1 + ( 3 - 2) `。不支持中间插入换行符


# match函数和next_token函数及示例
以`1 + ( 3 - 2) * ( 2 - 1 )`为例（每2个token中间间隔1个空格）

首先定义`match`函数和`next_token`函数

```
def next_token(src: bytes, program_state: dict):
    # skip white space
    ...


def match(tk: int, src: bytes, program_state: dict):
    # 清除头部空格
    ...
    next_token(src, program_state)
```

编译器一次线性扫描输入表达式序列实现解析，根据下图可以看到，每扫描到一个token（运算符，括号，数字）会执行一次`match`，每执行一次`match`会调用`next_token`，`match`和`next_token`都会有清除空格的操作，这样免除了在写文法时清除空格的问题。`next_token`函数意在收集单个数字token。

![示例表达式token序列及match函数执行顺序](/__pycache__/execute.png)


# 文法

运算表达式的文法：
```
<expr> ::= <expr> + <term>
         | <expr> - <term>
         | <term>

<term> ::= <term> * <factor>
         | <term> / <factor>
         | <factor>

<factor> ::= ( <expr> )
           | Num
```

消除左递归后的文法：
```
<expr> ::= <term> <expr_tail>
<expr_tail> ::= + <term> <expr_tail>
              | - <term> <expr_tail>
              | <empty>

<term> ::= <factor> <term_tail>
<term_tail> ::= * <factor> <term_tail>
              | / <factor> <term_tail>
              | <empty>

<factor> ::= ( <expr> )
           | Num
```

`expr`,`term`,`expr_tail`,`factor`,`term_tail`在代码里都是function，示例表达式执行顺序如下：

![示例表达式token序列及match函数执行顺序](/__pycache__/expression.png)

红框框出的是括号里的子表达式。
