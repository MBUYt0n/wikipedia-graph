import json
import bs4 as bs

with open("obama.json") as f:
    data = json.load(f)

a = data["parse"]["text"]["*"]
# print(a.keys())
soup = bs.BeautifulSoup(a, "html")
soup = soup.find_all("a")
l = []
for i in soup:
    j = i.get("href")
    if j and j.startswith("/wiki/") and "File" not in j:
        l.append(j[6:])

l = sorted(list(set(l)))
with open("obama.txt", "w") as f:
    for i in l:
        f.write(i + "\n")
