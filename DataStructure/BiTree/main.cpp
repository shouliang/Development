#include<stdio.h>
#include<iostream>

// 二叉树的二叉链表结点定义
typedef struct BiTNode {
    char data;
    struct BiTNode * lchild,* rchild;
} BiTNode;

typedef BiTNode * BiTree;

//先序拓展序列建立二叉树
void CreateBiTree(BiTree &T) {   // &表示参数按引用传递，这是一个知识点
    printf("Enter the data \n");
    T = (BiTNode *) malloc(sizeof(BiTNode));
    scanf(" %c", &T->data);

    if (T->data == '#') T = NULL;
    if (T) {
        printf("");
        CreateBiTree(T->lchild);
        CreateBiTree(T->rchild);
    }
}

//先序遍历 (递归)
void PreOrderTraverse(BiTree T) {
    if (T) {
        printf(" %c", T->data);  // 访问根结点

        PreOrderTraverse(T->lchild);        // 遍历左子树
        PreOrderTraverse(T->rchild);        // 遍历右子树
    }
}

//中序遍历 （递归）
void InOrderTraverse(BiTree T) {
    if (T) {
        InOrderTraverse(T->lchild);

        printf(" %c", T->data);

        InOrderTraverse(T->rchild);
    }
}

//后序遍历 （递归）
void PostOrderTraverse(BiTree T) {
    if (T) {
        PostOrderTraverse(T->lchild);
        PostOrderTraverse(T->rchild);

        printf(" %c", T->data);
    }
}

int main() {
    //建树
    printf("The fuction CreateBiTree() is called.\n");
    BiTree T;
    CreateBiTree(T);

    //三种遍历递归算法
    printf("\n");
    printf("The fuction PreOrderTraverse() is called.\n");
    PreOrderTraverse(T);

    printf("\n");
    printf("The fuction InOrderTraverse() is called.\n");
    InOrderTraverse(T);

    printf("\n");
    printf("The fuction PostOrderTraverse() is called.\n");
    PostOrderTraverse(T);


    printf("\n");
    return 0;

    //AB#D##C##

}