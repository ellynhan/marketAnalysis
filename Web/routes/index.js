var express = require('express');
var fs = require('fs');
var path = require('path');
var router = express.Router();
var request = require('request');

router.get('/', function(req, res, next) {
  console.log("welcoe to home");
  var readAnswer = fs.createReadStream(path.join(__dirname, '../../DATA') + '/answer.txt', 'utf8');
  var readFinalData = fs.createReadStream(path.join(__dirname, '../../DATA') + '/final_data.txt', 'utf8');
  var data = '';
  var finalData = '';
  var buffers = [];
  var buffers2 = [];
  var mapTest = {};

  readAnswer.on('data', function(chunk) {
    data += chunk;
  }).on('end', function() {
    buffers = data.split('\n');
    readFinalData.on('data', function(chunk2) {
      finalData += chunk2;
    }).on('end', function(){
      buffers2 = finalData.split('\n');
      buffers2.forEach(element => {
        var tmp = element.split(':');
        if(tmp[0]!=undefined && tmp[0]!=''){
          if(tmp[1]!=undefined){
            mapTest[tmp[0]] = tmp[1].split(',');
          }else{
            mapTest[tmp[0]] = [];
          }
        }
      });
      res.render('index', { scores: buffers, details: mapTest });
    })
  });
});


router.post('/a', function(req, res, next){
  // console.log(req.body)
  res.render('index', { title: 'Express' })
});


module.exports = router;