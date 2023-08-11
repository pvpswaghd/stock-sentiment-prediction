import yfinance as yf
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
import random

chrome_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
cheader = {"User-Agent":chrome_agent}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

def js_requests(url, *args):
    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(20.0 + random.random())
    if len(args) != 0:
        driver.switch_to.frame(args[0])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrape(url, samples=5):
    # url of articles
    urls = []
    # 2d array of [[title, article], ...]
    res = []
    url = "https://www.reuters.com/site-search/?query=" + url
    soup = js_requests(url)

    links = soup.find_all('a', class_="text__text__1FZLe text__dark-grey__3Ml43 text__inherit-font__1Y8w3 text__inherit-size__1DZJi link__underline_on_hover__2zGL4 media-story-card__heading__eqhp9")
    for link in links:
        try:
            href = link.get('href')
            if href: urls.append(urljoin(url, href))
        except:
            continue

    # Randomly select 5 articles as samples
    chosen = []
    for i in range(samples):
        if len(urls) <= i: break
        luckyNumber = random.randint(0, len(urls) - 1)
        while luckyNumber in chosen: luckyNumber = random.randint(0, len(urls) - 1)
        newUrl = urls[i]
        time.sleep(2.0 + random.random())
        newSoup = js_requests(newUrl)
        # Scrape the article page
        try:
            title = newSoup.find('h1')
            article = ""
            for p in newSoup.find_all('p', class_="text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__small__1kGq2 body__full_width__ekUdw body__small_body__2vQyf article-body__paragraph__2-BtD"):
                article += p.text
            res.append([title.text, article])
        except:
            i -= 1
            continue

    return res

# res = scrape("tesla", 5)
# for i in res:
#     print("Topic:")
#     print(i[0])
#     print("Article: ")
#     for j in i[1].split(". "): print(j)
#     print()
