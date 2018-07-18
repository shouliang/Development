// var http = require('http')
// http.createServer(function (request, response) {
// 	var body = [] 

// 	console.log(request.method)
// 	console.log(request.headers)

// 	request.on('data', function (chunk) {
// 		body.push(chunk)
// 	})

// 	request.on('end', function() {
// 		body = Buffer.concat(body)
// 		console.log(body.toString())
// 	})
// }).listen(3000)


var http = require('http')
http.get('http://www.baidu.com/',function(response) {
	var body = []

	console.log(response.statusCode)
	console.log(response.headers)

	response.on('data', function(chunk) {
		body.push(chunk)
	})

	response.on('end', function() {
		body = Buffer.concat(body)
		console.log(body.toString())
	})
})