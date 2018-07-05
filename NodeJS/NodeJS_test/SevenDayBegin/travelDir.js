function travel (dir, callback) {
	var fs = require('fs')
	var path = require('path')
	fs.readdirSync(dir).forEach(function (file) {
		var pathname = path.join(dir, file)

		if (fs.statSync(pathname).isDirectory()) {
			travel(pathname, callback)
		} else {
			callback(pathname)
		}
	})
}

travel('GitHub',function(pathname) {
	console.log(pathname)
})