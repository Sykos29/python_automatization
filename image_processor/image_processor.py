from PIL import Image, ImageEnhance, ImageFilter
import os

pathIn = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(pathIn):
    img = Image.open(f"{pathIn}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
