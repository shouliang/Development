#include <iostream>
#include "stdio.h"

#define MAXSIZE 5     // 用于要排序数组个数最大值

typedef struct {
    int r[MAXSIZE + 1]; // 用于存储要排序数组，r[0]用作哨兵或临时变量
    int length;         // 用于记录顺序表的长度
} SqList;


// 交换L中数组r下标为i和j的值
void swap(SqList *L, int i, int j) {
    int temp = L->r[i];
    L->r[i] = L->r[j];
    L->r[j] = temp;
}

// ----- 交换排序 -----
// 冒泡排序
// 基本思想：两两比较相邻记录的关键字，如果反序则交换，直到没有反序的记录为止
void BubbleSort(SqList *L) {
    int i, j;
    for (i = 1; i < L->length; i++) {
        for (j = L->length - 1; j >= i; j--) {
            if (L->r[j] > L->r[j + 1]) {  // 两两比较将小的不断地交换到最前面，就像气泡一样慢慢冒上去，每次称为一趟
                swap(L, j, j + 1);
            }
        }
    }
}


// 快速排序
// 交换顺序表L中子表的记录，使枢轴记录到位，并返回其所在位置
// 此时在它之前的记录均小于或者等于它，在它之后的记录都大于它
int Partition(SqList *L, int low, int high) {
    int pivotkey;
    pivotkey = L->r[low];                               // 用子表的第一个记录作枢轴记录
    while (low < high) {                                // 从表的两端交替向中间扫描

        while (low < high && L->r[high] >= pivotkey) {
            high--;
        }
        swap(L, low, high);                             // 将比枢轴记录小的记录交换到低端

        while (low < high && L->r[low] <= pivotkey) {
            low++;
        }
        swap(L, low, high);                             // 将比枢轴记录大的记录交换到高端
    }

    return low;                                         // 返回枢轴所在位置
}

// 对顺序表L中的子序列L->r[low...high]作快速排序
void QSort(SqList *L, int low, int high) {
    int pivot;
    if (low < high) {
        pivot = Partition(L, low, high);   // 将L->r[low...high]一分为二,算出枢轴值为pivot

        QSort(L, low, pivot - 1);          // 对低子表递归排序
        QSort(L, pivot, high);             // 对高子表递归排序
    }
}

// 对顺序表L作快速排序,只此一句
void QuickSort(SqList *L) {
    QSort(L, 1, L->length);
}

// ----- 插入排序 -----
// 基本思想：假设待排序的记录存放在数组R[1..n]中。初始时，R[1]自成1个有序区，无序区为R[2..n]。从i=2起直至i=n为止，依次将R[i]插入当前的有序区R[1..i-1]中，生成含n个记录的有序区。
// 直接插入排序
void InsertSort(SqList *L) {
    int i, j;
    for (i = 2; i <= L->length; i++) { // 初始r[0]设置为哨兵，r[1]自成一个有序区，故i从2开始
        // L->r[i] < L->r[i -1])，需要将L->r[i]插入到r[1..i-1]有序子表中(从小到大)，否则L->r[i]已经有序
        if (L->r[i] < L->r[i - 1]) {
            L->r[0] = L->r[i];                        // 将L->r[i]赋值给L->r[0]，将其设置为哨兵，以方便后面逐个比较大小

            for (j = i - 1; L->r[j] > L->r[0]; j--) { // L->r[i]逐个与前面1到i-1的元素进行比较，找到合适的插入位置
                L->r[j + 1] = L->r[j];                // 从右向左逐个比较，并后移元素，第j个位置赋值到第j+1的位置，但此时循环条件中j--,故实际空出的是j+1的位置
            }

            L->r[j + 1] = L->r[0];                    // 直接将之前作为哨兵的r[0]插入到j+1的位置上
        }
    }
}

/* 希尔排序
 * 基本思想: 先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。所有距离为dl的倍数的记录放在同一个组中。
 *         先在各组内进行直接插人排序；然后，取第二个增量d2<d1重复上述的分组和排序，直至所取的增量dt=1(dt<dt-l<…<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。
 *         希尔排序又称为“缩小增量排序”.
 *         该方法实质上是一种分组插入方法。
 * 稳定性：不稳定
 * 当增量d=1时，ShellPass和InsertSort基本一致，只是由于没有哨兵而在内循环中增加了一个循环判定条件"j>0"，以防下标越界。
*/
void ShellSort(SqList *L) {
    int i, j;
    int increment = L->length;

    do {
        increment = increment / 3 + 1;   // 增量序列,最后一次的值必须为1，此时就等同于直接插入排序了，对3求余+1也只是一种求下一个增量的方法，还有其他形式

        for (i = increment + 1; i <= L->length; i++) {

            if (L->r[i] < L->r[i - increment]) {
                L->r[0] = L->r[i];      //r[0]只是暂存单元，不是哨兵

                for (j = i - increment; L->r[j] > L->r[0] && j > 0; j -= increment) {  // j>0，以防下标越界
                    L->r[j + increment] = L->r[j];
                }

                L->r[j + increment] = L->r[0];
            }
        }

    } while (increment > 1);


}


// ----- 选择排序 -----
// 简单选择排序
void SelectSort(SqList *L) {
    int i, j, min;
    for (i = 1; i < L->length; i++) {
        min = i;

        // 从L->r[i+1...length]中选择最小的，然后与第i个记录进行交换
        for (j = i + 1; j <= L->length; j++) {
            if (L->r[j] < L->r[min]) {
                min = j;
            }
        }

        // 与第i个记录进行交换，如果i==min，说明第i个记录就是最小的，无需进行交换
        if (i != min) {
            swap(L, i, min);
        }
    }
}
// 堆排序 todo

// ----- 归并排序 -----
// 归并排序
// 将有序的SR[i...m]和SR[m...n]归并为有序的TR[i...n]:即将两个有序表合并为一个有序表
void Merge(int SR[], int TR[], int i, int m, int n) {
    int k, j;
    for (k = i, j = m + 1; i <= m && j <= n; k++) {
        if (SR[i] < SR[j]) {
            TR[k] = SR[i];
            i++;
        } else {
            TR[k] = SR[j];
            j++;
        }
    }

    int l;
    // 将剩余的SR[i...m]复制到TR
    if (i <= m) {
        for (l = 0; l <= m - i; l++) {
            TR[k + 1] = SR[i + l];
        }
    }

    // 将剩余的SR[j...j]复制到TR
    if (j <= n) {
        for (l = 0; l <= n - j; j++) {
            TR[k + 1] = SR[j + 1];
        }
    }
}

// 将SR[s...t]一分为二归并到TR1[s...t]中
void MSort(int SR[], int TR1[], int s, int t) {
    int m;
    int TR2[MAXSIZE + 1];
    if (s == t) {
        TR1[s] = SR[s];
    } else {
        m = (s + t) / 2;          // 将SR[s...t]平分为SR[s...m]和SR[m+1...t]
        MSort(SR, TR2, s, m);     // 递归将SR[s...m]归并为有序TR2[s...m]
        MSort(SR, TR2, m + 1, t); // 递归将SR[m+1...t]归并为有序TR2[m+1...t]
        Merge(TR2, TR1, s, m, t); // 将TR2[s...m]和TR2[m+1...t]归并到TR1[s...t]中
    }
}

void MergeSort(SqList *L) {
    MSort(L->r, L->r, 1, L->length);
}


int main() {
//    SqList *L1;
//    L1->r[0] = 0; // r[0]=0设置为哨兵的初始值
//    L1->r[1] = 5;
//    L1->r[2] = 3;
//    L1->r[3] = 4;
//    L1->r[4] = 6;
//    L1->r[5] = 2;
//    L1->length = 5;
//
//    InsertSort(L1);

    SqList *L2;
    L2->r[0] = 0;
    L2->r[1] = 6;
    L2->r[2] = 9;
    L2->r[3] = 20;
    L2->r[4] = 15;
    L2->r[5] = 11;
    L2->length = 5;
    //ShellSort(L2);
    BubbleSort(L2);

    return 0;
}