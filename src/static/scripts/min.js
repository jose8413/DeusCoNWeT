"use strict";angular.module("PicBit").controller("AboutCtrl",function(a,b,c){}),angular.module("PicBit").controller("contactCtrl",function(a,b){}),angular.module("PicBit").controller("FormularioCtrl",function(a,b,c){a.mailTo=function(){var a="mailto:deus@conwet.com?cc=deus@conwet.com&subject=beta&body="+document.querySelector("#mensaje").value;window.location.href=a}}),angular.module("picbit").controller("landingCtrl",function(a,b){}),angular.module("picbit").controller("MainCtrl",function(a,b,c){a.status=!1,a.logged=function(c){a.$apply(function(){if(a.hidePopup(),"twitter"===c.detail.redSocial)b.path("/user/"+c.detail.redSocial+"_"+c.detail.userId);else if("googleplus"===c.detail.redSocial){var d=new XMLHttpRequest,e="https://www.googleapis.com/plus/v1/people/me?access_token="+c.detail.token;d.open("GET",e,!0),d.onreadystatechange=function(){4==d.readyState&&200===d.status?a.$apply(function(){var e=JSON.parse(d.responseText);b.path("/user/"+c.detail.redSocial+"_"+e.id),a.sendData(c.detail.token,e.id,c.detail.redSocial)}):4==d.readyState&&console.log("[INFO]: Algo fue mal en google")},d.send()}else b.path("/user/"+c.detail.redSocial+"_"+c.detail.userId),a.sendData(c.detail.token,c.detail.userId,c.detail.redSocial);var f=document.querySelector("#nameId");f.innerHTML="Desconectar",a.status=!0})},a.sendData=function(a,b,c){var d=new XMLHttpRequest,e="http://example-project-13.appspot.com/api/oauth/"+c,f="token_id="+a+"&access_token="+b;d.open("POST",e,!0),d.setRequestHeader("Content-type","application/x-www-form-urlencoded"),d.onreadystatechange=function(){4==d.readyState&&200!==d.status&&201!==d.status&&console.log("[INFO]: Error al introducir datos en backend")},d.send(f)},a.changeView=function(a){b.path(a)},a.logout=function(){var c=document.querySelector("#nameId");c.innerHTML="Entrar",b.path("/"),a.status=!1},document.querySelector("body").addEventListener("google-logged",a.logged),document.querySelector("body").addEventListener("linkedin-logged",a.logged),document.querySelector("body").addEventListener("github-logged",a.logged),document.querySelector("body").addEventListener("instagram-logged",a.logged),document.querySelector("body").addEventListener("twitter-logged",a.logged),document.querySelector("body").addEventListener("facebook-logged",a.logged),document.querySelector("body").addEventListener("sof-logged",a.logged),a.popup=!1,a.showPopup=function(){a.status?a.logout():a.popup=!0},a.hidePopup=function(){a.popup=!1}}),angular.module("picbit").controller("SearchCtrl",function(a){a.orderBy="asc",a.sortBy="name",a.webComponents=a.$parent.webComponents,a.setSort=function(b){a.sortBy=b,getAllComponent(a.orderBy,a.sortBy)},a.setOrder=function(){a.orderBy="des"===a.orderBy?"asc":"des"},a.changeList=function(b){a.setOrder(),a.setSort(b)},a.init=function(){var b=function(b){a.$apply(function(){a.webComponents=b})};getAllComponents(a.orderBy,a.sortBy,b)},a.respuesta="",a.open=function(){var a=document.getElementById("inputC");a.validity.valid&&null!==a.inputValue&&google.appengine.api.picbit.uploadComponent(a.inputValue)}}),angular.module("picbit").controller("userHomeCtrl",function(a,b){a.list=[{name:"John"},{name:"Jessie"},{name:"Johanna"},{name:"Joy"},{name:"Mary"},{name:"Peter"},{name:"Sebastian"},{name:"Erika"},{name:"Patrick"},{name:"Samantha"}],a.menuStatus=!1,a.showElement=!1,a.listaOpciones=["false","false","false"],a.showMenu=function(){a.menuStatus?(document.querySelector("#menu-icon").icon="arrow-back",a.menuStatus=!1,a.showElement=!1,a.selected="",a.showSingle="",a.listaOpciones=["false","false","false"]):(document.querySelector("#menu-icon").icon="arrow-forward",a.menuStatus=!0,b(function(){a.showElement=!0},350))},a.setList=function(b){switch(b){case"add":a.listaOpciones=[!a.listaOpciones[0],"false","false"],document.querySelector("#arrowAdd").icon=a.listaOpciones[0]?"arrow-drop-down":"arrow-drop-up";break;case"delete":a.listaOpciones=["false",!a.listaOpciones[1],"false"],document.querySelector("#arrowDelete").icon=a.listaOpciones[1]?"arrow-drop-down":"arrow-drop-up";break;case"modify":a.listaOpciones=["false","false",!a.listaOpciones[2]],document.querySelector("#arrowModify").icon=a.listaOpciones[2]?"arrow-drop-down":"arrow-drop-up"}},a.hidelist=function(b){switch(b){case"add":return a.listaOpciones[0];case"delete":return a.listaOpciones[1];case"modify":return a.listaOpciones[2];default:return!1}},a.isSelected=function(b){return a.selected===b&&void 0!=b},a.setSelected=function(c){a.selected===c?(a.selected="",a.showSingle="",a.hidelist(c)||a.setList(c)):(a.selected=c,b(function(){a.showSingle=c},350))},a.isMenuHidden=function(b){return!(a.menuStatus|a.isSelected(b))}});