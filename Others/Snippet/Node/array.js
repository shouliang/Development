// 单个选择元素时，将其转换成数组
var knowledges = req.query.knowledges;
if (!_.isArray(knowledges)) {
	knowledges = [req.query.knowledges];
}


// 按onTopWapDetail排序 优先layer从小到大 而后priority从大到小
topHotelEntities.sort(function (a, b) {
        return
         (parseInt(a.onTopWapDetail.layer) - parseInt(b.onTopWapDetail.layer))
           ||
         (parseInt(b.onTopWapDetail.priority) - parseInt(a.onTopWapDetail.priority))
        ;
});


3.Array.prototype.map()  // 返回一个新的数组
 The map() method creates a new array with the results of calling a provided function on every element in this array.
 var numbers = [1, 5, 10, 15];
 var roots = numbers.map(function(x) {
   return x * 2;
});
// roots is now [2, 10, 20, 30]
// numbers is still [1, 5, 10, 15]

// 遍历对象的values ，对象的keys可以通过Object.keys(obj)直接来遍历
let countries =
{
"Argentina":1,
"Canada":2,
"Egypt":1,
};
let vals = Object.keys(countries).map(function(key) {
    return countries[key];
});

// just test push too

4.Array.splice
let myFish = ['angel', 'clown', 'drum', 'mandarin', 'sturgeon'];
let removed = myFish.splice(3, 1);

// removed is ["mandarin"]
// myFish is ["angel", "clown", "drum", "sturgeon"],
// 容易犯的错误是让: myFish =  myFish.splice(3, 1);
