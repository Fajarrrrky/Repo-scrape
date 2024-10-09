# Source by fajarxy

import requests
from bs4 import BeautifulSoup

headers: dict = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'
}

def main(url: str) -> str:
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.find_all('li', attrs={'class': 'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})
        Data_dict: dict = []
        for content in contents:
            link = content.find('div', attrs={'class': 'd-inline-block mb-1'}).find('h3', attrs={'class': 'wb-break-all'}).find('a')['href']
            repo = content.find('div', attrs={'class': 'd-inline-block mb-1'}).find('h3', attrs={'class': 'wb-break-all'}).find('a').get_text(strip=True)
            label = content.find('span', attrs={'class': 'Label Label--secondary v-align-middle ml-1 mb-1'}).text.strip()
            deskripsi = content.find('p', attrs={'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})
            desc = deskripsi.get_text(strip=True) if deskripsi else None
            data: dict = {
                'Repositories': repo+'|'+label,
                'link_repo': 'https://github.com'+link,
                'Description': desc
            }
            Data_dict.append(data)
        print(Data_dict)
    else:
        print(response.status_code)

if __name__ == '__main__':
	github = input('masukan username github: ')
	url: str = 'https://github.com/{}?tab=repositories'.format(github)
	main(url=url)
