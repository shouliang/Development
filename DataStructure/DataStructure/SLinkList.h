//
// Created by 朱守亮 on 2017/7/21.
//
#include "statusDef.h"
// ----- 线性表的静态单链表存储结构 -----
#define MAXSIZE 100 // 链表的最大长度

typedef struct {
    ElemType data;
    int cur;
} component, SLinkList[MAXSIZE];

int LocateElem_SL(SLinkList S, ElemType e) {
    int i = S[0].cur;
    while (i && S[i].data != e) {
        i = S[i].cur;
    }
    return i;
}

// 我们对数组的第一个和最后一个元素作为特殊元素处理
// space[0].cur存放备用链表的第一个结点的下标,相当于头指针
// 最后一个元素的cur存放第一个data数据域不为空的元素的下标，整个链表为空时，则为0
void InitSpace_SL(SLinkList &space) {
    for (int i = 0; i < MAXSIZE - 1; i++) {
        space[i].cur = i + 1;
    }
    space[MAXSIZE - 1].cur = 0; // 目前静态链表为空，最后一个元素的cur为0
}

int Malloc_SL(SLinkList &space) {
    int i = space[0].cur;
    if (space[0].cur) {
        space[0].cur = space[i].cur; // 第i个分量被使用，所以让space[0].cur指向i的下个分量作为备用
    }
    return i;
}

void Free_SL(SLinkList &space, int k) {
    space[k].cur = space[0].cur; // 删除元素的cur指向space[0].cur的位置，相当于next指向本来备用链表的首元素
    space[0].cur = k;            // 删除位置获取优先级，回收到备用链表，作为首元素
}

Status ListInsert_SL(SLinkList &space, int i, ElemType e) {
    int j, k, l;
    k = MAXSIZE - 1;  // 最后一个元素的下标 存放第一个data数据域不为空的元素的下标，故从最后一个元素开始变量查找第i-1个元素
    if (i < 1) {
        return ERROR; // 暂时不考虑 i > ListLength(L) + 1 的情况 todo
    }

    j = Malloc_SL(space);   // 获得空闲分量的下标
    if (j) {
        space[j].data = e;
        for (l = 1; i <= l - 1; i++) {  // 找到第i个元素之前的位置:即 i - 1
            k = space[k].cur;
        }

        space[j].cur = space[k].cur;
        space[k].cur = j;            // 此两句类似于单链表的插入，且不可弄反

        return OK;
    }
    return ERROR;
}

Status ListDelete_SL(SLinkList &space, int i) {
    int j, k;
    if (i < 1) {
        return ERROR; // 暂时不判断 i > ListLength(L)的情况
    }
    k = MAXSIZE - 1;
    for (j = 1; j <= i - 1; j++) {  // 找到删除位置之前的位置 i -1
        k = space[k].cur;           // 相当于p=p->next
    }

    j = space[k].cur;
    space[k].cur = space[j].cur;  // 此两句类似于单链表的删除，先保留后续，在指向后续的后续，cur就相当于单链表的next
    Free_SL(space, j);
    return OK;
}
