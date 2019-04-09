function bubbleSort(array) {
    var n = array.length
    for (var i = 0; i < n - 1; i++) {         // Do n - 1 bubbles, when the only one, it just ordered
        for (var j = 0; j < n - i - 1; j++) { // Start each bubble
            if (array[j] > array[j + 1]) {    // Exchange if needed
                swap(array, j, j + 1)
            }
        }
    }
}

function swap(array, i, j) {
    var temp = array[i]
    array[i] = array[j]
    array[j] = temp
}

array = [4, 5, 6, 1, 2, 3, 7]
bubbleSort(array)
console.log(array)