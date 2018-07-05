//
// Created by 朱守亮 on 2017/7/20.
//
#include <stdio.h>
#include <sys/malloc.h>
#include <cstdlib> // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

// 双向链表
typedef struct DuLNode {
    ElemType data;
    struct DuLNode *prior;
    struct DuLNode *next;
} DuLNode, *DuLinkList;

Status InitList_DuL(DuLinkList &L) {
    L = (DuLNode *) malloc(sizeof(DuLNode)); // 生成头结点，L->data无数据
    if (!L) return ERROR;
    L->prior = L;
    L->next = L;
    return OK;
}

DuLNode *GetElemP_DuL(DuLinkList &L, int i) {
    DuLNode *p = L->next;
    int j = 1;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (!p || j > i) return NULL;
    return p;
}

Status ListInsert_DuL(DuLinkList &L, int i, ElemType e) {
    DuLNode *p = GetElemP_DuL(L, i);
    if (!p) return ERROR;
    DuLNode *s = (DuLNode *) malloc(sizeof(DuLNode));
    if (!s) return ERROR;
    s->data = e;

    s->prior = p->prior;
    p->prior->next = s;
    s->next = p;
    p->prior = s;  // 四个指针需要修改

    return OK;
}

Status ListDelete_DuL(DuLinkList &L, int i, ElemType &e) {
    DuLNode *p = GetElemP_DuL(L, i);
    if (!p) return ERROR;
    e = p->data;

    p->prior->next = p->next;
    p->next->prior = p->prior;  // 两个指针需要修改，此两句可以互换
    free(p);
    return OK;
}

