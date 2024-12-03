import json
import requests
import threading
from bs4 import BeautifulSoup
import queue
import h5py

q = queue.Queue()
q.put("1988_Democratic_Party_presidential_primaries")


def doer(q, a):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={a}&format=json"
    r = requests.get(url)
    try:
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
        # with h5py.File("obama.h5", "a") as f:
        #     f.create_dataset(a, data=l)
        #     f.close()
            
        for i in l:
            q.put(i)
    except:
        print(a)


doer(q, q.get())
for i in range(70):
    print(i)
    doer(q, q.get())

print(q.qsize())
