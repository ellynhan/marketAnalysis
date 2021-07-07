var express = require('express');
var https = require('https');
var router = express.Router();
const request = require('request');
// var app = express();
// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));


router.get('/', function(req, res, next) {
  var basicUrl = 'http://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_ADEMD_INFO&key=';
  var key = '키를 입력하세요';
  var domainUrl = '&domain=http://localhost:3000/bound'; //도메인 url 꼭 있어야 작동함. 
  var attrFilter = '&attrFilter=emd_kor_nm:like:';
  var regionCode = "|emd_cd:like:"+"41"; //emd_kor_nm:like:갈산동|emd_cd:like:41
  var filterValue = '장전';
  var requestUrl = basicUrl+key+domainUrl+attrFilter+encodeURI(filterValue);

  request(requestUrl,function (error, response, body) {
  if (!error && response.statusCode == 200) {
    var body = JSON.parse(body);
    var results = body.response.result.featureCollection.features; // array. 같은 이름의 읍면동이 존재 할 수 있기 때문.
    //results[i].properties.fullnm 을 확인해야한다. (ex)부산광역시 금정구 장전동
    //우선 첫번째 값만 이용하자.
    var polygons = results[0].geometry.coordinates[0][0];
    console.log(polygons);
  }else{
    console.log(error);
  }
});
  res.send('respond with a resource');
});

module.exports = router;

/*
 서울특별시 11
 부산광역시 26
 대구광역시 27
 인천광역시 28
 광주광역시 29
 대전광역시 30
 울산광역시 31
 새종특별자치시 36
 경기도 41
 강원도 42
 충청북도 43
 충청남도 44
 전라북도 45
 전라남도 46
 경상북도 47
 경상남도 48
 제주특별자치도 50
*/ 
