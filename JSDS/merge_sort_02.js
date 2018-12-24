
function mergeSort(alist) {
    if (!alist) return [];
    if (alist.length === 1) return alist;
    var mid = Math.floor(alist.length / 2);
    var left = alist.slice(0, mid);
    var right = alist.slice(mid);
    left = mergeSort(left);
    right = mergeSort(right);
    return merge(left, right);
}


function merge(left, right) {
    var i = 0, j = 0;
    var merged = [];

    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            merged.push(left[i++]);
        } else {
            merged.push(right[j++]);
        }
    }

    while (i < left.length) {
        merged.push(left[i++]);
    }

    while (j < right.length) {
        merged.push(right[j++]);
    }

    return merged;
}


alist = [3, 5, 6, 7, 8, 1];
sorted = mergeSort(alist);
console.log(sorted);