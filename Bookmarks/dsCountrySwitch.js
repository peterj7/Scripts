javascript:
function(){
  if(document.location.href.indexOf("aem")>=0){
    a=((document.location.href).indexOf('jmp-discovery-summit'));
    b=(document.location.href).substring((a+20),(a+24));
    c=(document.location.href).split(b);document.location.href='INSERT BEGINNING URL HERE'+'/en/'+c[1];
  }else{
    a=((document.location.href).indexOf('.jmp'));
    b=(document.location.href).substring((a+4),(a+8));
    c=(document.location.href).split(b);document.location.href=c[0]+'/en/'+c[1];
  }
}();
