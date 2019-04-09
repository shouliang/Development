/**
 * Created by 朱守亮 on 2017/6/21.
 */
function myReplace(str, before, after) {
    var fb = before.substr(0, 1);
    if (/[A-Z]/.test(fb)) {
        return str.replace(new RegExp(before, 'g'), after.substr(0, 1).toUpperCase() + after.substr(1, after.length -1));
    } else {
        return str.replace(new RegExp(before, 'g'), after);
    }

}
console.log(
    myReplace("He is Sleeping on the couch", "Sleeping", "sitting")
);