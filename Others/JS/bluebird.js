/**
 * Created by shouliang on 2016/9/22.
 */
var Promise = require("bluebird");

function timerPromisefy (delay) {
    return new Promise( function ( resolve, reject ) {
        setTimeout( function () {
            console.log( 'process was done ' + delay );
            ( delay < 64 )? resolve(delay): reject('reject');
        }, delay);
    });
}

/*
Promise.all([
    timerPromisefy( 1 ),
    timerPromisefy( 4 ),
    timerPromisefy( 8 ),
    timerPromisefy( 16 )
]).then( function (value) {
    console.log(value);     // => [1 , 4 , 8 , 16]
}).catch ( function (error) {
    console.error(error); // => no error return
});

Promise.all([
    timerPromisefy( 32 ),
    timerPromisefy( 64 ),
    timerPromisefy( 128 ),
    timerPromisefy( 256 )
]).then( function (value) {
    console.log(value);     // => no result return
}).catch ( function (error) {
    console.error(error); // => reject
});*/


/*

function timerPromisefy (delay) {
    return new Promise( function ( resolve, reject ) {
        setTimeout( function () {
            console.log( 'process was done ' + delay );
            ( delay < 64 )? resolve(delay): reject('reject');
        }, delay);
    });
}

var join = Promise.join;
join(timerPromisefy(1), timerPromisefy(4), timerPromisefy(8),
    function(agrv1, agrv2, agrv3) {
        // agrv1 = 1, agrv2 = 4, agrv3 = 8
        return timerPromisefy( agrv1*1 + agrv2*2 + agrv3*3);
    }).then( function( value ){
    console.log( value ); // => 33
}).catch( function( error ){
    console.error( error );
});*/

// var propsFunc = {
//     timeFunc1: timerPromisefy(1),
//     timeFunc32: timerPromisefy(32),
//     timeFunc64: timerPromisefy(64),
//     timeFunc128: timerPromisefy(128)
// }
// Promise.props( propsFunc ).then(function(result) {
//     console.log(result.timeFunc1, result.timeFunc128, result.timeFunc64);
// });


function timerPromisefy (delay) {
    return new Promise( function ( resolve, reject ) {
        setTimeout( function () {
            console.log( 'process was done ' + delay );
            ( delay > 64 )? resolve(delay): reject('reject');
        }, delay);
    });
}

/*Promise.race([
    timerPromisefy( 128 ),
    timerPromisefy( 1024 ),
    timerPromisefy( 512 ),
    timerPromisefy( 256 )
]).then( function (value) {
    console.log(value);     // => 128
}).catch( function( error ){
    console.error( error ); // no error return
});*/


Promise.race([
    timerPromisefy( 1 ),
    timerPromisefy( 32 ),
    timerPromisefy( 64 ),
    timerPromisefy( 128 )
]).then( function (value) {
    console.log(value);     // no result return
}).catch( function( error ) {
    console.error(error); // => reject
})
