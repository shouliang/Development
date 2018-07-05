//
// Created by 朱守亮 on 2017/8/7.
//

#define MAXSTRLEN 255
typedef unsigned char SString[MAXSTRLEN + 1]; // 0单元存放串的长度

// 返回子串T在主串S中第pos个字符之后的位置，若不存在，则return 0
int Index(SString S, SString T, int pos) {
    int i = pos;  // i为主串当前正待比较的字符位置
    int j = 1;    // j为模式串当前正待比较的字符位置
//    while (i < S[0] && j < T[0]) {
    while (i < 13 && j < 4) {
        if (S[i] == T[j]) {
            ++i;           // 继续比较后续字符
            ++j;
        } else {
            i = i - j + 2; // 指针后退重新开始匹配
            j = 1;
        }
        if (j > T[0]) {
            return i - T[0];
        } else return 0;
    }
}

void get_next(SString T, int next[]) {
    // 求模式串T在next函数值并存入数组next
    int i = 1;
    next[1] = 0;
    int j = 0;
    while (i < T[0]) {
        if (j == 0 || T[i] == T[j]) {
            ++i;
            ++j;
            next[i] = j;
        } else {
            j = next[j];
        }
    }
}

// KMP算法
int Index_KMP(SString S, SString T, int pos) {
    int i = pos;  // i为主串当前正待比较的字符位置
    int j = 1;    // j为模式串当前正待比较的字符位置

    int next[255];
    get_next(T, next);

    while (i < S[0] && j < T[0]) {
        if (S[i] == T[j]) {
            ++i;           // 继续比较后续字符
            ++j;
        } else {
            j = next[j];    // 模式串向右移动
        }
        if (j > T[0]) {
            return i - T[0];
        } else return 0;
    }
}

// next数组方法的改进
void get_nextval(SString T, int nextval[]) {
    int i = 1;
    nextval[1] = 0;
    int j = 0;
    while (i < T[0]) {
        if (j == 0 || T[i] == T[j]) {
            ++i;
            ++j;

            if (T[i] != T[j]) nextval[i] = j;
            else nextval[i] = nextval[j];  // 当前字符与前缀字符相同，则将前缀字符的nextval的值赋值给nextval在i位置的值

        } else {
            j = nextval[j];
        }
    }
}