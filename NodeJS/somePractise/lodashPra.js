var _ = require("lodash");

var users = [
    {'user': 'barney', 'age': 36},
    {'user': 'fred', 'age': 40},
    {'user': 'pebbles', 'age': 18}
];

var userNames = _.map(users, "user");
console.log(userNames);

//get the youngest user.
var youngest = _.chain(users)
    .min(function (user) {
        return user.age;
    })
    .value();
console.log(youngest);

var youngest2 = _.chain(users)
    .sortBy("age")
    .map(function (user) {
        console.log("map", user);
        return user;
    })
    .first()
    .value();
console.log(youngest2);

//get oldest user
var oldest = _.chain(users)
    .max(function (user) {
        return user.age;
    })
    .value();

console.log(oldest);

//get all user names

var names = _.chain(users)
    .map(function (user) {
        return user.user;
    })
    .join(" , ")
    .value();
console.log(names);

//map to user obj.
var userObj = _.chain(users)
    .map(function (user) {
        return [user.user, user.age];
    })
    .zipObject()
    .value();
console.log(userObj);

console.log("<<<<<<<<<<<<<<<<<<<<<<<<<<<<");

var numbers = [1, 2, 3, 4, 5];
var sumOfEvenSquares = _.chain(numbers)
    .filter(function (n) {
        return n % 2 === 0;
    })
    .map(function (n) {
        return n * n;
    })
    .sum()
    .value();
console.log(sumOfEvenSquares);
//sumOfEvenSquares: 20

var sumOfEvenSquares = _(numbers)
    .filter(function (n) {
        return n % 2 === 0;
    })
    .map(function (n) {
        return n * n;
    })
    .sum()
console.log(sumOfEvenSquares);

console.log(_.random(5));
