function route(handle,pathname,response){
	console.log('About to route a request for ' + pathname);
	if (  typeof  handle[pathname]  === 'function'){
		return handle[pathname](response);
	}else{
		console.log("No request handle found for  " + pathname);
		response.writeHead(404,{  "Content-type":"text/plain"  });
		response.write("404 not found");
		response.end();
		return "404 not found";
	}
}

exports.route = route ;