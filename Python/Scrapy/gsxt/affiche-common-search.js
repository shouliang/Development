var location_info = 0;
var browser_version;
var hasValid = false;
var isPrompt = false;

/*--为IE8添加.map方法--*/
if (!Array.prototype.map) {
    Array.prototype.map = function (callback, thisArg) {
        var T, A, k;
        if (this == null) {
            throw new TypeError(" this is null or not defined");
        }
        var O = Object(this);
        var len = O.length >>> 0;
        if (typeof callback !== "function") {
            throw new TypeError(callback + " is not a function");
        }
        if (thisArg) {
            T = thisArg;
        }
        A = new Array(len);
        k = 0;
        while (k < len) {
            var kValue, mappedValue;
            if (k in O) {
                kValue = O[k];
                mappedValue = callback.call(T, kValue, k, O);

                A[k] = mappedValue;
            }
            k++;
        }
        return A;
    };
}

window.console = window.console || (function () {
    var c = {}; c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile
        = c.clear = c.exception = c.trace = c.assert = function () { };
    return c;
})();
/*--为IE8添加.map方法  end--*/

window.alert = function (str) {
    var shield = document.createElement("DIV");
    shield.id = "shield";
    shield.style.position = "absolute";
    shield.style.left = "0px";
    shield.style.top = "0px";
    shield.style.width = "100%";
    shield.style.height = document.body.scrollHeight + "px";
    //弹出对话框时的背景颜色 
    shield.style.textAlign = "center";
    shield.style.zIndex = "25";
    //背景透明 IE有效 
    //shield.style.filter = "alpha(opacity=0)"; 
    var alertFram = document.createElement("DIV");
    alertFram.id = "alertFram";
    alertFram.style.position = "fixed";
    alertFram.style.left = "50%";
    alertFram.style.top = "40%";
    alertFram.style.marginLeft = "-225px";
    alertFram.style.marginTop = "-75px";
    alertFram.style.width = "350px";
    alertFram.style.height = "100px";
    alertFram.style.background = "#ff0000";
    alertFram.style.textAlign = "center";
    alertFram.style.lineHeight = "100px";
    alertFram.style.zIndex = "300";
    strHtml = "<ul style=\"list-style:none;margin:0px;padding:0px;width:100%\">\n";
    strHtml += "<li style=\"background:#d1ab62;text-align:left;padding-left:10px;font-size:14px;font-weight:bold;height:40px;line-height:40px;color:#FCFCFC;font-family:Microsoft YaHei;\">提示框" +
        "<div style=\"width:20px;height:20px;background:#fff;border-radius:100%;display:inline-block;color:#000;line-height:20px;text-align:center;position:absolute;right:10px;top:10px;cursor:pointer;\" onclick=\"doOk()\" >X</div></li>\n";
    strHtml += " <li style=\"background:#ffffff;text-align:center;font-size:12px;height:100%;padding:25px;line-height:24px;padding-top:34;border-left:1px solid #F0F0F0;border-right:1px solid #F0F0F0;font-family:Microsoft YaHei;\">" + str + "</li>\n";
    strHtml += " <li style=\"background:#F7F7F7;text-align:center;" +
        "height:50px;line-height:50px; border:1px solid #F0F0F0;color:#FCFCFC;\">" +
        "<input  style=\"background:#d1ab62;text-align:center;width:75px;height:25px;color:#F0F0F0;" +
        "font-family:Microsoft YaHei;display: inline-block;    margin-bottom: 0;" +
        "font-weight: normal;" +
        "text-align: center;" +
        "vertical-align: middle;" +
        "-ms-touch-action: manipulation;" +
        "touch-action: manipulation;" +
        "cursor: pointer;" +
        "background-image: none;" +
        "border: 1px solid transparent;" +
        "white-space: nowrap;" +
        "padding: 6px 12px;" +
        "font-size: 14px;" +
        "line-height: 1;" +
        "border-radius: 4px;" +
        "-webkit-user-select: none;\" type=\"button\" value=\"确定\" onclick=\"doOk()\" /></li>\n";
    strHtml += "</ul>\n";
    alertFram.innerHTML = strHtml;

    var mask = document.createElement('div');
    mask.style.position = 'fixed';
    mask.style.width = '100%';
    mask.style.height = '100%';
    mask.style.left = '0';
    mask.style.top = '0';
    mask.style.backgroundColor = '#000000';
    mask.style.opacity = '0.5';

    /*--兼容IE8透明度--*/
    mask.style.filter = 'alpha(opacity=30)';

    document.body.appendChild(mask);
    document.body.appendChild(alertFram);
    document.body.appendChild(shield);

    this.doOk = function () {
        alertFram.style.display = "none";
        shield.style.display = "none";
        mask.style.display = "none";
        if (typeof (alertindex) !== 'undefined') {
            alertindex = 0;
        }
    }
    alertFram.focus();
    document.body.onselectstart = function () {
        return false;
    };
}

function selectTab(obj) {
    $(".search_tab").each(function () {
        $(this).removeClass("selected");
    });
    $(obj).addClass("selected");
    if ($(obj).attr("class").indexOf("general_tab") > -1)
        $("#selectedSearchTab").val("");
    if ($(obj).attr("class").indexOf("excep_tab") > -1)
        $("#selectedSearchTab").val("excep_tab");
    if ($(obj).attr("class").indexOf("ill_tab") > -1)
        $("#selectedSearchTab").val("ill_tab");
}
var isPress = false;
$(function () {
    var handler = function (captchaObj) {
        captchaObj.onReady(function () {
            $("#wait").hide();
            var keywords = $("#keywords_para").val();
            if (keywords != null && keywords != "") {
                keywords = decodeURI($("#keywords_para").val());
                $("#keyword").val(keywords);
                setTimeout(function () { $("#btn_query").click() }, 100);
            }
        }).onSuccess(function () {
            var result = captchaObj.getValidate();
            if (!result) {
                return alert('请完成验证');
            }
            $("#geetest_challenge").val(result.geetest_challenge);
            $("#geetest_validate").val(result.geetest_validate);
            $("#geetest_seccode").val(result.geetest_seccode);
            if (isPress) {
                $("#search_form").submit();
            } else {
                showDetails(quicksearchurl);
            }
        });
        $("#btn_query").on("click", function () {
            if ($("#keyword").val() == '请输入企业名称、注册号或统一社会信用代码') $("#keyword").val('');

            if (check()) {
                isPress = true;
                captchaObj.verify();
            }
        });
        $("#keyword").on("keypress", function (event) {

            if (event.keyCode === 13) {
                //        	if(isPrompt){
                //        		return false;
                //        	}else{
                //        		captchaObj.verify();
                //        	}
                $("#keyword").blur();
                if ($("#keyword").val() == '请输入企业名称、注册号或统一社会信用代码') {
                    $("#keyword").val('');
                }
                if (check()) {
                    isPress = true;
                    captchaObj.verify();
                }
                return false;
            }
        });
        // 更多前端接口说明请参见：http://docs.geetest.com/install/client/web-front/
    };
    $.ajax({
        url: "/SearchItemCaptcha?t=" + (new Date()).getTime(), // 加随机数防止缓存
        type: "get",
        dataType: "json",
        success: function (data) {

            // 调用 initGeetest 进行初始化
            // 参数1：配置参数
            // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它调用相应的接口
            initGeetest({
                // 以下 4 个配置参数为必须，不能缺少
                gt: data.gt,
                challenge: data.challenge,
                offline: !data.success, // 表示用户后台检测极验服务器是否宕机
                new_captcha: data.new_captcha, // 用于宕机时表示是新验证码的宕机
                //            timeout: '5000',
                product: "bind", // 产品形式，包括：float，popup
                width: "300px"
                // 更多前端配置参数说明请参见：http://docs.geetest.com/install/client/web-front/
            }, handler);
        }
    });
});

$(function () {
    //	$("#btn_query").on("click", function(){
    //        if($("#keyword").val()=='请输入企业名称、注册号或统一社会信用代码') $("#keyword").val('');
    //        if (check()) {
    //        	isPress = true;
    //            $("#pop-captcha-submit").trigger("click");
    //        }
    //    });
    //    $("#keyword").on("keypress", function(event){
    //
    //        if (event.keyCode === 13) {
    //        	if(isPrompt) return false;
    //        	$("#keyword").blur();
    //            if($("#keyword").val()=='请输入企业名称、注册号或统一社会信用代码') $("#keyword").val('');
    //            check();
    //            isPress = true;
    //            return false;
    //        }
    //    });

    var date = new Date();
    var timestamp = date.getMinutes() + date.getSeconds();

    $.ajax({
        type: "get",
        async: false,
        url: "/corp-query-custom-geetest-image.gif?v=" + timestamp,
        dataType: "json",
        success: function (json) {
            eval(json.map(function (item) { return String.fromCharCode(item); }).join(""));
            browser_version = check_browser;
        },
        error: function () {
            //            alert('fail');
        }
    });

})

function stripscript(s) {
    var pattern = new RegExp("[`~!@#$^&*=|{}':;',\\[\\].<>/?~！ @#￥……&*——|{}【】‘；：”“'。，、？]");
    var rs = "";
    for (var i = 0; i < s.length; i++) {
        rs = rs + s.substr(i, 1).replace(pattern, '');
    }
    return rs;
}

//正则验证字母和数字
function checkRate(nubmer) {
    number_2 = nubmer.replace(/[(|)|（|）]/g, "");
    number_2 = number_2.replace(/(^\s*)|(\s*$)/g, "");
    var re = /^[0-9a-zA-Z]*$/g;  //判断字符串是否为数字和字母（）()组合     //判断正整数 /^[1-9]+[0-9]*]*$/
    if (!re.test(number_2)) {
        return false;
    } else {
        return true;
    }
}

//判断输入的关键字是否存在单个字，比如：“北 京”或“北 京 有”不能搜索，但是“沈阳 有 限”或者“有 北京 限”都是能搜索的
function chechSingleWord(value) {
    value = stripscript(value);
    if (value == "") {
        alert("请输入企业名称、统一社会信用代码或注册号！");
        return false;
    }
    var words = value.split(' ');
    for (var i = 0; i < words.length; i++) {
        if (words[i].length > 1) {
            return true;
        }
    }
    alert("请输入更详细的查询条件");
    return false;
}
//正则验证是否全汉字
function load(str) {
    str_2 = str.replace(/[(|)|（|）]/g, "");
    str_2 = str_2.replace(/(^\s*)|(\s*$)/g, "");
    var regex = /^[\u4E00-\u9FA5]+$/;
    if (!regex.test(str_2)) {
        return false;
    } else {
        return true;
    }
}

var data1 = false;

function check() {
    data1 = false;
    //表单提交前验证是否有关键字corp-query-search-test.html
    var xhr = new XMLHttpRequest();
    var val = document.getElementById('keyword');
    var testStr = val.value;

    if (!chechSingleWord(testStr)) {
        return false;
    }

    testStr = testStr.replace(/ /g, '');

    var flag = checkRate(testStr);

    if (flag) {
        //数字和字母组合
        if (val.value.length > 18) {
            alert("您输入的长度超过规定长度，请输入不超过50个汉字或18个数字和字母！");
            return false;
        }
    } else {
        //数字和汉字的组合
        var isChinese = load(testStr);
        if (isChinese) {
            if (testStr.length > 50) {
                alert("您输入的长度超过规定长度，请输入不超过50个汉字或18个数字和字母！");
                return false;
            }
        } else {
            if (testStr.length > 50) {
                alert("您输入的长度超过规定长度，请输入不超过50个字符！");
                return false;
            }
            // alert("只能输入纯汉字或者数字和字母的组合！");
            // return false;
        }
    }

    $.ajax({
        type: "get",
        async: false,
        url: "/corp-query-geetest-validate-input.html?token=" + location_info,
        dataType: "json",
        success: function (json) {
            //           console.log("同学, 你在破解我的代码么?");
            eval(json.map(function (item) { return String.fromCharCode(item); }).join(""));
            var token = document.getElementById('token');
            token.value = location_info;
        },
        error: function () {
            //           alert('fail');
        }
    });
    $.ajax({
        type: "get",
        async: false,  //同步执行，加定时器的前提下依然提前执行了ajax后面的代码，加定时器相当于异步了
        url: "/corp-query-search-test.html",
        data: { searchword: val.value },
        dataType: "json",
        success: function (data) {
            if (data) {
                data1 = true
                //               $("#pop-captcha-submit").trigger("click");
            } else {
                if (val.value.length != 0) {
                    alert("请输入更为详细的查询条件！")
                } else {
                    alert("请输入企业名称、统一社会信用代码或注册号！");
                }

            }
            console.log(data1 + 'neibu')
        }
    });

    console.log(data1)

    return data1;
}

var provinceTonum = {
    '北京': 110000, '天津': 120000, '河北': 130000, '山西': 140000, '内蒙古': 150000, '辽宁': 210000, '吉林': 220000, '黑龙江': 230000, '上海': 310000, '江苏': 320000,
    '浙江': 330000, '安徽': 340000, '福建': 350000, '江西': 360000, '山东': 370000, '广东': 440000, '广西': 450000, '海南': 460000, '河南': 410000, '湖北': 420000,
    '湖南': 430000, '重庆': 500000, '四川': 510000, '贵州': 520000, '云南': 530000, '西藏': 540000, '陕西': 610000, '甘肃': 620000, '青海': 630000, '宁夏': 640000,
    '新疆': 650000
};
var teladdr = {
    "北京": "http://bj.gsxt.gov.cn/subPubSys-tel-110000.html",
    "天津": "http://tj.gsxt.gov.cn/subPubSys-tel-120000.html",
    "河北": "http://he.gsxt.gov.cn/subPubSys-tel-130000.html",
    "山西": "http://sx.gsxt.gov.cn/subPubSys-tel-140000.html",
    "内蒙古": "http://nm.gsxt.gov.cn/subPubSys-tel-150000.html",
    "辽宁": "http://ln.gsxt.gov.cn/subPubSys-tel-210000.html",
    "吉林": "http://jl.gsxt.gov.cn/subPubSys-tel-220000.html",
    "黑龙江": "http://hl.gsxt.gov.cn/subPubSys-tel-230000.html",
    "上海": "http://sh.gsxt.gov.cn/subPubSys-tel-310000.html",
    "江苏": "http://js.gsxt.gov.cn/subPubSys-tel-320000.html",
    "浙江": "http://zj.gsxt.gov.cn/subPubSys-tel-330000.html",
    "安徽": "http://ah.gsxt.gov.cn/subPubSys-tel-340000.html",
    "福建": "http://fj.gsxt.gov.cn/subPubSys-tel-350000.html",
    "江西": "http://jx.gsxt.gov.cn/subPubSys-tel-360000.html",
    "山东": "http://sd.gsxt.gov.cn/subPubSys-tel-370000.html",
    "河南": "http://ha.gsxt.gov.cn/subPubSys-tel-410000.html",
    "湖北": "http://hb.gsxt.gov.cn/subPubSys-tel-420000.html",
    "湖南": "http://hn.gsxt.gov.cn/subPubSys-tel-430000.html",
    "广东": "http://gd.gsxt.gov.cn/subPubSys-tel-440000.html",
    "广西": "http://gx.gsxt.gov.cn/subPubSys-tel-450000.html",
    "海南": "http://hi.gsxt.gov.cn/subPubSys-tel-460000.html",
    "重庆": "http://cq.gsxt.gov.cn/subPubSys-tel-500000.html",
    "四川": "http://sc.gsxt.gov.cn/subPubSys-tel-510000.html",
    "贵州": "http://gz.gsxt.gov.cn/subPubSys-tel-520000.html",
    "云南": "http://yn.gsxt.gov.cn/subPubSys-tel-530000.html",
    "西藏": "http://xz.gsxt.gov.cn/subPubSys-tel-540000.html",
    "陕西": "http://sn.gsxt.gov.cn/subPubSys-tel-610000.html",
    "甘肃": "http://gs.gsxt.gov.cn/subPubSys-tel-620000.html",
    "青海": "http://qh.gsxt.gov.cn/subPubSys-tel-630000.html",
    "宁夏": "http://nx.gsxt.gov.cn/subPubSys-tel-640000.html",
    "新疆": "http://xj.gsxt.gov.cn/subPubSys-tel-650000.html"
}
var devteladdr = {
    "北京": "subPubSys-tel-110000.html",
    "天津": "subPubSys-tel-120000.html",
    "河北": "subPubSys-tel-130000.html",
    "山西": "subPubSys-tel-140000.html",
    "内蒙古": "subPubSys-tel-150000.html",
    "辽宁": "subPubSys-tel-210000.html",
    "吉林": "subPubSys-tel-220000.html",
    "黑龙江": "subPubSys-tel-230000.html",
    "上海": "subPubSys-tel-310000.html",
    "江苏": "subPubSys-tel-320000.html",
    "浙江": "subPubSys-tel-330000.html",
    "安徽": "subPubSys-tel-340000.html",
    "福建": "subPubSys-tel-350000.html",
    "江西": "subPubSys-tel-360000.html",
    "山东": "subPubSys-tel-370000.html",
    "河南": "subPubSys-tel-410000.html",
    "湖北": "subPubSys-tel-420000.html",
    "湖南": "subPubSys-tel-430000.html",
    "广东": "subPubSys-tel-440000.html",
    "广西": "subPubSys-tel-450000.html",
    "海南": "subPubSys-tel-460000.html",
    "重庆": "subPubSys-tel-500000.html",
    "四川": "subPubSys-tel-510000.html",
    "贵州": "subPubSys-tel-520000.html",
    "云南": "subPubSys-tel-530000.html",
    "西藏": "subPubSys-tel-540000.html",
    "陕西": "subPubSys-tel-610000.html",
    "甘肃": "subPubSys-tel-620000.html",
    "青海": "subPubSys-tel-630000.html",
    "宁夏": "subPubSys-tel-640000.html",
    "新疆": "subPubSys-tel-650000.html"
}
//正式上线使用的首页地址
var homepageaddr = {
    "国家企业信用信息公示系统": "http://www.gsxt.gov.cn",
    "北京": "http://bj.gsxt.gov.cn",
    "天津": "http://tj.gsxt.gov.cn",
    "河北": "http://he.gsxt.gov.cn",
    "山西": "http://sx.gsxt.gov.cn",
    "内蒙古": "http://nm.gsxt.gov.cn",
    "辽宁": "http://ln.gsxt.gov.cn",
    "吉林": "http://jl.gsxt.gov.cn",
    "黑龙江": "http://hl.gsxt.gov.cn",
    "上海": "http://sh.gsxt.gov.cn",
    "江苏": "http://js.gsxt.gov.cn",
    "浙江": "http://zj.gsxt.gov.cn",
    "安徽": "http://ah.gsxt.gov.cn",
    "福建": "http://fj.gsxt.gov.cn",
    "江西": "http://jx.gsxt.gov.cn",
    "山东": "http://sd.gsxt.gov.cn",
    "河南": "http://ha.gsxt.gov.cn",
    "湖北": "http://hb.gsxt.gov.cn",
    "湖南": "http://hn.gsxt.gov.cn",
    "广东": "http://gd.gsxt.gov.cn",
    "广西": "http://gx.gsxt.gov.cn",
    "海南": "http://hi.gsxt.gov.cn",
    "重庆": "http://cq.gsxt.gov.cn",
    "四川": "http://sc.gsxt.gov.cn",
    "贵州": "http://gz.gsxt.gov.cn",
    "云南": "http://yn.gsxt.gov.cn",
    "西藏": "http://xz.gsxt.gov.cn",
    "陕西": "http://sn.gsxt.gov.cn",
    "甘肃": "http://gs.gsxt.gov.cn",
    "青海": "http://qh.gsxt.gov.cn",
    "宁夏": "http://nx.gsxt.gov.cn",
    "新疆": "http://xj.gsxt.gov.cn"
}
//开发使用的首页地址
var devhomepageaddr = {
    "国家企业信用信息公示系统": "corp-query-homepage.html",
    "北京": "subPubSys-110000.html",
    "天津": "subPubSys-120000.html",
    "河北": "subPubSys-130000.html",
    "山西": "subPubSys-140000.html",
    "内蒙古": "subPubSys-150000.html",
    "辽宁": "subPubSys-210000.html",
    "吉林": "subPubSys-220000.html",
    "黑龙江": "subPubSys-230000.html",
    "上海": "subPubSys-310000.html",
    "江苏": "subPubSys-320000.html",
    "浙江": "subPubSys-330000.html",
    "安徽": "subPubSys-340000.html",
    "福建": "subPubSys-350000.html",
    "江西": "subPubSys-360000.html",
    "山东": "subPubSys-370000.html",
    "河南": "subPubSys-410000.html",
    "湖北": "subPubSys-420000.html",
    "湖南": "subPubSys-430000.html",
    "广东": "subPubSys-440000.html",
    "广西": "subPubSys-450000.html",
    "海南": "subPubSys-460000.html",
    "重庆": "subPubSys-500000.html",
    "四川": "subPubSys-510000.html",
    "贵州": "subPubSys-520000.html",
    "云南": "subPubSys-530000.html",
    "西藏": "subPubSys-540000.html",
    "陕西": "subPubSys-610000.html",
    "甘肃": "subPubSys-620000.html",
    "青海": "subPubSys-630000.html",
    "宁夏": "subPubSys-640000.html",
    "新疆": "subPubSys-650000.html"
}
// var  areaIdTofkId = {
//     '110000':1,'120000':2,'130000':15,'140000':16,'150000':17,'210000':18,'220000':19,'230000':20,'310000':3,'320000':4,
//     '330000':5,'340000':21,'350000':22,'360000':23,'370000':6,'440000':25,'450000':26,'460000':9,'410000':7,'420000':8,
//     '430000':24,'500000':10,'510000':11,'520000':27,'530000':28,'540000':29,'610000':12,'620000':13,'630000':14,'640000':30,
//     '650000':31
// };
function addLinks() {
    $('#choose_state').hover(function () {
        if (!$('.loadingView').html()) {
            $('.state_box').show();
            return false;
        }
        $(this).addClass('activing');
        $('.loadingView').remove();
        var as = $('.state_box').find('a');
        as.each(function () {
            if ($(this).html().length < 4) {
                $(this).attr('href', homepageaddr[$(this).html()]).attr('target', '_blank');
            }
        });
        if (!$('#choose_state').hasClass('activing')) return;
        $('.state_box').show();
        $("#zj_link").attr("href", homepageaddr[$("#zj_link").html()]);
    }, function () {
        $('.state_box').hide();
        $(this).removeClass('activing');
    });
}

function addTelLinks() {
    $('.other-container a').each(function () {
        $(this).attr('href', teladdr[$($(this).html()).html()]).attr('target', '_blank');
    });
}

/*--兼容IE8的Placeholder--*/
function inputPlaceholder() {
    var input = $('#keyword');
    input.css({ 'color': '#999' }).val('请输入企业名称、注册号或统一社会信用代码');
    input.on('focus', function () {
        if ($(this).val() == '请输入企业名称、注册号或统一社会信用代码') {
            $(this).removeAttr('style').val('');
        }
    });
    input.on('blur', function () {
        if ($(this).val() == '请输入企业名称、注册号或统一社会信用代码' || $(this).val() == '') {
            $(this).css({ 'color': '#999' }).val('请输入企业名称、注册号或统一社会信用代码');
        }
    });
}
/*--兼容IE8的Placeholder end--*/

$(document).ready(function () {
    /*--兼容IE8的Placeholder--*/
    if (navigator.appName == "Microsoft Internet Explorer" && (navigator.appVersion.match(/8./i) == "8." || navigator.appVersion.match(/9./i) == "9.")) {
        inputPlaceholder();
    }

    /*--搜索结果页企业状态颜色赋值--*/
    $('.wrap-corpStatus span').each(function () {
        var status = $(this).html();
        if (status.indexOf('吊销') > -1) {
            $(this).css('background-color', '#f00');
        } else if (status.indexOf('注销') > -1) {
            $(this).css('background-color', '#999');
        } else {
            $(this).css('background-color', '#4395e1');
        }
    });

    /*--详情页企业状态颜色赋值--*/
    var status_span = $('.companyStatus');
    var status = status_span.html();
    if (status && status.indexOf('吊销') > -1) {
        status_span.css({ 'background-color': '#f00', 'display': 'inline-block' });
    } else if (status && status.indexOf('注销') > -1) {
        status_span.css({ 'background-color': '#999', 'display': 'inline-block' });
    } else {
        status_span.css({ 'background-color': '#4395e1', 'display': 'inline-block' });
    }

    addLinks();
    addTelLinks();
    /*--兼容IE8的Placeholder end--*/

    // var areaId = $('#search_logo').attr('class').split('_')[2] || 100000;
    // var fkId = areaIdTofkId[areaId] || 0;
    // $('#back_home').attr('href','/corp-query-homepage.html?fkId='+fkId);
    // $('#to_info').attr('href','/affiche-query-info-paperall.html?FKID='+fkId+'&areaId='+areaId);
    //var s = window.location.protocol+"//"+window.location.host+window.location.pathname
    /*$.ajax({
        type:'post',
        url: "/error.html",
        dataType:'json',
        success:function(data){
    	      if(data.code==404||data.code==400||data.code==500||data.code==502||data.code==504){
    	    	  alert("您发送的请求出现异常");   	    	  
    	      }
    	      
            $('.loadingView').remove();
            var as = $('.state_box').find('a');
            as.each(function(){
                if($(this).html().length<4){
                    $(this).off('click').on('click',function(){
                        window.open(data[provinceTonum[$(this).html()]]);
                    });
                }
            });
            if(!$('#choose_state').hasClass('activing')) return;
            $('.state_box').show();
        }
    });*/
});

function imgerror(t) {
    $(t).attr('src', '/images/trademark.png');
}