function forInObj(objName,obj) {
    for (let prop in obj) {
        console.log(`${objName}.${prop} = ${obj[prop]}`);
    }
}

//forInObj('global',global);

// if(global === global.global) {
// 	console.log('global === global.global');
// }

//console.log('typeof exports', exports);
//console.log('typeof module', module);


//forInObj('module',module);

console.log(void(0));

