var http = require('http')
var cheerio = require('cheerio')
var url = 'http://movie.douban.com/'

function filterMovie(html){
	var $ = cheerio.load(html)
	var movies = $('.billboard-bd table tr')
    console.log("本周电影口碑榜TOP10：\n")
	movies.each(function(item){
		var movie = $(this)
		var order = movie.children('td.order').text()
		var movieName = movie.children('td.title').find('a').text()
		console.log(order + ": " + movieName +'\n')
	})
}

http.get(url, function(res) {
	var html = ''

	res.on('data', function(data) {
		html += data
	})

	res.on('end', function() {
		filterMovie(html)
	})
}).on('error',function(){
	console.log('获取课程数据出错')
})
