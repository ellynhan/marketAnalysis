var express = require('express');
var request = require('request');
var router = express.Router();
var app = express();
var client_id = '3go24950yq';
var client_secret = 'gxpQojpBaijKvuhVwJnZB9pzCK8OL163RA8I8O7k';
const querystring = require('querystring');

router.get('/', function(req, res, next) {
  console.log("welcoe to home");
  res.render('index', { title: 'Express' });
});


router.post('/a', function(req, res, next){
  // console.log(req.body)
  res.render('index', { title: 'Express' })
});


module.exports = router;
