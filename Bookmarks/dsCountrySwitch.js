javascript:
function(){
  if(document.location.href.indexOf("INSERT UNIQUE IDENTIFIER HERE")>=0){
    a=((document.location.href).indexOf('INSERT UNIQUE IDENTIFIER HERE'));
    b=(document.location.href).substring((a+20),(a+24));
    c=(document.location.href).split(b);document.location.href='INSERT BEGINNING URL HERE'+'/INSERT COUNTRY CODE HERE/'+c[1];
  }else{
    a=((document.location.href).indexOf('INSERT UNIQUE IDENTIFIER HERE'));
    b=(document.location.href).substring((a+4),(a+8));
    c=(document.location.href).split(b);document.location.href=c[0]+'/INSERT COUNTRY CODE HERE/'+c[1];
  }
}();
