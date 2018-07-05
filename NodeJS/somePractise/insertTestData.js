/**
 * Created by shouliang on 2016/4/22.
 */
var ctc_db = require("../../models/ctcdb");
var SupplierGoodDailyMoneyStatistics = ctc_db.SupplierGoodDailyMoneyStatistics;
var SupplierGoodDailyAmountStatistics = ctc_db.SupplierGoodDailyAmountStatistics;
var moment = require("moment");
var async = require('async');

// 插入商品日销售额统计测试数据   近7日销售金额top10商品
function insertGoodDailyAmountStatistics() {
    async.auto({
        destroy: function (callback) {
            SupplierGoodDailyAmountStatistics
                .destroy({
                    where: {}
                })
                .then(function (affectedRows) {
                    console.log("destroy amount success");
                    callback(null, affectedRows);
                })
                .catch(function (error) {
                    console.log("destroy amount failure")
                });
        },
        insert: ["destroy", function (callback, result) {
            var goods = [[83, '牛栏山二锅头56度（绿瓶）'], [86, '仲景香菇酱'], [87, '（白瓶）牛栏山二锅头56度'],
                [88, '百年牛栏山清香二锅头58度'], [89, '乐乐鱼水晶双面有声挂画'], [92, '儿童投篮玩具'],
                [93, '乐趣体育玩具'], [94, '同里红 - 七年陈清爽型黄酒'], [99, '原产地赣南脐橙20斤箱装'], [108, '石龙嘴黄酒袋装']];

            var dataAry = [];
            for (var i = 0; i < 7; i++) {
                for (var j = 0; j < goods.length; j++) {
                    var obj = {};
                    obj.OnSellGoodId = goods[j][0];
                    obj.title = goods[j][1];
                    obj.amount = Math.round(Math.random() * 1000);
                    obj.saleDate = new Date(moment().subtract(i + 1, 'days').format('YYYY-MM-DD'));
                    obj.CityId = 1;
                    obj.SupplierId = 1;
                    dataAry.push(obj);
                }
            }

            SupplierGoodDailyAmountStatistics
                .bulkCreate(
                dataAry)
                .then(function (result) {
                    console.log("create amount success");
                }).catch(function (error) {
                    console.log("create amount failure");
                })
        }]
    }, function (error, results) {

    });
}

// 插入商品日金额统计测试数据
function insertGoodDailyMoneyStatistics() {
    async.auto({
        destroy: function (callback) {
            SupplierGoodDailyMoneyStatistics
                .destroy({
                    where: {}
                })
                .then(function (affectedRows) {
                    console.log("destroy money success");
                    callback(null, affectedRows);
                })
                .catch(function (error) {
                    console.log("destroy money failure")
                });
        },
        insert: ["destroy", function (callback, result) {
            var goods = [[83, '牛栏山二锅头56度（绿瓶）'], [86, '仲景香菇酱'], [87, '（白瓶）牛栏山二锅头56度'],
                [88, '百年牛栏山清香二锅头58度'], [89, '乐乐鱼水晶双面有声挂画'], [92, '儿童投篮玩具'],
                [93, '乐趣体育玩具'], [94, '同里红 - 七年陈清爽型黄酒'], [99, '原产地赣南脐橙20斤箱装'], [108, '石龙嘴黄酒袋装']];

            var dataAry = [];
            for (var i = 0; i < 7; i++) {
                for (var j = 0; j < goods.length; j++) {
                    var obj = {};
                    obj.OnSellGoodId = goods[j][0];
                    obj.title = goods[j][1];
                    obj.money = Math.round(Math.random() * 1000);
                    obj.saleDate = new Date(moment().subtract(i + 1, 'days').format('YYYY-MM-DD'));
                    obj.CityId = 1;
                    obj.SupplierId = 1;
                    dataAry.push(obj);
                }
            }

            SupplierGoodDailyMoneyStatistics
                .bulkCreate(
                dataAry)
                .then(function (result) {
                    console.log("create money success");
                }).catch(function (error) {
                    console.log("create money failure");
                })
        }]
    }, function (error, results) {

    });
}

//insertGoodDailyAmountStatistics();

//insertGoodDailyMoneyStatistics();

