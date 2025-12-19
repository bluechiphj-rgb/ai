import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ["김정은", "북한", "핵", "제재"]

out = open("wiki.txt", "w", encoding="utf-8")

for kw in KEYWORDS:
    url = f"https://ko.wikipedia.org/wiki/{kw}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    out.write(kw + " " + text[:3000] + "\n")

out.close()
print("wiki done")
