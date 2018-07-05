#include <iostream>
#include <stdio.h>

// 静态查找表、动态查找表：若在查找的同时对表做修改操作(如插入和删除)，则相应的表称之为动态查找表。否则称之为静态查找表。

typedef int KeyType;
typedef int ElemType;
typedef struct {
    ElemType *elem;
    int length;
} SSTable;

// 顺序查找
int Search_Seq(SSTable ST, KeyType key) {
    ST.elem[0] = key;  // 设置"哨兵"

    int i = ST.length; // 从数组尾部开始
    while (ST.elem[i] != key) {
        i--;
    }

    return i;
}

// ---------- 有序表的查找 ----------
// 二分查找(折半查找)
int Binary_search(SSTable ST, KeyType key) {
    int low, high, mid;
    low = 1;
    high = ST.length;
    while (low < high) {
        mid = (low + high) / 2;
        if (key < ST.elem[mid]) {
            high = mid - 1;
        } else if (key > ST.elem[mid]) {
            low = mid + 1;
        } else {
            return mid;
        }
    }

    return 0;
}


// 线索查找

// ---------- 树上的查找 ----------
// 二叉排序树
typedef struct BiTNode {
    int data;
    struct BiTNode *lchild, *rchild;
} BITNode, *BiTree;

typedef int Status;
#define TRUE 1
#define FALSE 0


// 递归查找二叉排序树T中是否存在key
// 指针f指向T的双亲，其初始调用值为NULL
// 若查找成功，则指针p指向该数据元素结点，并返回TRUE
// 否则指针p指向查找路径上访问的最后一个结点并返回FALSE
Status SearchBST(BiTree T, int key, BiTree f, BiTree *p) {
    if (T == NULL) {
        *p = f;
        return FALSE;
    }
    if (key == T->data) {
        *p = T;
        return TRUE;
    }
    if (key < T->data) {
        return SearchBST(T->lchild, key, T, p);
    }
    if (key > T->data) {
        return SearchBST(T->rchild, key, T, p);
    }
}

// 二叉排序树的插入
Status InsertBST(BiTree *T, int key) {
    BiTree p, s;

    if (SearchBST(*T, key, NULL, &p)) {  // 查找不成功，则插入新结点
        // 生成新的二叉树结点
        s = (BITNode *) malloc(sizeof(BITNode));
        s->data = key;
        s->lchild = NULL;
        s->rchild = NULL;

        // 插入新结点
        if (!p) {
            *T = s;             // 插入s为新的根结点
        }
        if (key < p->data) {
            p->lchild = s;      // 插入s为左孩子
        }
        if (key > p->data) {
            p->rchild = s;      // 插入s为右孩子
        }

    } else {
        return FALSE;           // 树中已有关键字相同的结点，不再插入
    }
}

// 从二叉排序树中删除结点p，并重新拼接它的左子树或者右子树
Status Delete(BiTree *p) {
    BiTree q;                          // 保存删除结点p的临时变量
    BiTree s;
    if ((*p)->lchild == NULL) {        // 删除结点的左子树为空
        q = *p;
        *p = (*p)->rchild;             // 将删除结点的右子树拼接到p上
        free(q);
    } else if ((*p)->rchild == NULL) { // 删除结点的右子树为空
        q = *p;
        *p = (*p)->lchild;
        free(q);
    } else {                          // 删除结点的右子树为都不为空
        q = *p;

        s = (*p)->lchild;              // 找到左子树的最右的结点（这个结点是删除结点的前驱）
        while (s->rchild) {
            q = s;
            s = s->rchild;
        }
        (*p)->data = s->data;         // 替换删除结点p的data值为s的值

        if (q == (*p)) {              // q==(*p)说明没有执行上面的while循环，即重接左子树 ，否则重接右子树
            q->lchild = s->lchild;
        } else {
            q->rchild = s->lchild;
        }
    }
    return TRUE;
}

// 若二叉排序树T中存在关键字等于key的数据元素，则删除该数据元素，并返回TRUE,否则返回FALSE
Status DeleteBST(BiTree *T, int key) {
    if (*T == NULL) {
        return FALSE;
    } else {
        if (key == (*T)->data) {
            return Delete(T);
        }
        if (key < (*T)->data) {
            return DeleteBST(&(*T)->lchild, key);
        }
        if (key > (*T)->data) {
            return DeleteBST(&(*T)->rchild, key);
        }
        return TRUE;
    }

}


// 平衡二叉树(AVL树)  todo


// 多路查找树(B树)   todo


// ---------- 散列 ----------
// 散列函数的构造

// 处理散列冲突

// 散列表的查找
#define SUCCESS 1
#define UNSUCESS 0
#define HASHSIZE 12
#define NULLKEY -32768
typedef struct {
    int *elem;   // 数据元素存储基址
    int count;   // 当前数据元素个数
} HashTable;

int m = 12;

// 初始化散列表
Status InitHashTable(HashTable *H) {
    H->count = HASHSIZE;
    H->elem = (int *) malloc(HASHSIZE * sizeof(int));

    int i;
    for (i = 0; i < H->count; i++) {
        H->elem[i] = NULLKEY; // 初始化为NULLKEY
    }
    return 1;
}

// 散列函数
int Hash(int key) {
    return key % m; // 求余法
}

void InsertHash(HashTable *H, int key) {
    int addr = Hash(key);    // 求散列地址

    while (H->elem[addr] != NULLKEY) { // 如果不为空则冲突
        addr = (addr + 1) % m;         // 开放定址法的线性探索
    }

    H->elem[addr] = key;
}

// 散列表查找关键字
Status SearchHash(HashTable H, int key, int *addr) {
    *addr = Hash(key);
    while (H.elem[*addr] != key) {       // 如果不是关键字，则冲突，需要重新寻址

        *addr = (*addr + 1) % m;         // 开放定址法的线性探测

        if (H.elem[*addr] == NULLKEY || *addr == Hash(key)) {  // H.elem[*addr] == NULLKEY 说明没找到，
            // *addr == Hash(key)，说明循环回到原点，也即没有找到
            return UNSUCESS;
        }
    }

    return SUCCESS;
}

int main() {
    SSTable ST;
    ElemType elem[] = {8, 4, 9, 3, 5, 7};
    ST.elem = elem;
    ST.length = sizeof(elem) / sizeof(ElemType);

    // 顺序查找
    KeyType key1 = 9;
    int location1 = Search_Seq(ST, key1);
    printf("seqSearch %d location is %d\n", key1, location1);

    // 二分查找
    ElemType elemOrdered[] = {1, 2, 3, 8, 9, 10, 24, 56, 101};
    ST.elem = elemOrdered;
    KeyType key2 = 9;
    int location2 = Search_Seq(ST, key2);
    printf("binSearch %d location is %d\n", key2, location2);

    // 生成二叉排序树 （循环插入新结点到二叉树）
    int i;
    int a[10] = {62, 88, 58, 47, 35, 73, 51, 99, 37, 93};
    BiTree T = NULL;
    for (i = 0; i < 10; i++) {
        InsertBST(&T, a[i]);
    }

    // Hash查找
    int hashData[] = {12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34};
    HashTable ht;
    InitHashTable(&ht);

    int hashDataLength = sizeof(hashData) / sizeof(int);
    for (int i = 0; i < hashDataLength; i++) {
        InsertHash(&ht, hashData[i]);
    }

    int hkey1 = 56;
    int find1 = SearchHash(ht, hkey1, ht.elem);
    if (find1 == 1) {
        printf("find %d is success\n", hkey1);
    }
    if (find1 == 0) {
        printf("find %d is failure\n", hkey1);
    }

    int hkey2 = 49;
    int find2 = SearchHash(ht, hkey2, ht.elem);
    if (find2 == 1) {
        printf("find %d is success\n", hkey2);
    }
    if (find2 == 0) {
        printf("find %d is failure\n", hkey2);
    }

    return 0;
}