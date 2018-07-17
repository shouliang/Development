var student = require('./student')

var teacher = require('./teacher')

//teacher.add('ZhangSan')

function add(teacherName,students){
	teacher.add(teacherName)

	students.forEach(function(item,index){
		student.add(item)
	})
}

exports.add = add

//module.exports = add