//
// Created by 朱守亮 on 2017/7/31.
//

#include <stdio.h>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

typedef int QElemType;

// ----- 循环队列——队列的顺序存储结构
#define  MAXSIZE 100
typedef struct {
    QElemType *base;
    int front;
    int rear;
} SqQueue;

// ----- 循环队列的基本操作 -----
Status InitQueue(SqQueue &Q) {
    Q.base = (QElemType *) malloc(sizeof(QElemType));
    if (!Q.base) exit(OVERFLOW);
    Q.front = Q.rear = 0;
    return OK;
}

int QueueLength(SqQueue Q) {
    return (Q.rear - Q.front + MAXSIZE) % MAXSIZE;
}

Status EnQueue(SqQueue &Q, QElemType e) {
    if ((Q.rear + 1) % MAXSIZE == Q.front) return ERROR; // 队列满 的判定：约定队尾元指针的一位为队头指针
    Q.base[Q.rear] = e; // 插入新的元素e到队尾
    Q.rear = (Q.rear + 1) % MAXSIZE;
    return OK;
}

Status DelQueue(SqQueue &Q, QElemType &e) {
    if (Q.front == Q.rear) return ERROR; // 队列空 的判定
    e = Q.base[Q.front]; // 删除Q的队头元素，用e返回其值
    Q.front = (Q.front + 1) % MAXSIZE;
    return OK;
}

// 循环队列，注意对MAXSIZE求余
// 队列空：Q.front == Q.rear
// 队列满：(Q.front + 1) % MAXSIZE == Q.front
// 进队列：Q.rear = (Q.rear + 1) % MAXSIZE ，队尾
// 出队列：Q.front = (Q.front + 1) % MAXSIZE ，队头