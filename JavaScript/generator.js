/**
 * Created by 朱守亮 on 2017/3/24.
 */
/*
 function* helloWorldGenerator() {
 yield 'hello';
 yield 'world';
 return 'ending';
 }

 let hw = helloWorldGenerator();
 console.log(hw);
 console.log(hw.next());
 console.log(hw.next());
 console.log(hw.next());
 console.log(hw.next());*/

function* foo(x) {
    let y = 2 * (yield (x + 1));
    let z = yield (y / 3);
    return (x + y + z);
}

/*let a = foo(5);
console.log(a.next());
console.log(a.next());
console.log(a.next());*/

let b= foo(5);
console.log(b.next());
console.log(b.next(12));
console.log(b.next(13));

