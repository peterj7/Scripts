javascript:
a=((document.location.href).indexOf('_'));
b=(document.location.href).substring((a-2),(a+3));
c=(document.location.href).split(b);
function(){
  if(document.location.href.indexOf("aem")>=0){
    document.location.href='http://aemauthor.unx.sas.com:4502/cf#/content/jmp/en_us'+c[1];
  } else{
    document.location.href=c[0]+'en_us'+c[1];
  }
}();
