/**
 * Created by 朱守亮 on 2017/3/24.
 */
/*
 let gen = function * () {
 return 1;
 };

 let a = gen();
 console.log(a.next());
 console.log(a.next());
 */

/*
 let gen = function * () {
 yield 2;
 return 1;
 };
 let a = gen();
 console.log(a.next());
 console.log(a.next());
 console.log(a.next());
 */

let gen = function *() {
    let content = 'initial content';
    return new Promise((resolve, reject) => {
        setTimeout(function () {
            content = 'changed content';
            resolve(content);
        }, 1000);
    });
};

let myCo = (fn) => {
    let state = null;
    let g = fn();
    return (function next(data) {
        state = g.next(data);
        if (state.done) {
            return state.value;
        } else {
            return state.value.then(val => next(val));
        }
    })();
};

let a = myCo(gen);
a.then(val => {
    console.log(val)
});
