#!/usr/bin/env python

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/#countries'
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

r = requests.get(url, headers=header)

# fix HTML multiple tbody
soup = BeautifulSoup(r.text, "html.parser")
for body in soup("tbody"):
    body.unwrap()

df = pd.read_html(str(soup), index_col=1, thousands=r',', flavor="bs4")[0]
df = df.replace(regex=[r'\+', r'\,'], value='')

df = df.fillna('0')
df = df.to_json(orient='index')

print(df)