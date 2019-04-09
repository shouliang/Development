1. //lodash求交集
conditions.user = {$in: users};
if (classId) {
    users = _.intersection(_.toArray(results.getMembers.toString().split(',')), _.toArray(users.toString().split(',')));
}
conditions.user = {$in: users};
  MyAnswer.find(conditions)
        .populate('user', '_id name username')
        .populate('topic', '_id stem image')
        .exec(function (err, myanswers) {
            if (err) callback(err);
            callback(null, myanswers);
        })

2.findIndex 从0开始，因为数组下标是从0开始
_.findIndex(parent.profile.children || [], {username:user.username}) >=0

3.通过条件查找到索引，再通过slice删除，而后重新组装成删除后的新数组
   var checkers = task.checkers || [];
   var index = _.findIndex(checkers, {userId: mongoose.Types.ObjectId(userId)});
   if (index >= 0) {
        task.checkers = checkers.slice(0, index).concat(checkers.slice(index + 1, checkers.length + 1));
    }

// mongoose查询到的为model对象，为其赋值可以通过 lodash的extend方法
4.subject = _.extend(subject, {versions: newVersions});

5.cloneDeep深度复制对象，新对象包含老对象的所有属性，且完全不同于老对象
var options_top = _.cloneDeep(options);

6.uniqBy可通过某字段来去重数组里面的object元素
 entities: _.uniqBy((topHotelEntities || []).concat(( hotels.entities || [])), 'id'),


