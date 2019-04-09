/**
 * Created by 朱守亮 on 2017/6/21.
 */
function truncate(str, num) {
    // Clear out that junk in your trunk
    if(str.length > num) {
        if(num > 3) {
            str = str.substr(0,num - 3) + '...';
        } else {
            str = str.substr(0,num) + '...';
        }

    }
    return str;
}

let tr = truncate("Absolutely Longer", 2);
console.log(tr);