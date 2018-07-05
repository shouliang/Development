//
// Created by 朱守亮 on 2017/7/27.
//
#include <stdio.h>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

#define STACK_INIT_SIZE 100
#define STACKINCREMENT  10

typedef char SElemType;

typedef struct {
    SElemType *base;
    SElemType *top;
    int stacksize;
} SqStack;

Status InitStack(SqStack &S) {
    S.base = (SElemType *) malloc(sizeof(SElemType));
    if (!S.base) exit(OVERFLOW);
    S.top = S.base;
    S.stacksize = STACK_INIT_SIZE;
    return OK;
}

Status GetTop(SqStack S, SElemType &e) {
    if (S.top == S.base) return ERROR;  // S.top == S.base 栈空的标记
    e = *(S.top - 1);
    return OK;
}

Status Push(SqStack &S, SElemType &e) {
    if (S.top - S.base >= S.stacksize) {
        S.base = (SElemType *) realloc(S.base, (S.stacksize + STACKINCREMENT) * sizeof(SElemType));
        if (!S.base) exit(OVERFLOW);
        S.top = S.base + S.stacksize;
        S.stacksize = S.stacksize + STACKINCREMENT;
    }
//    *S.top++ = e;
    *S.top = e;
    S.top = S.top + 1;  // 非空栈中的栈顶指针始终指向栈顶元素的下一个元素的位置上
    return OK;
}

Status Pop(SqStack &S, SElemType &e) {
    if (S.top == S.base) return ERROR;
//    e = *--S.top;
    S.top = S.top - 1;
    e = *(S.top);
    return OK;
}

Status StackEmpty(SqStack S) {
    if (S.top == S.base) {
        return OK;
    }
    return ERROR;
}

// 为后缀表达式服务的GetTop方法
SElemType GetTop(SqStack S) {
    if (S.top == S.base) return ERROR;  // S.top == S.base 栈空的标记
    return *(S.top - 1);
}

/* 转换成八进制
void conversion() {
    SqStack S;
    InitStack(S);
    int N;
    scanf("%d", &N);
    while (N) {
        SElemType m = (SElemType) N % 8;  // 求余
        Push(S, m);
        N = N / 8;                        // 再整除
    }
    while (!StackEmpty(S)) {
        SElemType e;
        Pop(S, e);
        printf("%d", e);
    }
}
*/

// 括号匹配
Status ParenthesisMatch(SqStack &S, char *str) {
    int i = 0;
    SElemType e;
    while (str[i]) {
        switch (str[i]) {
            case '(':
                Push(S, str[i]);
                break;
            case '[':
                Push(S, str[i]);
                break;
            case '{':
                Push(S, str[i]);
                break;


                // 右括号的话，判断是否与栈顶的左括号匹配，匹配则出栈
            case ')':
                GetTop(S, e);
                if (e == '(') {
                    Pop(S, str[i]);
                }
                break;
            case ']':
                GetTop(S, e);
                if (e == '[') {
                    Pop(S, str[i]);
                }
                break;
            case '}':
                GetTop(S, e);
                if (e == '{') {
                    Pop(S, str[i]);
                }
                break;
        }

        i++;
    }

    if (StackEmpty(S)) {
        return OK;
    }
    return FALSE;
}


// 判断是否是运算符
Status In(char c) {
    char OP[] = {'+', '-', '*', '/', '(', ')', '#'};
    for (int i = 0; i < 7; i++) {
        if (c == OP[i]) {
            return 1;
            break;
        }
    }
    return 0;
}

// 比较运算符的优先级  (优先级最大，)优先级最小
char Precede(char c1, char c2) {
    switch (c1) {
        case '+':
        case '-':
            switch (c2) {
                case '+':
                case '-':
                case ')':
                case '#':
                    return '>';
                    break;
                case '*':
                case '/':
                case '(':
                    return '<';
                    break;
                default:
                    break;
            }
            break;
        case '*':
        case '/':
            switch (c2) {
                case '+':
                case '-':
                case '*':
                case '/':
                case ')':
                case '#':
                    return '>';
                    break;
                case '(':
                    return '<';
                    break;
                default:
                    break;
            }
            break;
        case '(':
            switch (c2) {
                case '+':
                case '-':
                case '*':
                case '/':
                case '(':
                    return '<';
                    break;
                case ')':
                    return '=';
                    break;
                default:
                    break;
            }
            break;
        case ')':
            switch (c2) {
                case '+':
                case '-':
                case '*':
                case '/':
                case ')':
                case '#':
                    return '>';
                    break;
                default:
                    break;
            }
            break;
        case '#':
            switch (c2) {
                case '+':
                case '-':
                case '*':
                case '/':
                case '(':
                    return '<';
                    break;
                case '#':
                    return '=';
                    break;
                default:
                    break;
            }
            break;
        default:
            break;
    }
}

int Operate(int a, char theta, int b) {
    switch (theta) {
        case '+':
            return a + b;
            break;
        case '-':
            return a - b;
            break;
        case '*':
            return a * b;
            break;
        case '/':
            return a / b;
            break;
    }
}

// 单个字符转换成数字，仅支持1-9
int charToInt(char c) {
    switch (c) {
        case '1':
            return 1;
            break;
        case '2':
            return 2;
            break;
        case '3':
            return 3;
            break;
        case '4':
            return 4;
            break;
        case '5':
            return 5;
            break;
        case '6':
            return 6;
            break;
        case '7':
            return 7;
            break;
        case '8':
            return 8;
            break;
        case '9':
            return 9;
            break;
        default:
            return 0;
            break;
    }
}

void MiddelToBack() {
    SqStack S;  // 存放运算符的栈
    InitStack(S);

    char middle[] = "9+(3-1)*3+8/2#";  // 中缀表达式
    char back[100];                    // 后缀表达式
    int i = 0;                         // 循环遍历中缀表达式的变量
    int j = 0;                         // 生成后缀表达式的变量
    char c = middle[i];
    while (c != '#') {

        if (!In(c)) {
            back[j] = c;  // 非运算符即数字直接输出到后缀表达式
            j++;

        } else {
            if (StackEmpty(S) || c == '(' || Precede(GetTop(S), c) == '<') {  // 栈为空或者遇到左括号(,直接进栈
                Push(S, c);
            } else if (c == ')') {
                while (!StackEmpty(S) && GetTop(S) != '(') {  // 遇到右括号),弹出直到左括号的运算符，但不包括左括号(
                    SElemType e;
                    Pop(S, e);
                    back[j++] = e;
                }

                // 直接弹出左括号(
                SElemType eb;
                Pop(S, eb);
            } else if (Precede(GetTop(S), c) == '>') {  // 栈顶元素权重高，运算符进栈
                while (!StackEmpty(S) && Precede(GetTop(S), c) == '>') { // 栈顶元素权重高，弹出栈顶元素直到栈顶元素权重低或者栈为空
                    SElemType e;
                    Pop(S, e);
                    back[j++] = e;
                }

                // 权重低的运算符进栈
                Push(S, c);
            }
        }

        c = middle[++i];
    }

    // 弹出剩余的运算符
    while (!StackEmpty(S)) {
        SElemType e;
        Pop(S, e);
        back[j++] = e;
    }

    back[j++] = '\n';

    i = 0;
    while (back[i] != '\n') {
        printf("%c", back[i]);
        i++;
    }

    return;
}






