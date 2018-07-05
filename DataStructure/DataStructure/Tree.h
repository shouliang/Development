//
// Created by 朱守亮 on 2017/9/29.
//

// ------------------------- 树的存储结构(注意：非二叉树) -------------------------

// 1.双亲表示法
#define MAX_TREE_SIZE 100
typedef int TElemType;
struct PTNode {
    TElemType data;
    int parent;  // 双亲位置
};

typedef PTNode PTNode;

typedef struct {
    PTNode node[MAX_TREE_SIZE];
    int r, n;   // 根的位置和结点数
} PTree;

// 2.孩子表示法
struct CTNode {           // 孩子结点
    int child;
    struct CTNode *next;
};
typedef CTNode *ChildPtr;

typedef struct {         // 表头结构
    TElemType data;
    // int parent;       // 如定义了双亲的位置，则为双亲孩子表示法，此方法可知道结点的双亲
    ChildPtr firstchild;
} CTBox;

typedef struct {        // 树结构
    CTBox nodes[MAX_TREE_SIZE];
    int r, n;
} CTree;

// 3.孩子兄弟表示法(第一个孩子和右兄弟)，这种表示法的最大好处就是把一颗复杂的树变成了一颗二叉树
struct CSNode {
    TElemType data;
    struct CSNode *fristchild, *rightsib;
};

typedef CSNode CSNode;
typedef CSNode *CSTree; // 头指针
