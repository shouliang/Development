

var c = 0;

function printCC(){
	console.log(c)
}

// function plus(){
// 	setTimeout(function(){
// 		c = c + 1
// 	},1000)

// }

//plus()
//printCC()

function plus(callback){
	setTimeout(function(){
		c = c + 1
		callback()
	},1000)
 }

 plus(printCC)