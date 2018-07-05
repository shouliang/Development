//
// Created by 朱守亮 on 2017/7/14.
//
#include <stdio.h>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

// 单链表
typedef struct LNode {
    ElemType data;
    struct LNode *next;
} LNode, *LinkList;

Status GetElem_L(LinkList L, int i, ElemType &e) {
    // L为带头结点的单链表的头指针，一般用头指针名指代单链表的名称
    LNode *p = L->next;  // 初始化，p指向第一个结点，故j从1开始计数
    int j = 1;           // 初始化，j为计数器
    while (p && j < i) { // 顺指针向后查找，直到p指向第i个元素或者p为空
        p = p->next;
        ++j;
    }
    if (!p || j > i) return ERROR;
    e = p->data;
    return OK;
}

// 链表在第i(i从1开始而不是0)个位置插入或者删除都要找到第i-1个元素
// 故LNode *p = L,是从头结点开始的，故j=0
// 因为在头结点后可以插入数据
// 但是在删除数据时，需要通过判断p->next是否有结点可以删除
Status ListInsert_L(LinkList &L, int i, ElemType e) {
    LNode *p = L; // 从头结点开始,故j从0开始
    int j = 0;
    while (p && j < i - 1) {
        p = p->next;
        ++j;
    }

    if (!p || j > i) {
        return ERROR;
    }
    LNode *s = (LNode *) malloc(sizeof(LNode));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return OK;
}

Status ListDelete_L(LinkList &L, int i, ElemType &e) {
    LNode *p = L;
    int j = 0;
    while (p->next && j < i - 1) {
        p = p->next;
        ++j;
    }
    if (!(p->next) || j > i - 1) { return ERROR; }
    LNode *q = p->next;  // 临时保存删除的结点
    p->next = q->next;
    e = q->data;
    free(q);
    return OK;
}

// 头插法
void CreateList_L(LinkList &L, int n) {
    L = (LinkList) malloc(sizeof(LNode));  // 生成一个头结点,其中数据域data为空
    L->next = NULL;
    for (int i = n; i > 0; --i) {
        LNode *p = (LNode *) malloc(sizeof(LNode));
        scanf("%d", &p->data);
        p->next = L->next;
        L->next = p;
    }
}

// 尾插法
void CreatListTail_L(LinkList &L, int n) {
    srand(time(0)); // 初始化随机种子
    L = (LinkList) malloc(sizeof(LNode));
    L->next = NULL;
    LinkList r = L; // 表尾指针初始化指向L
    for (int i = 0; i < n; i++) {
        LNode *p = (LNode *) malloc(sizeof(LNode));
//        scanf("%d", &p->data);
        p->data = rand() % 100 + 1;
        r->next = p;
        r = p;               // 表尾指针指向当前新结点
    }
    r->next = NULL;
}

void ListTraverse_L(LinkList &L) {
    LNode *p = L->next;
    while (p) {
        printf("%d\n", p->data);
        p = p->next;
    }
}


void MergeList_L(LinkList &La, LinkList &Lb, LinkList &Lc) {
    LNode *pa = La->next; // 从第一个结点开始
    LNode *pb = Lb->next;
    LNode *pc = La;
    Lc = pc;
    while (pa && pb) {
        if (pa->data < pb->data) {
            pc->next = pa;
            pc = pa;          // pc重新指向表尾
            pa = pa->next;
        } else {
            pc->next = pb;
            pc = pb;
            pb = pb->next;
        }
    }
    pc->next = pa ? pa : pb;
    free(Lb);
}
