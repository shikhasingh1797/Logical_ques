var n=require("readline-sync")
var pass=n.question("Enter strong password :")
var l=0
var p=0
var d=0
if (pass.length==4){
    for (var i=0; i<pass.length;i++){
    if (pass[i]>="0" && pass[i]<="9"){
        l++
    }
      else if (pass[i]>="a" && pass[i]<="z"){
            p++
        }
      else if(pass[i]=="@" || pass[i]=="#"){
            d++
        }
    }
}
if (l>=1 &&  p>=1 && d>=1 && l+p+d==pass.length){
    console.log("Strong Password")
}
else{
    console.log("Not Strong Password")
}