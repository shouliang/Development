var EventEmitter = require('events').EventEmitter

var life = new EventEmitter()

life.setMaxListeners(11)

// addEventListener
function water(who){
	console.log('给' + who + '倒水')
}

life.on('求安慰',water)

life.on('求安慰',function(who) {
	console.log('给' + who + '揉肩')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '洗衣')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '做饭')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '拖地')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '...6')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '...7')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '...8')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '...9')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '...10')
})

life.on('求安慰',function(who) {
	console.log('给' + who + '哈哈哈哈')
})

life.on('求溺爱',function(who) {
	console.log('给' + who + '买衣服')
})

life.on('求溺爱',function(who) {
	console.log('给' + who + '买鞋子')
})

//移除事件监听 需要命名函数
life.removeListener('求安慰',water)
life.removeAllListeners('求安慰')
//life.removeAllListeners() //无参数删除全部，包括“求安慰”和“求溺爱”

// 事件是否被监听过
var hasConforListener = life.emit('求安慰','汉子')
var hasLovedListener = life.emit('求溺爱','妹纸')
var hasPlayedListener = life.emit('求玩坏','汉子和妹纸')

//当前事件的个数
console.log(life.listeners('求安慰').length)
console.log(EventEmitter.listenerCount(life,'求溺爱'))

console.log(hasConforListener)
console.log(hasLovedListener)
console.log(hasPlayedListener)










