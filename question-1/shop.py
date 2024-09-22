import requests
from bs4 import BeautifulSoup


def scrape_cnn_articles():
    url = "https://www.cnn.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")  # Print status code

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response.text[:500])
        articles = soup.find_all('a')

        for article in articles:
            title = article.get_text(strip=True)
            link = article.get('href')
            if title and link:
                if link.startswith('/'):
                    link = f'https://www.cnn.com{link}'
                print(f'Title: {title}\nURL: {link}\n')
    else:
        print(f"Failed to retrieve articles. Status code: {response.status_code}")


if __name__ == "__main__":
    scrape_cnn_articles()