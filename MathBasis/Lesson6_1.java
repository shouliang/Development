import java.util.Arrays;

// 归并排序
public class Lesson6_1 {

    /**
     * 使用函数的递归(嵌套)调用，实现归并排序(从小到大)
     *
     * @param tosort 等待排序的数组
     * @return 排序后的数组
     */
    public static int[] merge_sort(int[] tosort) {
        if (tosort == null) return new int[0];

        if (tosort.length == 1) return tosort;

        // 将数组分解成左右两半
        int mid = tosort.length / 2;
        int[] left = Arrays.copyOfRange(tosort, 0, mid);
        int[] right = Arrays.copyOfRange(tosort, mid, tosort.length);

        // 嵌套调用，对两半分别进行排序
        left = merge_sort(left);
        right = merge_sort(right);

        // 合并排序后的两半
        int[] merged = merge(left, right);

        return merged;
    }

    /**
     * 合并两个已经排序完毕的数组(从小到大)
     *
     * @param a 第一个数组
     * @param b 第二个数组
     * @return 合并后的数组
     */
    public static int[] merge(int[] a, int[] b) {
        if (a == null) a = new int[0];
        if (b == null) b = new int[0];

        int[] merged_one = new int[a.length + b.length];

        int mi = 0, ai = 0, bi = 0;

        // 轮流从两个数组中取出较小的值，放入合并后的数组中
        while (ai < a.length && bi < b.length) {
            if (a[ai] <= b[bi]) {
                merged_one[mi++] = a[ai++];
            } else {
                merged_one[mi++] = b[bi++];
            }
        }

        if (ai < a.length) {
            for (int i = ai; i < a.length; i++) {
                merged_one[mi++] = a[i];
            }
        }

        if (bi < b.length) {
            for (int i = bi; i < b.length; i++) {
                merged_one[mi++] = b[i];
            }
        }

        return merged_one;
    }

    public static void main(String[] args) {
        int[] to_sort = {3, 5, 6, 7, 8, 1};
        int[] sorted = merge_sort(to_sort);

        for (int i = 0; i < sorted.length; i++) {
            System.out.println(sorted[i]);
        }
    }
}
