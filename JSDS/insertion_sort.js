function insertSort(array) {
    for (var i = 1; i < array.length; i++) {
        var insertToItem = array[i]

        var j = i - 1
        while (j >= 0 && array[j] > insertToItem) {
            array[j + 1] = array[j]
            j = j - 1
        }

        array[j + 1] = insertToItem

    }
}


nums = [4, 5, 6, 1, 2, 3]
insertSort(nums)
console.log(nums)