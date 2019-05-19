from bs4 import BeautifulSoup
import requests
import csv

with open('data.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['序号', '代码', '名称', '营业收入', '同比增长', '净利润', '同比增长', '基本每股收益',	'每股净资产', '净资产收益率', '公告日期'])

    for i in range(0, 78):
        url = 'http://quotes.money.163.com/data/caibao/yjsd_ALL.html?reportdate=20181231&sort=declaredate&order=desc&page=' + str(i)
        req = requests.get(url)
        html = req.text

        bf = BeautifulSoup(html, 'lxml')
        trs = bf.find_all('tr')

        for j in range(len(trs)):
            if j == 0: continue
            tr_data = []
            for td in trs[j].select('td'):
                tr_data.append("".join(td.get_text().split()))
            writer.writerow(tr_data)
