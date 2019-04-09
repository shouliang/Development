/**
 * Created by 朱守亮 on 2017/6/20.
 */
function telephoneCheck(str) {
    var reg = /^[1]{0,1}\s{0,1}(\(){0,1}\d{3}(\){0,1})[-\s]{0,1}\d{3}[-\s]{0,1}\d{4}$/;


    var match = str.match(reg);
    console.log(str.match(reg));

    if (match) {
        if (( match[1] === '(' && match[2] === ')' ) || (!match[1] && !match[2])) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}


console.log(
    //telephoneCheck("555-555-5555")
    //telephoneCheck("27576227382")
    telephoneCheck("1 555)555-5555")
);
