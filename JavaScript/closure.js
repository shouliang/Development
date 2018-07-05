/**
 * Created by 朱守亮 on 2017/6/29.
 */
function init() {
    let name = 'Mozilla';

    function displayName() {
        console.log(name);
    }

    displayName();
}

init();

// ---------------------

function makeFunc() {
    let name = 'Mozilla 1';

    function displayName() {
        console.log(name);
    }

    return displayName;
}

let myFunc = makeFunc();
myFunc();

// ---------------------

function makeAdder(x) {
    return function (y) {
        return x + y;
    }
}

let add5 = makeAdder(5);
let add10 = makeAdder(10);

console.log(add5(2));
console.log(add10(2));
