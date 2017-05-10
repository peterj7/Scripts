javascript:
a=((document.location.href).indexOf('INSERT UNIQUE IDENTIFIER HERE'));
b=(document.location.href).substring((a-2),(a+3));
c=(document.location.href).split(b);
function(){
  if(document.location.href.indexOf("INSERT UNIQUE IDENTIFIER HERE")>=0){
    document.location.href='INSERT BEGINNING URL HERE'+'/INSERT COUNTRY CODE HERE'+c[1];
  } else{
    document.location.href=c[0]+'INSERT COUNTRY CODE HERE'+c[1];
  }
}();
