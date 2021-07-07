var express = require('express');
var https = require('https');
const request = require('request');

function getPolygonPoints(requestUrl){
    request(requestUrl,function (error, response, body) {
        if (!error && response.statusCode == 200) {
        var body = JSON.parse(body);
        var results = body.response.result.featureCollection.features; // array. 같은 이름의 읍면동이 존재 할 수 있기 때문.
        //results[i].properties.fullnm 을 확인해야한다. (ex)부산광역시 금정구 장전동
        //우선 첫번째 값만 이용하자.
        console.log(results);
        console.log("-------");
        var polygons = results[0].geometry.coordinates[0][0];
        console.log(polygons);
        }else{
        console.log(error);
        }
    });
}

function testFunc(){
    console.log("test FUNC FUNC");
}
module.exports = {
    polygon : getPolygonPoints,
    testFunc : testFunc
}
