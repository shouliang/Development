var globalVariable = 'This is global Variable'

function globalFunction(){
	var localVariable = 'This is local Variable'

	console.log("Visit global/local variable")
	console.log(globalVariable)
	console.log(localVariable)

	function localFunction(){
		var innerLocalVariable = 'This is inner Local variable'
		console.log("Visit global/local/innerLocal variable")
		console.log(globalVariable)
		console.log(localVariable)
		console.log(innerLocalVariable)
	}

	localFunction()
}

globalFunction()