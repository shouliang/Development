/**
 * Created by 朱守亮 on 2017/3/24.
 */
let it = makeIterator(['a','b']);
console.log(it.next());
console.log(it.next());
console.log(it.next());

function makeIterator(array) {
    let nextIndex = 0;
    return {
        next: function () {
            return nextIndex < array.length ?
                {value: array[nextIndex++]} :
                {done: true}
        }
    }
}

// just test git pull
