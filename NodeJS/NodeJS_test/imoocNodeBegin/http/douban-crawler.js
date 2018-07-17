var http = require('http')
var url = 'http://movie.douban.com/'

http.get(url, function(res) {
	var html = ''

	res.on('data', function(data) {
		html += data
	})

	res.on('end', function() {
		console.log(html)
	})
}).on('error',function(){
	console.log('获取课程数据出错')
})
