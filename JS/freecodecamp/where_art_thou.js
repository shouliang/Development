/**
 * Created by 朱守亮 on 2017/6/16.
 */
function where1(collection, source) {

    var arr = [];
    // What's in a name?
    var sourceKeys = Object.keys(source);

    collection.forEach(function (obj) {
        var objKeys = Object.keys(obj);

        var flag = true;
        for (var i = 0; i < sourceKeys.length; i++) {
            if (objKeys.includes(sourceKeys[i]) && (obj[sourceKeys[i]] === source[sourceKeys[i]])) {
                flag = true;
            } else {
                flag = false;
            }
        }

        if (flag) {
            arr.push(obj);
        }

    });

    return arr;
}

function where2(collection, source) {
    var arr = [];
    // What's in a name?
    var sourceKeys = Object.keys(source);

    collection.forEach(function (obj) {
        var objKeys = Object.keys(obj);

        var flag = false;
        for (var i = 0; i < sourceKeys.length; i++) {
            if (objKeys.includes(sourceKeys[i]) && (obj[sourceKeys[i]] === source[sourceKeys[i]])) {
                flag = true;
            } else {
                flag = false;
            }
        }
        if (flag) {
            arr.push(obj);
        }

    });

    return arr;


}

function where3(collection, source) {
    var arr = [];
    var sourceKeys = Object.keys(source);

    collection.forEach(function (obj) {
        var objKeys = Object.keys(obj);

        var flag = true;
        sourceKeys.forEach(function (key) {
            if (!objKeys.includes(key) || obj[key] !== source[key]) {
                flag = false;
            }
        });

        if (flag) {
            arr.push(obj);
        }

    });

    return arr;
}

function where4(collection, source) {
    var sourceKeys = Object.keys(source);

    var arr = collection.filter(function (obj) {
        var objKeys = Object.keys(obj);

        var flag = true;
        sourceKeys.forEach(function (key) {
            if (!objKeys.includes(key) || obj[key] !== source[key]) {
                flag = false;
            }
        });

        return flag;

    });

    return arr;
}

function where5(collection, source) {
    var sourceKeys = Object.keys(source);

    var arr = collection.filter(function (obj) {
        var objKeys = Object.keys(obj);

         var flag = true;
        for (var i = 0; i < sourceKeys.length; i++) {
            if (!objKeys.includes(sourceKeys[i]) || (obj[sourceKeys[i]] !== source[sourceKeys[i]])) {
                flag = false;
                break;
            }
        }

        return flag;
    });

    return arr;
}

console.log(
    where5(
        [
            {first: "Romeo", last: "Montague"},
            {first: "Mercutio", last: null},
            {first: "Tybalt", last: "Capulet"}
        ],
        {last: "Capulet"}
    )
);

console.log(
    where5([{"a": 1, "b": 2}, {"a": 1}, {"a": 1, "b": 2, "c": 2}], {"a": 1, "b": 2})
);