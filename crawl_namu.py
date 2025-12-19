import requests
import re

KEYWORDS = ["김정은", "북한", "핵"]
HEADERS = {"User-Agent": "Mozilla/5.0"}

out = open("namu.txt", "w", encoding="utf-8")

for kw in KEYWORDS:
    url = f"https://namu.wiki/w/{kw}"
    html = requests.get(url, headers=HEADERS).text
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    out.write(kw + " " + text[:3000] + "\n")

out.close()
print("namu done")
