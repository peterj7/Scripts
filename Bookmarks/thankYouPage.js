javascript:
a=((document.location.href).split('.html')[0]);
b=(a.split('content/jmp')[1]);
function(){
  if(document.location.href.indexOf("aemauthor")>=0&& document.location.href.indexOf("ondemand")>=0){
    document.location.href='http://aemauthor.unx.sas.com:4502/cf#/content/jmp'+b+'/watch.html';
  }else if(document.location.href.indexOf("ondemand")>=0){
    document.location.href= a+'/watch.html';
  }else if(document.location.href.indexOf("aemauthor")>=0){
    document.location.href= a+'/thanks.html';
  }else{
    document.location.href= a+'/thanks.html';
  }
}();
