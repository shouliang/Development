#include<stdio.h>
#include<iostream>

typedef char VertexType;  // 顶点类型
typedef int EdgeType;     // 边的权值类型
#define MAXVEX 100        // 最大顶点数
#define INFINITY 65535    // 用65535来代表∞

// ---------- 图的存储结构 ----------

// 邻接矩阵存储
typedef struct {
    VertexType vexs[MAXVEX];      // 顶点集合
    EdgeType arc[MAXVEX][MAXVEX]; // 邻接矩阵，可看作边表
    int numVertexes;              // 图中当前的顶点数
    int numEdges;                 // 图中当前的边数
} MGraph;

/* 建立无向网图的邻接矩阵表示 */
void CreateMGraph(MGraph *G) {
    int i, j, k, w;
    printf("输入顶点数和边数:\n");
    scanf("%d,%d", &G->numVertexes, &G->numEdges);

    // 读入顶点信息
    for (i = 0; i < G->numVertexes; i++) {
        scanf(&G->vexs[i]);
    }

    // 邻接矩阵初始化
    for (i = 0; i < G->numVertexes; i++) {
        for (j = 0; j < G->numVertexes; j++) {
            G->[i][j] = INFINITY;     // 初始值为INFINITY
        }
    }

    // 读入边的信息(起点、终点、权值)
    for (k = 0; k < G->numEdges; k++) {
        printf("请输入(vi,vj)上的下标i,下标j和权w:\n");
        scanf("%d,%d,%d", &i, &j, &w);
        G->arc[i][j] = w;
        G->[j][i] = G->arc[i][j];  // 因为无向图，矩阵对称
    }
}

// 邻接表存储

// 边表结点
typedef struct EdgeNode {
    int adjvex;              // 邻接点，存储该顶点对应的下标，注意是下标
    EdgeType weight;         // 权值，对于非网图可以不需要
    struct EdgeNode *next;   // 指向下一个邻接点的指针
} EdgeNode;

// 顶点表结点
typedef struct VertexNode {
    int in;                    // 顶点入度(此处为拓扑排序服务)
    VertexType data;           // 顶点域，存储顶点信息
    EdgeNode *fristdege;       // 边表 头指针
} VertexNode, AdjList[MAXVEX];


// 邻接表结构
typedef struct {
    AdjList adjList;  // 顶点数组
    int numVertexes;  // 当前顶点数
    int numEdges;     // 当前边数
} GraphAdjList;

void CreateALGraph(GraphAdjList *G) {
    int i, j, k;
    printf("输入顶点数和边数:\n");
    scanf("%d,%d", &G->numVertexes, &G->numVertexes);

    // 建立顶点表
    for (i = 0; i < G->numVertexes; i++) {
        scanf(&G->adjList[i].data);       // 输入顶点信息
        G->adjList[i].fristdege = NULL;   // 将边表置为空表
    }

    // 建立边表
    EdgeNode *e;
    for (k = 0; k < G->numEdges; k++) {
        printf("请输入边(vi,vj)上的顶点序号:\n");
        scanf("%d,%d", &i, &j);
        // 头插法
        e = (EdgeNode *) malloc(sizeof(EdgeNode));
        e->adjvex = j;
        e->next = G->adjList[i].fristdege;
        G->adjList[i].fristdege = e;

        // 无向图，一条边对于两个顶点，故一次就针对顶点i和j分别插入 ，故时间复杂度为n个顶点和e条边 O(n+e)
        e = (EdgeNode *) malloc(sizeof(EdgeNode));
        e->adjvex = i;
        e->next = G->adjList[j].fristdege;
        G->adjList[j].fristdege = e;
    }

}


// ---------- 图的遍历 ----------
// 深度优先遍历
typedef int Boolean;
Boolean visited[MAXVEX];  // 顶点是否已经访问的标志
#define TRUE 1;
#define FALSE 0;

// 邻接矩阵深度优先递归遍历(对邻接矩阵中下标为i的顶点进行深度优先遍历)
void DFS(MGraph G, int i) {
    visited[i] = TRUE;      // 下标为i的顶点已被访问
    printf("%c", G.vexs[i]);  // 打印顶点下标，也可以进行其他操作

    int j;
    for (j = 0; j < G.numVertexes; j++) {
        if (G.arc[i][j] == 1 && !visited[j]) {    // 对i的未被访问过的邻接顶点进行递归访问
            DFS(G, j);
        }
    }
}

// 邻接矩阵的深度遍历操作
void DFSTraverse(MGraph G) {
    int i;
    for (i = 0; i < G.numVertexes; i++) {
        visited[i] = FALSE;       // 初始化所有顶点的状态都是未访问
    }

    for (i = 0; i < G.numVertexes; i++) {
        if (!visited) {             // 对未被访问过的顶点调用DFS,若是连通图，只会执行一次，若是非连通图另选一个未被访问的顶点进行深度遍历
            DFS(G, i);
        }
    }
}

// 邻接表和邻接矩阵的代码几乎是相同的，只是将数组换成了链表
// 邻接表的深度优先递归算法(针对邻接表中下标为i的顶点进行深度优先遍历)
void _DFS(GraphAdjList GL, int i) {
    EdgeNode *p;
    visited[i] = TRUE;
    printf("%c", GL.adjList[i].data);
    p = GL.adjList[i].fristdege;

    while (p) {
        if (!visited[p->adjvex]) {
            _DFS(GL, p->adjvex);       // 对未被访问过的邻接顶点进行递归调用
        }
        p = p->next;
    }
}

// 邻接表的深度遍历操作
void _DFSTraverse(GraphAdjList GL) {
    int i;
    for (i = 0; i < GL.numVertexes; i++) {
        visited[i] = FALSE;           // 初始化所有顶点的状态都是未被访问过的
    }

    for (i = 0; i < GL.numVertexes; i++) {
        if (!visited[i]) {
            _DFS(GL, i);             // 对未被访问过的顶点进行深度优先遍历，若是连通图，只会执行一次
        }
    }
}

// 广度优先遍历
// 邻接矩阵的广度优先遍历
void BFSTraverse(MGraph G) {
    int i, j;
    for (i = 0; i < G.numVertexes; i++) {
        visited[i] = FALSE;            // 初始化顶点都是未被访问的
    }

    //Queue Q;
    //InitQueue(&Q);  // 初始化辅助用的队列，存储某顶点未被访问过的邻接顶点，然后再按顺序遍历这些邻接顶点
    for (i = 0; i < G.numVertexes; i++) {
        if (!visited[i]) {
            visited[i] = TRUE;
            printf("%c", G.vexs[i]);
            //EnQueue(&Q,i);         // 将此顶点入队列
            //while(!QueueEmpty(Q))  // 如果队列不为空
            {
                //DeQueue(&Q,i)         // 出队列
                for (j = 0; j < G.numVertexes; j++) {
                    if (G.arc[i][j] == 1 && !visited[i]) {
                        visited[j] = TRUE;
                        printf("%c", G.vexs[j]);
                        //EnQueue(&Q,j)  // 将顶点的邻接顶点入队列 ，直到顶点的邻接顶点全部出队列，再访问下一个未被访问过顶点的邻接顶点
                    }
                }
            }
        }
    }
}

// 邻接表的广度优先遍历
void _BFSTraverse(GraphAdjList GL) {
    int i;
    for (i = 0; i < GL.numVertexes; i++) {
        visited[i] = FALSE;
    }

    EdgeNode *p;
    // Queue Q;
    // InitQueue(&Q)
    for (i = 0; i < GL.numVertexes; i++) {
        if (!visited[i]) {
            visited[i] = TRUE;
            printf("%c", GL.adjList[i].data);
            // EnQueue(&Q,i);
            //while(!QueueEmpty(Q))
            {
                // DeQueue(&Q,&i);
                p = GL.adjList[i].fristdege;
                while (p) {
                    if (!visited[p->adjvex]) {
                        visited[p->adjvex] = TRUE;
                        printf("%c", GL.adjList[p->adjvex].data);
                        // EnQueue(&Q,p->adjvex)
                    }
                    p = p->next;
                }
            }
        }
    }
}


// ---------- 最小生成树 包含所有顶点且边的权值之和最小 ----------
// 普利姆算法 Prime
void MiniSpanTree_Prime(MGraph G) {
    int i, j, k, min;
    int adjvex[MAXVEX];  // 相关顶点下标
    int lowcost[MAXVEX]; // 相关边最小的权值
    lowcost[0] = 0;      // 初始化第一个权值为0，即v0加入生成树
    adjvex[0] = 0;       // 初始化第一个顶点下标为0

    for (i = 0; i < G.numVertexes; i++) {
        lowcost[i] = G.arc[0][i];    // 顶点v0的邻接边的权值存入数组
        adjvex[i] = 0;
    }

    for (i = 1; i < G.numVertexes; i++) {
        min = INFINITY;
        j = 1;
        k = 0;
        while (j < G.numVertexes) {
            if (lowcost[j] != 0 && lowcost[j] < min) {  // 找出邻接点权值最小的顶点k
                min = lowcost[j];
                k = j;
            }
            j++;
        }
        printf("(%d,%d)", adjvex[k], k);
        lowcost[k] = 0;                               // 将当前顶点的权值设置0，表示此顶点已完成

        for (j = 1; j < G.numVertexes; j++) {              // 若下标W为k的顶点小于此前这些顶点未被加入生成树的权值，将较小的权值存入lowcost
            if (lowcost[j] != 0 && G.arc[k][j] < lowcost[j]) {
                lowcost[j] = G.arc[k][j];
                adjvex[j] = k;
            }
        }
    }
}


// 克鲁斯卡尔算法 Kruskal   按边的权值从小到大排序
// 边集合数组结构表示图
typedef struct {
    int begin;
    int end;
    int weight;
} Edge;

// 查找连线顶点的尾部下标是否已经在parent数组中
int Find(int *parent, int f) {
    while (parent[f] > 0) {
        f = parent[f];
    }

    return f;
}

#define EDGES 10    // 边的最大数目
#define VEXS 10     // 顶点的最大数目

void MiniSpanTree_Kruskal(MGraph G) {
    int i;
    Edge edges[EDGES];  // 定义边集数组
    int parent[VEXS];   // 定义一个数组用来判断是否构成环

    /*此处省略将邻接矩阵G转换成边集数组edges并按权值从小到大排序的代码*/
    int n, m;
    for (i = 0; i < G.numEdges; i++) {     // 循环每一条边
        n = Find(parent, edges[i].begin);
        m = Find(parent, edges[i].end);
        if (n != m) {         // n与m不相等，说明此边与现有生成树不构成环
            parent[n] = m; // 将此边的结尾顶点放入下标为起点的parent数组中，表示此顶点已经在生成树集合中
            printf("(%d,%d) %d", edges[i].begin, edges[i].end, edges[i].weight);
        }
    }

}


// ---------- 最短路径 ----------
// 迪杰斯特拉算法 从单个源点到其余各顶点的最短路径
#define VEXNUMS 9
typedef int Pathmatrix[VEXNUMS];     // 存储最短路径顶点下标
typedef int ShortPathTable[VEXNUMS]; // 存储源点到其余各顶点的最短路径权值

void ShortestPath_Dijsktra(MGraph G, int v0, Pathmatrix *P, ShortPathTable *D) {
    int v;
    int final[VEXNUMS];              // final[w] = 1表示已经求得v0到v(w)的最短路径

    // 初始化
    for (v = 0; v < G.numVertexes; v++) {
        final[v] = 0;
        (*D)[v] = G.arc[v0][v];     // v0到邻接点的权值
        (*P)[v] = 0;                // 初始化下标全部为0
    }
    (*D)[v0] = 0;      // v0到v0的路径为0
    final[v0] = 1;     // v0加入已求得的v0到v0的最短路径

    int min;
    int k, w;
    // 主循环、每次求得v0到某个顶点v的最短路径，更新最短路径数组D和顶点下标数组P
    for (v = 1; v < G.numVertexes; v++) {   // 其余G.numVertexes -1 个顶点
        min = INFINITY;
        for (w = 0; w < G.numVertexes; w++) {     // 寻找离v0最近的顶点
            if (final[w] != 1 && (*D)[w] < min) {
                min = (*D)[w];
                k = w;
            }
        }

        final[k] = 1;
        for (w = 0; w < G.numVertexes; w++) {    // 如果经过v顶点的路径比现在这条路径还短，就修正当前最短路径
            if (final[w] != 1 && (min + G.arc[k][w]) < (*D)[w]) {
                (*D)[w] = min + G.arc[k][w];
                (*P)[w] = k;
            }
        }
    }
}


// 佛洛依德算法 每一对顶点之间的最短路径
typedef int Pathmatrix_[VEXNUMS][VEXNUMS];
typedef int ShortPathtable_[VEXNUMS][VEXNUMS];

/*Floyd算法，求网图G中各顶点v到其余顶点w的下标的最短路径P[v][w]和带权长度D[v][w]*/
void ShortestPath_Floyd(MGraph G, Pathmatrix_ *P, ShortPathtable_ *D) {
    int v, w, k;
    // 初始化
    for (v = 0; v < G.numVertexes; v++) {
        for (w = 0; w < G.numVertexes; w++) {
            (*D)[v][w] = G.arc[v][w];
            (*P)[v][w] = w;
        }
    }

    // 三重循环 详情见：http://wiki.jikexueyuan.com/project/easy-learn-algorithm/floyd.html
    for (k = 0; k < G.numVertexes; k++) {
        for (v = 0; v < G.numVertexes; v++) {
            for (w = 0; w < G.numVertexes; w++) {
                if ((*D)[v][w] > (*D)[v][k] + (*D)[k][w]) {  // 如果经过下标为k的顶点路径比原两点见路径更短，就将当期两点见的权值设置为更小的一个
                    (*D)[v][w] = (*D)[v][k] + (*D)[k][w];
                    (*P)[v][w] = (*P)[v][k];               // 路径设置经过下标为k的顶点
                }
            }
        }
    }
}

// ---------- 拓扑排序 ----------
// 拓扑排序是一种排序，这种排序要求先做什么，后做什么，活动与活动之间存在先后顺序
int TopologicalSort(GraphAdjList GL) {
    EdgeNode *e;
    int top = 0;
    int gettop;
    int *stack = (int *) malloc(GL.numVertexes * sizeof(int));
    int count = 0;
    int i, k;

    // 将入度为0的顶点入栈
    for (i = 0; i < GL.numVertexes; i++) {
        if (GL.adjList[i].in == 0) {
            stack[++top] = i;
        }
    }

    while (top != 0) {
        gettop = stack[top--];                   // 出栈
        printf("%d ->", GL.adjList[gettop].data); // 输出数据域
        count++;                                 // 统计输出顶点个数

        // 对此顶点的弧表进行遍历
        for (e = GL.adjList[gettop].fristdege; e; e = e->next) {
            k = e->adjvex;
            GL.adjList[k].in = GL.adjList[k].in - 1; // 将k号顶点的邻接点的入度减1
            if (GL.adjList[k].in == 0) {
                top = top + 1;
                stack[top] = k;                     // 若为0则入栈，以便下次循环输出
            }
        }
    }

    // 如果count小于顶点数，说明存在环
    if (count < GL.numVertexes) {
        return 0;
    }

    return 1;

}


// ---------- 关键路径 ----------
// AOE边上的权值表示活动持续的时间，AOE是建立在活动之间制约关系没有矛盾的基础上，再来分析完成整个工程至少需要多少时间
// 从源点到汇点具有的最大长度的路径叫关键路径，只有完成最长的工期完成后，项目才算真正的完成，在路径上的活动叫关键活动
// 同城AOE只有一个表示开始的源点和一个表示结束的汇点

/*
算法思想：
要准备两个数组，a：最早开始时间数组etv，b：最迟开始时间数组ltv（针对顶点即事件而言）
1.从源点V0出发，令etv[0]（源点）=0，按拓扑有序求其余各顶点的最早发生时间etv[i]（1 ≤ i ≤ n-1）。同时检测拓扑排序是否有环存在。
2.从汇点Vn出发，令ltv[n-1] = etv[n-1]，按拓扑排序求各个其余各顶点的最迟发生时间ltv[i]（n-2 ≥ i ≥ 2）;
3.根据各顶点的etv和ltv数组的值，求出弧（活动）的最早开工时间和最迟开工时间，求每条弧的最早开工时间和最迟开工时间是否相等，若相等，则是关键活动。
*/


int *etv, *ltv;    // 事件最早发生时间和最迟发生时间数组
int *stack2;      // 用于存储拓扑排序列的栈
int top2;         // 用于stack2的指针

// 为关键路径而改造后的拓扑排序
int TopologicalSort_CriticalPath(GraphAdjList GL) {
    EdgeNode *e;
    int top = 0;
    int gettop;
    int *stack = (int *) malloc(GL.numVertexes * sizeof(int));
    int count = 0;
    int i, k;

    // 将入度为0的顶点入栈
    for (i = 0; i < GL.numVertexes; i++) {
        if (GL.adjList[i].in == 0) {
            stack[++top] = i;
        }
    }

    // 新增的部分1 begin
    top2 = 0;
    etv = (int *) malloc(GL.numVertexes * sizeof(int));
    for (i = 0; i < GL.numVertexes; i++) {
        etv[i] = 0;  // 初始化为0
    }
    stack2 = (int *)malloc(GL.numVertexes * sizeof(int *));  // 存储拓扑排序的顶点
    // 新增的部分1 end


    while (top != 0) {
        gettop = stack[top--];                    // 出栈
        printf("%d ->", GL.adjList[gettop].data); // 输出数据域
        count++;                                  // 统计输出顶点个数

        // 新增的部分2 begin
        stack2[++top2] =  gettop;  // 将弹出的顶点序号压入拓扑序列的栈
        // 新增的部分2 end

        // 对此顶点的弧表进行遍历
        for (e = GL.adjList[gettop].fristdege; e; e = e->next) {
            k = e->adjvex;
            GL.adjList[k].in = GL.adjList[k].in - 1; // 将k号顶点的邻接点的入度减1
            if (GL.adjList[k].in == 0) {
                top = top + 1;
                stack[top] = k;                     // 若为0则入栈，以便下次循环输出
            }

            // 新增部分3 begin
            if(etv[gettop] + e->weight > etv[k]) {
                etv[k] = etv[gettop] + e->weight;   // 各顶点的最早发生时间（最早发生时间取决于最长的路径，只有最长路径发生后，它才可以执行）
            }
            // 新增部分3 end


        }
    }

    // 如果count小于顶点数，说明存在环
    if (count < GL.numVertexes) {
        return 0;
    }

    return 1;

}

// 求关键路径，GL为有向图，输出GL的各项关键活动
void CriticalPath(GraphAdjList GL) {
    EdgeNode *e;
    int ete, lte;

    TopologicalSort_CriticalPath(GL);  // 得到拓扑排序，并取得etv和stack2的值
    ltv = (int *)malloc(GL.numVertexes * sizeof(int *));
    // 初始化ltv
    int i;
    for (i=0; i < GL.numVertexes;i++) {
        ltv[i] = etv[GL.numVertexes -1];
    }

    // 计算ltv
    int gettop,k ;
    while(top2 !=0) {
        gettop = stack2[top2--];   // 将拓扑排序数组从最后一个开始遍历
        for(e = GL.adjList[gettop].fristdege;e;e=e->next){
            // 求各顶点事件的最迟发生时间ltv值
            k = e->adjvex;
            if(ltv[k] - e->weight < ltv[gettop]) {
                ltv[gettop] = ltv[k] - e->weight;
            }
        }
    }

    // 求关键活动
    for(i =0; i< GL.numVertexes;i++){
        for(e=GL.adjList[i].fristdege;e;e=e->next) {
            k = e->adjvex;
            ete = etv[i];             // 活动最早发生时间
            lte = ltv[k] - e->weight; // 活动最迟发生时间

            // 两者相等即在关键路径上
            if(ete == lte) {
                printf("<%d,%d> length %d ,",GL.adjList[i].data,GL.adjList[k].data,e->weight);
            }
        }
    }


}

int main() {

    return 0;
}