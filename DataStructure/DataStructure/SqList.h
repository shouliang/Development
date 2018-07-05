//
// Created by 朱守亮 on 2017/7/14.
//
#include <stdio.h>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件
#include "statusDef.h"

#define LIST_INIT_SIZE 100  // 线性表存储空间的初始分配量
#define LISTINCREMENT  10   // 线性表存储空间的分配增量

typedef struct {
    ElemType *elem;  // 存储空间基址
    int length;      // 当前长度
    int listsize;    // 当前分配的存储容量(以sizeof(ElemType)为单位)
} SqList;

// 构造一个空的线性表L
Status InitList_Sq(SqList &L) {
    L.elem = (ElemType *) malloc(LIST_INIT_SIZE * sizeof(ElemType)); // 分配了LIST_INIT_SIZE大小的连续空间，为一个数组，L.elem指向其首地址，
    if (!L.elem) {
        exit(OVERFLOW);            // 存储分配失败
    }
    L.length = 0;                  // 空表的长度为0
    L.listsize = LIST_INIT_SIZE;   // 初始存储容量
    return OK;
}

// 在顺序线性表L中第i个位置之前插入新的元素e
Status ListInsert_Sq(SqList &L, int i, ElemType e) {
    // i的合法值为 1≤ i ≤ L.length +1
    if (i < 1 || i > L.length + 1) { // i值不合法
        return ERROR;
    }
    if (L.length >= L.listsize) {    // 当前存储空间已满，增加分配
        ElemType *newbase = (ElemType *) realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
        if (!newbase) exit(OVERFLOW);             // 存储分配失败
        L.elem = newbase;                         // 新基址
        L.listsize = L.listsize + LISTINCREMENT;  // 增加存储容量
    }

    ElemType *q = &(L.elem[i - 1]);               // q为插入位置
    for (ElemType *p = &(L.elem[L.length - 1]); p >= q; p--) {
        *(p + 1) = *p;                            // 表尾到插入位置的元素依次右移
    }
    *q = e;     // 插入e
    L.length++; // 表长增1
    return OK;
}

// 在顺序表L中删除第i个元素，并用e返回其值
Status ListDelete_Sq(SqList &L, int i, ElemType &e) {
    // i的合法值为 1≤ i ≤ L.length
    if (i < 1 || i > L.length) return ERROR; // i值不合法
    ElemType *p = &(L.elem[i - 1]);          // p为被删除元素的位置
    e = *p;                                  // 被删除的元素的值赋值给e
    // 指针（地址）与常数相加减，不是简单地算术运算，而是以当前指针指向的对象的存储长度为单位来计算的
    // &a[0]为数组首元素的地址，故&a[0]+1 越过一个数组元素长度的位置。 即：&a[0]+1*sizeof(a[0])
    ElemType *q = L.elem + (L.length - 1);   // 表尾元素的位置
    //ElemType *q = &(L.elem[L.length - 1]); // 表尾元素的位置,与L.elem + (L.length - 1)的写法效果等同，但便于理解
    for (p++; p <= q; p++) {
        *(p - 1) = *p;                       // 被删除元素之后的元素依次左移,注意“之后”，所以p++
    }
    L.length--;                              // 表长减1
    return OK;
}

// 在顺序表L中查询第1个值与e满足相等的位序
int LocateElem_Sq(SqList L, ElemType e) {
    int i = 1;
    ElemType *p = L.elem;
    while (i <= L.length &&  *p!=e) {
        i++;
        p++;
    }
    if (i <= L.length) {
        return i;
    } else {
        return 0;
    }
}

// printf顺便表的全部元素
Status ListTraverse_Sq(SqList L) {
    for (int i = 0; i < L.length; i++) {
        printf("L.elem[%d]=%d\n", i, L.elem[i]);
    }
}

// 顺序表合并为新的顺序表  时间复杂度(La.length + Lb.length)
void MergeList_Sq(SqList La, SqList Lb, SqList &Lc) {
    ElemType *pa = La.elem;
    ElemType *pb = Lb.elem;
    Lc.listsize = Lc.length = La.length + Lb.length;
    ElemType *pc = Lc.elem = (ElemType *) malloc(Lc.listsize * sizeof(ElemType));
    if (!Lc.elem) exit(OVERFLOW);

    ElemType *pa_last = La.elem + (La.length - 1);
    ElemType *pb_last = Lb.elem + (Lb.length - 1);
    while (pa <= pa_last && pb <= pb_last) {
        if (*pa <= *pb) {
            //*pc++ = *pa++;  // 对于 *cp++ ; 我们可以把它分解为： *cp 之后再 cp++
            // 对于 *++cp ; 我们可以把它分解为：++cp 之后再*cp
            *pc = *pa;
            pa++;
            pc++;

        } else {
            *pc++ = *pb++;
        }
    }
    while (pa <= pa_last) {
        *pc++ = *pa++;
    }
    while (pb <= pb_last) {
        *pc++ = *pb++;
    }
}

