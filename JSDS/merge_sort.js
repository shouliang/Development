function mergeSort(alist) {
    mergeSortHelper(alist, 0, alist.length - 1);
}

function mergeSortHelper(alist, low, high) {
    if (low < high) {
        var mid = Math.floor((low + high) / 2);
        mergeSortHelper(alist, low, mid);
        mergeSortHelper(alist, mid + 1, high);
        merge(alist, low, mid, high);
    }
}

function merge(alist, low, mid, high) {
    var i = low, j = mid + 1;
    var tmp = [];
    while (i <= mid && j <= high) {
        if (alist[i] <= alist[j]) {
            tmp.push(alist[i]);
            i = i + 1;
        } else {
            tmp.push(alist[j]);
            j = j + 1;
        }
    }

    while (i <= mid) {
        tmp.push(alist[i]);
        i = i + 1;
    }
    while (j <= high) {
        tmp.push(alist[j]);
        j = j + 1;
    }

    for(var k=0,i=low; i<=high;i++,k++) {
        alist[i] = tmp[k];
    }

}


alist = [3, 5, 6, 7, 8, 1];
mergeSort(alist);
console.log(alist);