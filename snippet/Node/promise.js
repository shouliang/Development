1.  // 将bluebird赋值给mongoose.Promise，使Promise化
1.1 // markModified也可以作用于子项上
1.2 // 通过数组的concat方法添加新项
var mongoose = require('mongoose');
var Promise = require('bluebird');
mongoose.Promise = Promise;

 User.findOne({name: name, mobile: mobile, userType: 'student'}).exec() // create promise
        .then(function (user) {
            parent = user;
            parent.profile.children = (user.profile.children || []).concat( // 通过数组的concat方法添加新项
                {
                    _id: user._id,
                    username: user.username,
                    name: user.name
                });
            parent.markModified('profile.children'); // markModified也可以作用于子项上
            return parent.save(); // return promise  必须返回promise才可以继续then
        })
        .then(function (parent) {
            res.json({result: 1, data: parent});
        })
        .catch(function (err) {
            res.json({result: 0, data: err})
        })

2. //Promise执行多个任务，并返回Promise
function getParentsByChildrenIds(Ids) {
	var promiseFuns = [];
	_.each(Ids, function (item) {
	    promiseFuns.push(
	        User.find({'profile.children._id': mongoose.Types.ObjectId(item)})
	            .exec()
	    );
	})

   return Promise.all(promiseFuns);
}

3.  // 因为函数getParentsByChildrenIds返回的是Promise，所以在调用时可以使用then方法
3.1 //   _.flatten 可以将数组降一级( 例如本例将二维数组降为一级数组)
 getParentsByChildrenIds(noti_Options.children)
        .then(function (user) {
            var users = _.flatten(user);
            var parents = _.map(users, "_id");

            if (parents && parents.length > 0) {
                var notification = {
                    title: noti_Options.notiTitle,
                    content: noti_Options.taskTitle + '.请进入作业列表查看',
                    from: {
                        name: noti_Options.teacherName,
                        userId: noti_Options.teacherUserId
                    },
                    to: parents
                };
                app.get('notificationEvent').emit('notification_multiple', notification);
            }
        });

