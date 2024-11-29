import json
import requests
import threading
from bs4 import BeautifulSoup
import queue

q = queue.Queue()
q.put("Barack_Obama")


def doer(q, a):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={a}&format=json"
    r = requests.get(url)
    data = r.json()["parse"]["text"]["*"]
    soup = BeautifulSoup(data, features="html.parser")
    soup = soup.find_all("a")
    l = list(
        set(
            [
                i.get("href")[6:]
                for i in soup
                if i.get("href")
                and i.get("href").startswith("/wiki/")
                and "File" not in i.get("href")
                and ":" not in i.get("href")
            ]
        )
    )
    d = {a: l}
    with open("obama.json", "a") as f:
        f.write(json.dumps(d) + "\n")
        f.close()
    for i in l:
        q.put(i)


doer(q, q.get())

for j in range(5):
    a = q.get()
    doer(q, a)



print(q.qsize())
