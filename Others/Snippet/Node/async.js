async.auto({
    getData: function(callback){
        callback(null, 'data', 'converted to array');
    },
    makeFolder: function(callback){        
        callback(null, 'folder');
    },
    writeFile: ['getData', 'makeFolder', function(callback, results){        
        callback(null, 'filename');
    }],
    emailLink: ['writeFile', function(callback, results){
        callback(null, {'file':results.writeFile, 'email':'user@example.com'});
    }]
}, function(err, results) {
    console.log('err = ', err);
    console.log('results = ', results);
});

async.series({
    one: function(callback){
        callback(null, 1);
    },
    two: function(callback){
        callback(null, 2);
    }
},function(err, results) { 
});

async.waterfall([  
    function(callback){ 
      //task1 
      callback(null,1);       
    },function(data,callback){
      //task2 
      callback(null,2); 
    } 
],function(err,results){  
    console.log(results); 
});

async.parallel([
    function(callback){
        callback(null, 'one');
    },
    function(callback){
        callback(null, 'two');
    }
],
function(err, results){
});

// 多任务执行
req.body.taskIds = ["57ac2fe9403118881be24ecb"];
var taskIds = req.body.taskIds || [];
var fnTasks = [];
TaskExe.find({task: {$in: taskIds}})
    .exec(function (err, results) {
        if (err) return res.status(500).send("数据库访问失败");

        for (var i = 0; i < results.length; i++) {
            fnTasks.push(
                (function (taskexe) {
                    return function (callback) {
                        taskexe.status = "已批改";
                        taskexe.save(function (err) {
                            if (err) return callback(err);
                            callback(null, taskexe);
                        });
                    }
                })(results[i])
            );
        }

        async.parallel(fnTasks, function (err, results) {
            if (err) return res.status(500).send("数据库访问失败");
            return res.json({result: 1, data: results});
        })
    });



