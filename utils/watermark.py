#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : watermark
# @Date     : 2018/7/30
# @Author   : Maliao
# @Link     : None
from PIL import Image, ImageDraw, ImageFont
from conf import settings
import os

def str2img(txt, path):
    font_path = os.path.join(settings.BASE_DIR,'files','font','SourceHanSans-Medium.ttc')
    font = ImageFont.truetype(font_path, 20)

    # 黑底圖 默認是黑色 大小為128x128
    im = Image.new("RGB", (180, 130), (1, 152, 255))
    draw = ImageDraw.Draw(im)

    xpos_list = [0, 80, 70, 55, 55, 45, 40, 35, 30, 25, 20]
    text = txt
    text = text[:10]
    draw.text(xy=(xpos_list[len(text)], 45), text=text, font=font)
    im.save(path)
