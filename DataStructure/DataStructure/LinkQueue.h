//
// Created by 朱守亮 on 2017/7/31.
//
#include <stdio.h>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

// ----- 单链队列——队列的链式存储结构 ------

typedef int QElemType;

typedef struct QNode {
    QElemType data;
    struct QNode *next;
} QNode, *QueuePtr;

// 单链队列
typedef struct {
    QueuePtr front;  // 队头指针
    QueuePtr rear;   // 队尾指针
} LinkQueue;

// ----- 基本操作的算法描述 -----
Status InitQueue(LinkQueue &Q) {
    Q.front = Q.rear = (QueuePtr) malloc(sizeof(QNode));
    if (!Q.front) exit(OVERFLOW);
    Q.front->next = NULL;
    return OK;
}

Status DestroyQueue(LinkQueue &Q) {
    while (Q.front) {
        Q.rear = Q.front->next; // 利用Q.rear充当临时变量，节省了重新声明
        free(Q.front);
        Q.front = Q.rear;
    }
}

Status EnQueue(LinkQueue &Q, QElemType e) {
    QueuePtr p = (QueuePtr) malloc(sizeof(QNode));
    if (!p) exit(OVERFLOW);
    p->data = e;
    p->next = NULL;

    Q.rear->next = p; // 插入元素e到新的队列的尾部
    Q.rear = p;
    return OK;
}

Status DelQueue(LinkQueue &Q, QElemType &e) {
    // 若队列不为空，则删除Q的队头元素，用e返回其值
    // 否则返回ERROR
    if (Q.front == Q.rear) return ERROR;
    QNode *p = Q.front->next;
    e = p->data;
    if (Q.rear == p) Q.rear = Q.front; // 如果队列中最后一个元素被删除后，队尾指针也丢失了，因此需要对队尾指针重新赋值（指向头结点）
    Q.front->next = p->next;
    free(p);
}
