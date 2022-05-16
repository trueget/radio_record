import requests
from bs4 import BeautifulSoup
import pandas as pd

q = []
url = 'https://www.radiorecord.ru/stations?style=ALL'
r = requests.get(url)
s = BeautifulSoup(r.text, 'lxml')
vse = s.findAll('div', class_='_2QTSTI_2ZTb-y1W_Hq-QXj')

for v in vse:
    radio = 'https://www.radiorecord.ru' + v.find('a', class_='_3EL46XmHpWHxC9oIt5vmTx').get('href')
    name = v.find('a', class_='l5TqoasmC1AEhB1RTABm8').text
    fo1 = v.find('img', class_='_35nqQjq2BYYHo1i2MA6ctF').get('src')
    fo2 = v.find('img', class_='_13V-Bh1pEEvB21wQJOJvRo').get('src')
    q.append([name,radio,fo1,fo2])
h = ['Имя радиостанции','Сылочка на станцию','Картинка 1','Картинка 2']
d = pd.DataFrame(q, columns=h)
d.to_csv('radio.csv', sep=';', encoding='utf8')