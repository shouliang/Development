1.// 修改Model里面没有定义字段的时候，需要加上
var rightRate = taskExe.statistics.mark ? Math.round(rightNum / taskExe.statistics.mark * 100) : 0;
taskExe.statistics.time = Date.now();
taskExe.statistics.right = rightNum;
taskExe.statistics.rightRate = rightRate;
taskExe.markModified('statistics'); // 修改Model里面没有定义字段的时候，需要加上
taskExe.save(function (err) {
    if (err) return callback(err);
})

2.// populate 也可以关联子项
Task.find(query)
    .sort({created: -1})
    .skip((page - 1) * pageItem)
    .limit(pageItem)
    .populate('executed')
    .populate('content.book', "_id name grade subject session cover", 'TeacherBook')
    .exec(function (err, results) {
        callback(err, results);
    });

3.// lodash交集的方法intersection
  // 搜索条件为主键时需要通过mongoose.Types.ObjectId转换成ObjectId类型
var TaskExeSchema=new Schema({
    created:{
        type:Date,
        default:Date.now
    },
    task:{
        type:Schema.ObjectId,
        ref: 'Task',
        required: true
    },
    user:{
        type:Schema.ObjectId,
        ref:'User',
        required: true
    }
}

var users = [];
var taskExes = results.getTaskExes;
_.each(taskExes, function (item) {
    users.push(mongoose.Types.ObjectId(item.user));
})
conditions.user = {$in: users};
if (classId) {
    users = _.intersection(_.toArray(results.getMembers.toString().split(',')), _.toArray(users.toString().split(',')));  // lodash求交集
}
conditions.user = {$in: users};
  MyAnswer.find(conditions)
        .populate('user', '_id name username')
        .populate('topic', '_id stem image')
        .exec(function (err, myanswers) {
            if (err) callback(err);
            callback(null, myanswers);
        })

4.//查询结果为mongoose中Model类型的对象，如果需要添加新属性，则需要先通过toObject()方法转换成普通的对象
var wrongAnswerUser = wrongMyAnswers[i].user.toObject();  // toObject()方法转换成普通对象
var taskexe = _.filter(taskexes, {user: wrongMyAnswers[i].user._id});
if (taskexe && taskexe[0]) {
    wrongAnswerUser.taskExe = taskexe[0]._id;  //添加新属性
}

5.// 通过_.extend方法也可以将mongoose中Model类型转换成普通对象
var newNoti = _.extend({}, noti);
newNoti.to = item;
notification_single(newNoti, callback);


6.// populate 嵌套查询 myanswer ref topic  topic ref knowledge

  // 3.8版本的mongoose的populate,不能深度关联获取
MyAnswer.find(conditions)
        .skip((page - 1) * ItemInPage)
        .limit(ItemInPage)
        .sort('created')
        .populate('user', 'name username')
        .populate('topic', '_id subject stem type answer analysis level from image knowledge')
        .exec(function (err, docs) {
            var options = {
                path: 'topic.knowledge',
                select:'_id title level',
                model: 'Knowledge'  //  mongoose.model('Knowledge', KnowledgeSchema);
            };

            if (err) return callback(err);
            MyAnswer.populate(docs, options, function (err, myanswers) {
                if(err) return callback(err);
                callback(null,myanswers);
            });
        });

7.//4.5版本的mongoose支持deep-populate,也就是深度关联获取 可以嵌套populate获取关联对象的子关联对象
MyAnswer.find(conditions)
        .skip((page - 1) * ItemInPage)
        .limit(ItemInPage)
        .sort('created')
        .populate('user', 'name username')
        .populate('topic', '_id subject stem type answer analysis level from image')
        .pupulate({
        	path:'topic',
            populate:{
            	path:'knowledge',
            	select:'_id title level'
            }
        })
        .exec(function (err, docs) {
            if (err) return callback(err);
            callback(null,myanswers);
        });

8.// $where 查询中可以使用javascript中的函数 注意this
Notification.find({"$where" :  "this.to.indexOf('"+ req.user._id.toString()+"') > 0" } )

9.// 视model里面定义的数据类型是否是ObjectId类型来决定是否需要通过mongoose.Types.ObjectId来转换
  // accepters是数组，但是可以通过字段直接等于查询条件来过滤
	var user = '57b9523ac1106b4c22881a74' ;
	if (user) {
	    taskConditions.accepters = user;
	    myAnswerConditions.user = mongoose.Types.ObjectId(user);
	}

10.//mongoose数组查询
例如：
user : {
	profile:{
		children:[
		   "57abf61506e356e41a86e99d",
		   "67abf61506e356e41a86e99e"
		]
	}
}
可通过：User.find({'profile.children': mongoose.Types.ObjectId(item)}).exec() 来查询

如果children里面是一个数组对象：
user : {
	profile:{
		children:[
		{
          _id: "57abf61506e356e41a86e99d",
          username:'zhangsan',
          name:'张三'
		},
		{
          _id: "67abf61506e356e41a86e99e",
          username:'lisi',
          name:'李四'
		}
	}
}
可通过: User.find({'profile.children._id': mongoose.Types.ObjectId(item)}).exec() 来查询

10.mongoose查询时，数组多对多也可以匹配查询
可通过: User.find({'profile.children._id': {$in:[id1,id2]} }).exec() 来查询

//1. Mongoose query nested documents greater or less a certain date
Post.find({ "comments.created_at": { $gt: date1, $lt: date2 }}, function (err, docs) {

});

 // Example for Node.js
var _ = require('lodash');
var queryDate = {};
if (req.query.beginDate && _.isDate(new Date(req.query.beginDate))) {
    queryDate["$gte"] =  moment(new Date(req.query.beginDate));
    conditions.created = queryDate;
}

if (req.query.endDate && _.isDate(new Date(req.query.endDate))) {
    queryDate["$lt"] =  moment(new Date(req.query.endDate)).add(1, 'd');
    conditions.created = queryDate;
}


//2. Combine two OR-queries with AND in Mongoose

//It's probably easiest to create your query object directly as:
11.
Test.find({
  $and: [
      { $or: [{a: 1}, {b: 1}] },
      { $or: [{c: 1}, {d: 1}] }
  ]
}, function (err, results) {

}

//But you can also use the Query#and helper that's available in recent 3.x Mongoose releases:
Test.find()
  .and([
      { $or: [{a: 1}, {b: 1}] },
      { $or: [{c: 1}, {d: 1}] }
  ])
  .exec(function (err, results) {

  });

12.是否存在该字段 可通过 exists('字段', true)来查询
  User.find({isvote: 1})
        .exists('checkInAt', true)
        .count(function (err, count) {
            if (err) {
                data.code = 0;
                data.msg = 'query error';
            }
            data.count = count;
            res.jsonp(data);
        })
