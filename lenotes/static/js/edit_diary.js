name = '';
oDiv = '';
disX = 0;
disY = 0;
selected = '';

$(document).ready(function(){ 
    $("#texform").hide();
    $("#picform").hide();
}); 


function delete_ele(){
    $.ajax({
        url:'/delete_ajax/',
        type:'POST',
        data: {"del_id":name},
        //  processData: false,  // tell jquery not to process the data
        //  contentType: false, // tell jquery not to set contentType
        success: function(callback) {
           
        }
    });
    $("#"+name).remove();
}

//当文本内容改变时触发该函数，实时更新内容
function changeContent(minput){
    oDiv = $("#"+name);
    oDiv.html(minput.value);
  //  console.log(minput.value);
}

function texmove(ev,mdiv)
{
    //console.log(ev['path'][0].id);
    name = mdiv.id;
    $("#texId").val(mdiv.id);
    $("#texform").show();
    $("#picform").hide();
    oDiv = $("#"+name);
    $("#texContent").val(oDiv.html())
    var oEvent = ev; 
    disX =  oDiv.position().left;
    disY =  oDiv.position().top;
    initialX = oEvent.clientX;
    initialY = oEvent.clientY;
    document.onmousemove=function (ev)
    {   
        oEvent = ev;
        //console.log(oEvent.clientX -disX);
      //  console.log()
        oDiv.css("left",disX+oEvent.clientX-initialX +"px");
        oDiv.css("top",disY+oEvent.clientY-initialY+"px");
    }
    /*document.onmouseup=function()
    {
        
    } */
    
}

function Fontcolor(color){
    tex = $("#"+name);
    var colorstr;
    switch(color){
        case 1: colorstr="red"; break;
        case 2: colorstr="black"; break;
        case 3: colorstr="white"; break;
        case 4: colorstr="green"; break;
    }
    tex.css("color",colorstr);
}

function picWChange(minput){
    pic = $("#"+name);
    if(parseInt(minput.value)>0)
        pic.css("width",minput.value + "px");
    else
        alert("图片宽要大于0哦~");
}

function picHChange(minput){
    pic = $("#"+name);
    if(parseInt(minput.value)>0)
        pic.css("height",minput.value + "px");
    else
        alert("图片高要大于0哦~");
}


function addzindex(){
    ele = $("#"+name);
    nowZ = parseInt(ele.css("z-index"));
    nowZ++;
    ele.css("z-index",nowZ);
}   

function subzindex(){
    ele = $("#"+name);
    nowZ = parseInt(ele.css("z-index"));
    nowZ--;
    ele.css("z-index",nowZ);
}

function addFontsize(){
    tex = $("#"+name);
    nowSize = parseInt(tex.css("font-size"));
    nowSize++;
    tex.css("font-size",nowSize+"px");
}

function subFontsize(){
    tex = $("#"+name);
    nowSize = parseInt(tex.css("font-size"));
    if(nowSize>0)
        nowSize--;
    else
        alert("不能再小啦~");
    tex.css("font-size",nowSize+"px");
}

function picmove(ev,mdiv)
{
    //console.log(ev['path'][0].id);
    name = mdiv.id;
    $("#texId").val(mdiv.id);
    $("#picform").show();
    $("#texform").hide();
    oDiv = $("#"+name);
    var oEvent = ev; 
    disX =  oDiv.position().left;
    disY =  oDiv.position().top;
    $("#picHeight").val(parseInt(oDiv.css("height")));
    $("#picWidth").val(parseInt(oDiv.css("width")));
   // console.log("disX"+disX);
   // console.log("disY"+disY);
    initialX = oEvent.clientX;
    initialY = oEvent.clientY;
    document.onmousemove=function (ev)
    {   
        oEvent = ev;
        //console.log(oEvent.clientX -disX);
      //  console.log()
       // console.log(oEvent.clientX-initialX);
       // console.log(oEvent.clientY-initialY);
        oDiv.css("left",disX+oEvent.clientX-initialX +"px");
        oDiv.css("top",disY+oEvent.clientY-initialY+"px");
    }
    /*document.onmouseup=function()
    {
        
    } */
    
}

function reset(){
    document.onmousemove=null;
    document.onmouseup=null;
}

function TexUpload(){
    var texId = $("#texId").val();
    if(texId.length == 0){
        alert("id字段不能为空");
        return;
    }
    var tex = $("#tex"+texId);
    if(tex == null){
        alert("不存在此id的文本块");
        return;
    }

    var texContent = $("#texContent").val();
   // alert(tex.text());
    var texX = $("#texX").val();
    var texY = $("#texY").val();
    var texFontcolor = $("#texFontcolor").val();
    var texFontsize = $("#texFontsize").val();
    var texZ = $("#texZ").val();
    if(texContent.length != 0)
        tex.html(texContent);
    else
        tex.html("");

    if(texX.length != 0)
        tex.css("left",texX+"px");
    if(texY.length != 0)
        tex.css("top",texY+"px");
    if(texZ.length != 0)
        tex.css("z-index",texZ);
    if(texFontcolor.length != 0)
        tex.css("color",texFontcolor);
    if(texFontsize.length != 0)
        tex.css("font-size",texFontsize+"px");
}

function PicUpload(){
    var picId = name;
    if(picId.length == 0){
        alert("id字段不能为空");
        return;
    }
    var pic = $("#"+picId);
    if(pic == null){
        alert("不存在此id的文本块");
        return;
    }

    
    //var picX = $("#picX").val();
    //var picY = $("#picY").val();
    var picH = $("#picHeight").val();
    var picW = $("#picWidth").val();
    //var picZ = $("#picZ").val();
    // if(picX.length != 0)
    //     pic.css("left",picX+"px");
    // if(picY.length != 0)
    //     pic.css("top",picY+"px");
    // if(picZ.length != 0)
    //     pic.css("z-index",picZ);
    if(picH.length != 0)
        pic.css("height",picH+"px");
    if(picW.length != 0)
        pic.css("width",picW+"px");
}


mydata = {
    "a" : "lalala",
    "b" : {
        "a" : "123",
        "b" : "123",
    }
};

function collect(){
    var ret = {};
    var boxS = $("#MainContent").children();
    for(var i=0; i<boxS.length; i++){
        var newitem = {};
        tid = boxS[i].getAttribute("id");
        ele = $("#"+tid);
        if(tid[0] == 't'){
            newitem["x"] = ele.css("left");
            newitem["y"] = ele.css("top");
            newitem["content"] = ele.html();
            newitem["fontcolor"] = document.getElementById(tid).style.color;
            newitem["fontsize"] = ele.css("font-size");
            newitem["z"] = ele.css("z-index");
            //console.log(document.getElementById(tid).style.color);
        }
        else if(tid[0] == 'p'){
            newitem["x"] = ele.css("left");
            newitem["y"] = ele.css("top");
            newitem["w"] = ele.css("width");
            newitem["h"] = ele.css("height");
            newitem["z"] = ele.css("z-index");
        }
        ret[tid] = newitem;
    }
    return ret;
    //console.log(chi);
}

function AllUpload(){


    mydata = collect();
    $.ajax({
        url:'/upload_ajax/',
        type:'POST',
        dataType: "json",
        data: JSON.stringify(mydata),
        //  processData: false,  // tell jquery not to process the data
        //  contentType: false, // tell jquery not to set contentType
        success: function(callback) {
            console.log('ok');
        }
    })
}

