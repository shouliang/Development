/**
 * Created by zhushouliang on 16/7/19.
 */
module.exports = {
    sum:function() {
        var result = 0;
        for(var i in arguments) {
            console.log("i is: " + i);
            if(!isNaN(arguments[i])){
                result += parseInt(arguments[i]);
            }
        }

        return result;
    }

};