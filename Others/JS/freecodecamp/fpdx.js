/**
 * Created by 朱守亮 on 2017/6/19.
 */

let girls = ['M87-UI-果子-苏本', 'M86-ip-栗子-鲁本', 'M89-金融-维c小妞-豫本', 'M85-广告-VV-湘本',
    'M92-采购-凡薏米-皖本','M88-环保-bobo头-皖硕','M90-项目管理-莫语-鄂本'];
let boys = ['G84-ENG-木muji-鲁硕', 'G88-科研-牧野-豫本', 'G87-医药-沉沙-皖本', 'G88-设计-blue-鲁硕',
    'G86-研发-千年-桂博'];

let min = Math.min(girls.length, boys.length);
let match = [];

for (let i = 0; i < min; i++) {
    let girlChoosedByGod = randomPickArray(girls, 1);
    let boyChoosedByGod = randomPickArray(boys, 1);
    match.push({
        girl: girlChoosedByGod,
        boy: boyChoosedByGod
    })
}

console.log(match);

/**
 * 从给定的数组中随机抽取给定数量的元素，返回一个新数组
 * @param arr 原数组
 * @param count 随机抽取的数量
 * @returns {Array} 新数组
 */
function randomPickArray(arr, count) {
    let resultArr = [];

    if (arr.length <= count) {
        count = arr.length;
    }

    // 随机选取过程
    for (let i = count - 1; i >= 0; i--) {
        let index = Math.floor(Math.random() * arr.length); // 从原数组中随机取一个元素出来
        resultArr.push(arr[index]);                         // 压入结果数组
        arr.splice(index, 1);                               // 将该元素从原数组中删除
    }

    return resultArr;
}