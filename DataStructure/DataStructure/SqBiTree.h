//
// Created by 朱守亮 on 2017/9/18.
//

// 二叉树特点：1.最大只有两颗子树 2.左右子树是有顺序的
/*
 * 满二叉树，简单理解就是“满”，所有分支都存在左子树和右子树，并且所有叶子都在同一层上
 * 完全二叉树：按层次编号与满二叉树的结点一一对应，且不出现空挡
 */

// ----- 二叉树的顺序存储表示 -----
#include <cstdio>
#include <sys/malloc.h>  // MAC平台引入malloc.h需要加入sys
#include <cstdlib>       // MAC平台使用malloc函数需要引入的头文件

#define MAX_TREE_SIZE 100
typedef int TElemType;
typedef TElemType SqBiTree[MAX_TREE_SIZE];

SqBiTree bt;
// 用一组地址连续的存储单元依次自上而下、自左至右存储完全二叉树上的结点元素
// 即将完全二叉树上编号为i的结点元素存储在一维数组中下标为i-1的分量中
// 这种顺序存储仅适用于完全二叉树，因为在最坏的情况下，一个深度为n且只有n个结点的单叉树，却需要长度为2ⁿ-1的一维数组

// ----- 二叉树的链式存储结构之二叉链表 -----
typedef struct BiTNode {
    TElemType data;
    struct BiTNode *lchild, *rchild; // 左右孩子指针
} BiTNode, *BiTree;  // BinTree为指向BinTNode类型结点的指针类型,即指向根结点的头指针

Status CreateBiTree(BiTree &T) {
    TElemType data;
    scanf("%d", &data);
    if (data == 0) {
        T = NULL;
        return 0;
    } else {
        T = (BiTNode *) malloc(sizeof(BiTNode));
        if (!T) {
            exit(OVERFLOW);
        }
        T->data = data;
        CreateBiTree(T->lchild);
        CreateBiTree(T->rchild);
    }
    return OK;
}

void PreOrderTraverse(BiTree T) {
    if (T == NULL) return;
    printf("%d", T->data);
    PreOrderTraverse(T->lchild);
    PreOrderTraverse(T->rchild);
}

// 二叉树的二叉线索存储
typedef enum {
    Link, Tread
} PointerTag; // Link ==0 表示指向左右孩子的指针；Thread ==1 表示指向前驱或后继的线索

typedef struct BiThrNode {
    TElemType data;
    struct BiThrNode *lchild, *rchild;
    PointerTag LTag;
    PointerTag RTag;
} BiThrNode, *BiThrTree;

BiThrTree pre;

void InThreading(BiThrTree p) {
    if (p) {
        InThreading(p->lchild);
        if (!p->lchild) {
            p->LTag = Tread;
            p->lchild = pre;
        }
        if (!pre->rchild) {
            pre->LTag = Tread;
            pre->rchild = p;
        }

        pre = p;
        InThreading(p->rchild);
    }
}


