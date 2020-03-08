var express =require("express");
var app=express();
var request=require('request');
var bodyparser = require('body-parser');
app.use(bodyparser.urlencoded({extended:true}));
app.use( express.static( "public" ) );
 
app.set("view engine","ejs" );
var s="http://";
var ip;

 app.get("/",function(req,res){
 res.render("index.ejs");                

 });

 app.get("/remote",function(req,res){

 ip=s+req.query.ha+"/";
 res.render("remote");

 });
 app.get("/command",function(req,res){
var r=ip+req.query.direction;
console.log(r);
 request(r,function(er,res,body){
   if(er){

   	console.log("Error has occured");
 	
  }else{

   	if(res.statusCode==200){

   console.log(body);


   	}
   }
 
 });

res.render("remote.ejs")

});
app.listen(3000,function(){

console.log("Server has started");

});