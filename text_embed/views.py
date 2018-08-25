from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponse
from django import forms

from PIL import Image
import numpy as np
import functools
# Create your views here.

def embedding_info(request):
    if request.method == 'POST':
        text = request.POST['text']
        text = '#$#' + text
        text += '#%#' #作为结束标记
        
        img = request.FILES.get('beforeimg', None)
        
        if not img.name.endswith('.png'):
            raise Http404
        
        im = np.array(Image.open(img))        
        rows, columns, colors = im.shape
        embed = []
        for c in text:
            bin_sign = (bin(ord(c))[2:]).zfill(16)
            for i in range(16):
                embed.append(int(bin_sign[i]))
        
        count = 0
        for row in range(rows):
            for col in range(columns):
                for color in range(colors):
                    if count < len(embed):
                        im[row][col][color] = im[row][col][color] // 2 * 2 + embed[count]
                        count += 1

        Image.fromarray(im).save('After.png')

        file=open('After.png','rb')  
        response =HttpResponse(file)  
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename="After.png"'  
        return response 

    return render(request, 'text_embed/embedding_info.html')
    

def extract_info(request):
    if request.method == 'POST':
        img = request.FILES.get('afterimg', None)

        if not img.name.endswith('.png'):
            raise Http404

        im = np.array(Image.open(img))
        rows, columns, colors = im.shape
        text = ""
        extract = np.array([], dtype = int)

        count = 0
        for row in range(rows):
            for col in range(columns):
                for color in range(colors):
                    extract = np.append(extract, im[row][col][color] % 2)
                    count += 1
                    if count % 16 == 0:
                        bcode = functools.reduce(lambda x, y: str(x) + str(y), extract)
                        cur_char = chr(int(bcode, 2))
                        text += cur_char
                        if len(text) == 3 and text != '#$#':
                            content = { 'text':'非标准格式文件，无法解密' }
                            return render(request, 'text_embed/extract_info.html', content)
                        if cur_char == '#' and text[-3:] == '#%#':
                            # text = text[3:]
                            content = { 'text':text[3:-3] }
                            return render(request, 'text_embed/extract_info.html', content)
                        extract = np.array([], dtype=int)

    return render(request, 'text_embed/extract_info.html')