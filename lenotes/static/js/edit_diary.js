function TexUpload() {
    texId = $("#texId").val();
    if (texId.length == 0) {
        alert("id字段不能为空");
        return;
    }
    tex = $("#" + texId);
    if (tex == null) {
        alert("不存在此id的文本块");
        return;
    }

    texContent = $("#texContent").val();
    alert(texContent);
    texX = $("#texX").val();
    texY = $("#texY").val();
    texFontcolor = $("#texFontcolor").val();
    texFontsize = $("#texFontsize").val();
    texZ = $("#texZ").val();
    if (texContent.length != 0)
        tex.html(texContent);
    else
        tex.html("");

    if (texX.length != 0)
        tex.css("left", texX + "px");
    if (texY.length != 0)
        tex.css("top", texY + "px");
    if (texZ.length != 0)
        tex.css("z-index", texZ);
    if (texFontcolor.length != 0)
        tex.css("color", texFontcolor);
    if (texFontsize.length != 0)
        tex.css("font-size", texFontsize + "px");
}