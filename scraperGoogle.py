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
    time.sleep(10.0 + random.random())
    if len(args) != 0:
        driver.switch_to.frame(args[0])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrape(query, samples=5, start="2020-01-01", end="2020-01-02"):
    # names of webpages
    names = []
    # 2d array of [[title, article], ...]
    res = []
    start, end = start.split("-"), end.split("-")
    start = [start[1], start[2], start[0]]
    end = [end[1], end[2], end[0]]
    url = "https://www.google.com/search?client=safari&sca_esv=555929706&rls=en&tbs=cdr:1,cd_min:" + "/".join(start) + ",cd_max:" + "/".join(end) + "&q=" + \
        "+".join(query.split(" ")) + "&tbm=nws&source=lnms&sa=X&ved=2ahUKEwiP77OD89SAAxVSpVYBHYCKD9kQ0pQJegQIDBAB&biw=1373&bih=603&dpr=2"
    print(url)
    soup = js_requests(url)

    links = soup.find_all('div', class_="n0jPhd ynAwRc MBeuO nDgy9d")
    for link in links:
        try:
            if link.text: names.append(link.text)
        except:
            continue

    # Randomly select 5 articles as samples
    chosen = []
    for i in range(samples):
        if len(names) <= i: break
        luckyNumber = random.randint(0, len(names) - 1)
        while luckyNumber in chosen: luckyNumber = random.randint(0, len(names) - 1)
        res.append(names[i])
        chosen.append(luckyNumber)
    return res

# res = scrape("tesla stock news", 10, "2020-01-01", "2020-01-02")
# for i in res:
#     print(i)
