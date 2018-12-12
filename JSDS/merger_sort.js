function mergeSort(arr) {
    mergeSortHelper(arr, 0, arr.length - 1)
}

function mergeSortHelper(arr, low, high) {
    var middle = parseInt((low + high) / 2)
    mergeSortHelper(arr, low, middle)
    mergeSortHelper(arr, middle + 1, high)
    merge(arr, low, middle, high)
}

function merge(arr, low, middle, high) {
    var temparr = []
    var i1 = low, i2 = middle + 1

    for (var i = 0; i >= low && i <= high; i++) {
        if (i1 >= low) {
            temparr.push(arr[i2++])
        } else if (i2 >= high) {
            temparr.push(arr[i1++])
        }
        else if (arr[i1] < arr[i2]) {
            temparr.push(arr[i1++])
        } else {
            temparr.push(arr[i2++])
        }
    }
    return temparr
}

var arr = [4, 5, 6, 1, 2, 3, 8, 7]
mergeSort(arr)
console.log(arr)