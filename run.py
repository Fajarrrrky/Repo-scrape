# !!source code by fajarxy

import requests, os, csv
import pandas as pd
from git import Repo
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
            soup = BeautifulSoup(response.text, 'html.parser')
            contents = soup.find_all('li', attrs={'class': 'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})
            Data = []
            for content in contents:
                link = content.find('a', href=True)['href']
                repo = content.find('h3').get_text(strip=True).replace('Public', '')
                label = content.find('span', class_='Label').get_text(strip=True) if content.find('span', class_='Label') else None
                deskripsi = content.find('p', class_='col-9 d-inline-block color-fg-muted mb-2 pr-4')
                desc = deskripsi.get_text(strip=True) if deskripsi else None
                data = ({
                    'Repositories': repo +'|'+ label,
                    'Repositories Url': 'https://github.com'+link,
                    'Description': desc
                })
                Data.append(data)
            return Data
        else:
            console.print(f' [bold red]# {response.status_code}')
            return None
    except requests.exceptions.ConnectionError:
        console.print(" [bold red]# ConnectionError Coba lagi!![bold white]")
        return None

def repo_file_list(detail_url: str) -> str:
    try:
        response = requests.get(detail_url, headers = headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr', class_='react-directory-row undefined')
            Data = []
            for row in rows:
                a_tag = row.find('a', class_='Link--primary')
                if a_tag:
                	Data.append(a_tag.get_text(strip=True))
            return Data
        else:
            console.print(f' [bold red]# {response.status_code}')
            return []
    except requests.exceptions.ConnectionError:
        console.print(" [bold red]# ConnectionError Coba lagi!![bold white]")
        return []

def clone_repository(repo_url: str, clone_dir: str):
    try:
        console.print(f" [bold green]#[bold white] mengkloning {repo_url} ke dalam {clone_dir}...")
        Repo.clone_from(repo_url, clone_dir)
        console.print(f" [bold green]# Clone berhasil!")
    except Exception as e:
        console.print(f" [bold red]# Gagal mengkloning {repo_url}: {e}")

def main(url: str) -> None:
    repositories = repo_list(url=url) 
    if repositories:
    	results = [] 
    for repository in repositories:
        nama_repo = repository.get('Repositories')
        url_repo = repository.get('Repositories Url')
        desc_repo = repository.get('Description')
        repo_file = repo_file_list(detail_url=url_repo)
        console.print(f"""
 [bold green]#[bold white] Repositories: [bold green]{nama_repo}[bold white]
 [bold green]#[bold white] Repositories Url: [bold green]{url_repo}[bold white]
 [bold green]#[bold white] Description: [bold green]{desc_repo}[bold white]""")
        file_repo = console.print(f" [bold green]#[bold white] File:[bold green] {', '.join(repo_file)}") if repo_file else None
        results.append({
            'Repositories': nama_repo,
            'Url': url_repo,
            'Description': desc_repo,
            'File': file_repo,
        })
        clone_choice = console.input(f" [bold green]#[bold white] Apakah Anda ingin mengkloning {nama_repo}? (y/n): ").lower()
        if clone_choice == 'y':
        	clone_repository(url_repo, f"./Peyimpanan/{nama_repo.split(' ')[0]}")
        
    df = pd.DataFrame(results)
    df.to_csv('repository.csv', index=False)
    exit()
        
if __name__ == '__main__':
    os.system('clear')
    github = console.input(' [bold green]#[bold white] masukan username github: ')
    main(url='https://github.com/{}?tab=repositories'.format(github))