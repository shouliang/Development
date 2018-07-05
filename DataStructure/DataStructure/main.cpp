#include <time.h>
#include <cstring>
#include "SqList.h"     // 顺序表
#include "LinkList.h"   // 单链表
#include "DuLinkList.h" // 双链表

#include "SqStack.h"    // 顺序栈
#include "SqStack_int"  // 顺序栈 数据类型是int类型

#include "LinkQueue.h"  // 单链队列
#include "SqQueue.h"    // 循环队列(顺序队列的一种)

#include "SString.h"   // 串

#include "SqBiTree.h"  // 二叉树

/* 顺序表
int main() {
    SqList L;
    // 初始化顺序表L
    InitList_Sq(L);

    // 1-10的位置插入随机的
    srand(time(0)); // 初始化随机种子
    for (int i = 1; i <= 10; i++) {
        ListInsert_Sq(L, i, rand() % 100 + 1);
    }

    printf("----------random generate 10 number insert L----------\n");
    ListTraverse_Sq(L);

    // 删除位置随机(1-9)的元素，并返回e
    ElemType e;
    int delI = rand() % 10;
    ListDelete_Sq(L, delI, e);
    printf("----------deleted position:%d is %d----------\n", delI, (e));

    printf("----------after deleted position:%d list is----------\n", delI);
    ListTraverse_Sq(L);

    printf("----------union ordered list----------\n");
    // 顺序表合并
    SqList La, Lb, Lc;

    // 初始化顺序表L
    InitList_Sq(La);
    InitList_Sq(Lb);
    InitList_Sq(Lc);

    // 1-10的位置插入元素
    for (int i = 1; i <= 10; i++) {
        ListInsert_Sq(La, i, i + 1);  // 构造有序表
        ListInsert_Sq(Lb, i, i + 3);  // 构造有序表
    }

    MergeList_Sq(La, Lb, Lc);
    ListTraverse_Sq(Lc);

    ElemType locateNum = 3;
    printf("%d position is %d",locateNum,LocateElem_Sq(Lc, locateNum));

    return 0;
}
 */

// 单链表：单向的
// 双链表：双向指针
// 循环链表：单循环链表、双循环链表

// 单链表：结点只包含一个指向直接后续存储位置的指针域，故称线性链表或单链表
// 双链表：结点中有两个指针域，其一指向直接后继，另一个指向直接前驱
// 循环链表：表中的最后一个结点的指针域指向头结点，整个链表形成一个环

/* 单链表
int main() {
    printf("---------- 单链表插入、删除test ----------");
    LinkList L;
    CreateList_L(L, 3);

    int insertPosition = 3;
    ElemType insertElem = 2;
    ListInsert_L(L, insertPosition, insertElem);

    int deletePosition = 2;
    ElemType deletedElem;
    ListDelete_L(L,deletePosition,deletedElem);

    printf("---------- 单链表test ----------");
    LinkList L_tail;
    CreatListTail_L(L_tail, 5);  // 尾插法生成新的链表

    ListTraverse_L(L_tail); // 遍历单链表
    return 0;
}
 */

// 双向链表
//int main() {
//    DuLinkList L;
//    InitList_DuL(L);
//
//    for (int i = 1; i <= 3; i++) {
//        ListInsert_DuL(L, i, i);
//    }
//
//    ElemType  deleteElem;
//    ListDelete_DuL(L,2,deleteElem);
//
//    return 0;
//}

// 栈：此处讨论的是 顺序栈
//int main() {
//   ---------- SElemType 为int类型 ----------
//    // 输入任意数，转换成八进制
//    // conversion();
//
//    SqStack S;
//
//    // 初始化栈
//    InitStack(S);
//    ElemType e;
//
//    // Push元素进栈
//    for (int i = 0; i <= 4; i++) {
//        e = i + 1;
//        Push(S, e);
//    }
//
//    // Pop出栈中所有元素
//    while (!StackEmpty(S)) {
//        SElemType e;
//        Pop(S, e);
//        printf("%d\n", e);
//    }

//   ---------- SElemType 为char类型 ----------
//   括号匹配
//    char str[100];
//    SqStack S;
//    InitStack(S);
//    printf("input parentheses\n");
//    scanf("%s", str);
//
//    if (ParenthesisMatch(S, str)) {
//        printf("Parenthesis is matched");
//    } else {
//        printf("Parenthesis is not matched");
//    }

//    return 0;
//}

// 单链队列
//int main() {
//
//    LinkQueue Q;
//    InitQueue(Q);
//    EnQueue(Q,4);
//    EnQueue(Q,8);
//    EnQueue(Q,6);
//
//    QElemType  e;
//    DelQueue(Q,e);
//    return 0;
//}

// 循环队列(线性队列的一种)
//int main() {
//    SqQueue SQ;
//    InitQueue(SQ);
//    EnQueue(SQ, 5);
//    EnQueue(SQ, 9);
//    EnQueue(SQ, 7);
//
//    QElemType se; // 实际上是没有删除，而是在后面进队列的时候覆盖掉
//    DelQueue(SQ, se);
//    return 0;
//}

//int main() {
//    // 中缀表达式转为后缀表达式
//    // MiddelToBack();
//
//    // 计算中缀表达式
//    //EvaluateMiddleExpression();
//    return 0;
//}

// TODO KMP算法还不是很清楚，待二次复习来搞清楚
//int main() {
//    SString S = "#abcabaabcabac";;
//
//    SString T = "#abaa";
//
//    int index = Index(S, T, 1);
//    return 0;
//}


int main(){
    BiTree T;
    CreateBiTree(T);
    return 0;
}
