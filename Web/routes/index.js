var express = require('express');
var fs = require('fs');
var path = require('path');
var router = express.Router();

router.get('/', function(req, res, next) {
  console.log("welcoe to home");
  var readStream = fs.createReadStream(path.join(__dirname, '../../DATA') + '/answer.txt', 'utf8');
  var data = ''
  var buffers = [];
  readStream.on('data', function(chunk) {
    data += chunk;
  }).on('end', function() {
      // console.log(data);
      buffers = data.split('\n');
      // console.log(buffers[0]);
      res.render('index', { scores: buffers });
  });
});


router.post('/a', function(req, res, next){
  // console.log(req.body)
  res.render('index', { title: 'Express' })
});


module.exports = router;