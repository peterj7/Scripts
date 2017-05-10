javascript:
a=((document.location.href).split('.html')[0]);
b=(a.split('content/jmp')[1]);
function(){
  if(document.location.href.indexOf("aemauthor")>=0&& document.location.href.indexOf("ondemand")>=0){
    document.location.href='INSERT BEGINNING URL HERE'+b+'/watch.html';
  }else if(document.location.href.indexOf("ondemand")>=0){
    document.location.href= a+'/watch.html';
  }else if(document.location.href.indexOf("aemauthor")>=0){
    document.location.href= a+'/thanks.html';
  }else{
    document.location.href= a+'/thanks.html';
  }
}();
