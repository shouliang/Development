/**
 * Created by shouliang on 2016/5/4.
 */
//  logging: console.log, a function (or false) for logging your queries
//  plain: false,  if plain is true, then sequelize will return all of the records within an array, otherwise it will return a single object/first record returned.
//  raw: false,    Set this to true if you don't have a model definition for your query
ctc_db.SupplierGoods.findAll({
    where: {
        state:10
    },
    attributes: ["supplierId","GoodId"]
    //,
    // logging:false,  
    // plain: true,    
    // raw: true       
}).then(function (result) {
    console.log(result);
    //callback(null, result);
}).catch(function (error) {
    //callback({message: "", error: error});
});