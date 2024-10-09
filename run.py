# !sourceby fajarxy

import requests, os, csv
import pandas as pd
from rich.console import Console
from bs4 import BeautifulSoup
console = Console()

headers: dict = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

def repo_list(url: str) -> str:
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            contents = soup.find_all('li', attrs={'class': 'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})
            Data = []
            for content in contents:
                link = content.find('div', attrs={'class': 'd-inline-block mb-1'}).find('h3', attrs={'class': 'wb-break-all'}).find('a')['href']
                repo = content.find('div', attrs={'class': 'd-inline-block mb-1'}).find('h3', attrs={'class': 'wb-break-all'}).find('a').get_text(strip=True)
                label = content.find('span', attrs={'class': 'Label Label--secondary v-align-middle ml-1 mb-1'}).text.strip()
                deskripsi = content.find('p', attrs={'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})
                desc = deskripsi.get_text(strip=True) if deskripsi else None
                data = {
                    'Repositories': repo+' -> '+label,
                    'link_repo': 'https://github.com'+link,
                    'Description': desc
                }
                Data.append(data)
            return Data
        else:
            console.print(f' [bold red]# {response.status_code}')
            exit()
    except requests.exceptions.ConnectionError:
        console.print(" [bold red]# ConnectionError Coba lagi!![bold white]")

def detail_repo(detail_url: str) -> str:
    try:
        response = requests.get(detail_url, headers = headers)
        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr', class_='react-directory-row undefined')
            Data = []
            for row in rows:
                a_tag = row.find('a', attrs={'class': 'Link--primary'})
                primary = a_tag.get_text(strip=True) if a_tag else None
                url_blob = a_tag['href'] if a_tag else 'No link'
                data = {
                    'File': primary
                }
                Data.append(data)
            return Data
        else:
            console.print(f' [bold red]# {response.status_code}')
            exit()
    except requests.exceptions.ConnectionError:
        console.print(" [bold red]# ConnectionError Coba lagi!![bold white]")
        exit()

def main(url: str) -> None:
    results: list[dict[str, str]] = []
    data = repo_list(url=url)
    for x in data:
        repo = x.get('Repositories')
        url_repo = x.get('link_repo')
        desc = x.get('Description')
        details = detail_repo(detail_url=url_repo)
        console.print(f"""
 [bold green]#[bold white] Repositories: [bold green]{repo}[bold white]
 [bold green]#[bold white] Repositories Url: [bold green]{url_repo}[bold white]
 [bold green]#[bold white] Description: [bold green]{desc}[bold white]""")
        file_list = []
        for z in details:
            file = z.get('File')
            if file:
                console.print(f" [bold green]#[bold white] Files: [bold green]{file}[bold white]")
                file_list.append(file)
                
        file_str = ', '.join(file_list)
        results.append({
            'Repositories': repo,
            'Repositories Url': url_repo,
            'Description': desc,
            'Files': file_str
        })
        
    df = pd.DataFrame(results)
    df.to_csv('repository.csv', index=False)
            
    exit()
        
if __name__ == '__main__':
    os.system('clear')
    github = input('masukan username github: ')
    main(url='https://github.com/{}?tab=repositories'.format(github))