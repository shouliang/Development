function selectionSort(array) {
    for (var i = 0; i < array.length - 1; i++) {
        var minIndex = i
        for (var j = i + 1; j < array.length; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j
            }
        }

        if (minIndex != i) {
            swap(array, minIndex, i)
        }
    }
}

function swap(array, i, j) {
    var temp = array[i]
    array[i] = array[j]
    array[j] = temp
}

array = [4, 5, 6, 1, 2, 3]
selectionSort(array)
console.log(array)