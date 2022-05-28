import requests
from PIL import Image
from io import BytesIO
import requests
import openpyxl
from openpyxl import Workbook


def get_img(url):
    r = requests.get(url, stream=True, verify=False)
    if not r.ok:
        r.raise_for_error()
    r.raw.decode_content = True
    img = Image.open(r.raw)
    temp = BytesIO()
    img.save(temp, format="png")
    temp.seek(0)
    return Image.open(temp)


def insert_row(ws, img_url, num, size=(200,200)):
    img = openpyxl.drawing.image.Image(get_img(img_url))
    row_num = ws.max_row + 1
    cell_addr = f"A{num}"
    img.anchor = cell_addr
    ws.add_image(img)
    ws.row_dimensions[row_num].height = int(size[1] * .8)
    ws.column_dimensions["A"].width = int(size[0] * .2)

##############################################################################
size = (200, 200)
wb = Workbook()
ws = wb.active


f = open('text.txt', 'r', encoding='utf-8')
i = 0
for line in f:
    i = i + 1
    if i > 2920:
        ting = line.split("\t")
        im_url_nastya = str(ting[4])
        if len(im_url_nastya) > 15:
            if str.find(im_url_nastya, "https://store77.net") > 0:
                im_url_nastya = 'https://store77.net' + im_url_nastya
            insert_row(ws, im_url_nastya,i, size=size)
        wb.save('test.xlsx')