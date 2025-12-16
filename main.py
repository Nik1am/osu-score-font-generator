import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

fonts = os.listdir("./fonts/")

def char_to_filename(c):
    if c == "%":
        return "percent"
    if c == ",":
        return "comma"
    if c == ".":
        return "dot"
    return c

def max_height(f):
    m = 0
    for char in "0123456789x,.%":
        x = f.getbbox(char)[3]
        if x > m:
            m = x
    return m


for font_file in fonts:
    if font_file == "DELETEME":
        continue
    font_path = f"./fonts/{font_file}"
    font_size = 64
    font = ImageFont.truetype(font_path, font_size)

    folder_to_save = f"./output/{font_file}"

    if not os.path.isdir(folder_to_save):
        os.makedirs(folder_to_save)

    num_height = max_height(font)#used to fix the fucking comma

    for char in "0123456789x,.%":
        bbox = font.getbbox(char)
        
        margin_h = 2
        margin_v = 3

        width = bbox[2]
        height = bbox[3]
        print(char, font_file, bbox)

        img = Image.new("LA", [width + margin_h*2, num_height + margin_v*2])
        draw = ImageDraw.Draw(img)

        draw.text((margin_h, img.size[1]//2 + margin_v), char, fill=(0, 255), font=font, anchor="lm")

        img = img.filter(ImageFilter.GaussianBlur(2))
        
        draw = ImageDraw.Draw(img)

        draw.text((margin_h, img.size[1]//2 + margin_v), char, fill=(255, 255), font=font, anchor="lm")
        
        img.save(f"{folder_to_save}/score-{char_to_filename(char)}.png")