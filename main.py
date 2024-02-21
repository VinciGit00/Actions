import time
import requests

header = {
    'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/97.0.4692.71 safari/537.36'
}

urls = ["https://scrapegraph-ai-demo.streamlit.app/", "https://vincigit00-nba-platform-main-ounnit.streamlit.app/", "https://vincigit00-amazon-scraping-app-nfzu99.streamlit.app/"]

for i in range(0,10):
    print(f"iteration: {i+1}")
    for url in urls:
        r = requests.get(url, headers=header)
        print(f"status code for the website: {url} - {r.status_code}")
        time.sleep(20)