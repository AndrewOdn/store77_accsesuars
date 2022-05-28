import requests
from bs4 import BeautifulSoup
f = open('text.txt', 'a', encoding='utf-8')
f.write(f'Наименование\tАртикул\tЦена\tЦвет\tКартинка\tБрэнд\tКатегория\n')
set_list = [
["chekhly_dlya_telefonov", 176],
["plenki_i_stekla", 16],
["sredstva_dlya_ukhoda", 2],
["chekhly_dlya_planshetov", 19],
["plenki_i_stekla_1", 3],
["zashchitnye_plenki_i_stekla", 3],
["chekhly", 4],
["remeshki", 14],
["myshi_i_klaviatury", 2],
["adaptery_dlya_macbook", 7],
["bloki_pitaniya", 2],
["nakladki_na_klaviaturu", 2],
["sumki_chekhly_i_ryukzaki_dlya_noutbukov", 15],
["aksessuary_dlya_apple_airpods", 16],
["dopolnitelnye_batarei", 4],
["kabeli_i_perekhodniki", 9],
["derzhateli_i_podstavki", 3],
["zaryadnye_ustroystva", 8],
["avtoderzhateli", 4],
["podarochnye_karty", 2],
]
#135
for thing in set_list:
    for iurl in range(1, thing[1]):
        url = f"https://store77.net/{thing[0]}/?reload=true&q=null&cat_id=null&ms=null&set_filter=Y&PAGEN_2=1&PAGEN_1={iurl}"
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(str(r.text), 'html.parser')
        for link in soup.find_all('div',{'class':'blocks_product_fix_w'}):
            data = str(link)
            attributes = data[str.find(data, 'onclick="dataLayer.push(')+24:str.find(data, ');">')]

            name = attributes[str.find(attributes, "'name': '")+9:]
            name = name[:str.find(name, "'")]

            artcode = attributes[str.find(attributes, "'id': '") + 7:]
            artcode = artcode[:str.find(artcode, "'")]

            price = attributes[str.find(attributes, "'price': ") + 9:]
            price = price[:str.find(price, ",")]

            brand = attributes[str.find(attributes, "'brand': '") + 10:]
            brand = brand[:str.find(brand, "'")]

            category = attributes[str.rfind(attributes, "'category': '") + 13:]
            category = category[:str.find(category, "'")]

            color = name[str.rfind(name, '(')+1:]
            color = color[:str.find(color, ')')]
            image = data[str.find(data, 'src="')+5:]
            image = image[:str.find(image, '"')]
            if 'https://store77.net' not in image:
                image = 'https://store77.net'+image
            if '/upload/' not in image:
                print(image)
                image = ''
            name = name.replace('\t', '')
            artcode = artcode.replace('\t', '')
            brand = brand.replace('\t', '')
            category = category.replace('\t', '')
            f.write(f'{name}\t{artcode}\t{price}\t{color}\t{image}\t{brand}\t{category}\n')