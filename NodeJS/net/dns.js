const dns = require('dns');
const host = 'www.baidu.com';

dns.lookup(host,(err,address,family)=>{
    if(err){
        console.error(err);
    }
    console.log('by net.lookup, address is:%s,family is:%s',address,family);
});

dns.resolve(host,(err,address)=>{
    if(err){
        console.error(err);
        return;
    }

    console.log('by net.resolve,address is:%s',address);

})