var express = require('express');
var router = express.Router();


router.get('/', function(req, res, next) {
  console.log("welcoe to home");
  res.render('index', { title: 'Express' });
});


router.post('/a', function(req, res, next){
  // console.log(req.body)
  res.render('index', { title: 'Express' })
});


module.exports = router;