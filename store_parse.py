import requests
from bs4 import BeautifulSoup


def get_catalog_urls():

    url = 'https://store77.net/'

    r = requests.get(url, verify=False)
    soup = BeautifulSoup(str(r.text), 'html.parser')

    cat_links = soup.find_all(class_='dl-submenu')

    url_soup = BeautifulSoup(str(cat_links), 'html.parser')
    urls = url_soup.find_all('a', class_='mob_catalog_ico')

    res = []

    for u in urls:
        link = str(u)
        link = link[str.find(link, 'href="') + 6:str.find(link, '">')]
        if '#' not in link:
            res.append('https://store77.net' + link)
    return res


def get_items_urls(url_list):

    for url in url_list:

        r = requests.get(url, verify=False)
        soup = BeautifulSoup(str(r.text), 'html.parser')

        for link in soup.find_all('div', class_='brand_zone_device_item'):
            item_url = 'https://store77.net' + link.find('a', class_='brand_zone_device_col').get('href')

            print(item_url)


def main():
    print(*get_catalog_urls(), sep='\n')
    # get_items_urls(url_list)


if __name__ == '__main__':
    main()


# url = 'https://store77.net/apple_brand_zone/'
#
# r = requests.get(url, verify=False)
#
# soup = BeautifulSoup(str(r.text), 'html.parser')
#
# categories_names = soup.find(class_='collapse_menu').text.strip().split('\n')[1:]
# categories_urls = soup.find('ul', class_='collapse_menu')
#
#
# foup = BeautifulSoup(str(categories_urls), 'html.parser')
# urll = foup.find_all('a')
# for url in urll:
#     link = str(url)
#     link = link[str.find(link,'href="')+6:str.find(link, '">')]
#     print(link)
