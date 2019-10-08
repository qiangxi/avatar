#!/usr/bin/env python3

from PIL import Image


def add_flag(src_img, flag_img):
    # src_img = src_img.convert(mode = "RGBA")
    # flag_img = flag_img.convert(mode = "RGBA")
    # flag_img = flag_img.resize((src_img.width // 5, src_img.height // 5))
    # src_img.paste(flag_img, (src_img.width - flag_img.width, src_img.height - flag_img.height))
    # Image.alpha_composite(src_img, flag_img)

    return src_img


srcImg = Image.open("res/avatar.png").convert(mode = "RGBA")  # type: Image.Image
flagImg = Image.open("res/flag.png").convert(mode = "RGBA")  # type: Image.Image
Image.alpha_composite(srcImg, flagImg).save("result.png")
# dstImg = add_flag(srcImg, flagImg)
# dstImg.save("result.png")
# srcImg.close()
# flagImg.close()
