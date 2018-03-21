import urllib.request
import json
import numpy as np
import pandas as pd
from classCompanyInfo import Company

#from ファイル名 import クラス名
#from ファイル名.クラス名 import 関数名（引数なし）

from G_Sheet import gsheet



class Row:
    def __init__(self, id, url, status,companyName, establishedIn, capital, ceo):
        self.id = id
        self.url = url
        self.status = status
        self.companyName = companyName
        self.establishedIn = establishedIn
        self.capital = capital
        self.ceo = ceo
        
    def __repr__(self) :
        return repr((self.id, self.url, self.status, self.companyName, self.establishedIn, self.capital, self.ceo))

def load_urls():
    gsheet_a = gsheet() 
    file = gsheet_a.readSheet()
    table = []
    for a in file :
        # print(a)
        row = Row(a["id"], a["url"], a["status"], a["companyName"], a["establishedIn"], a["capital"], a["ceo"])
        table.append(row)
    return table

def define_unchecked_row(all_data) :
    """
    args: Array<row>
    return 更新した行
    Rowインスタンスの中からステータスが未実行の物の、スコアを取得する
    """
    updated_rows = []
    for row in all_data :
        if row.status == "" :
            print("crowling company info from..." + row.url)
            company1 = Company()
            company1.get_html_from_url(row.url)    # ここで内部でhtmlデータを持つ
            row.campanyName = company1.get_companyName()
            row.establishedIn = company1.get_establishedIn()
            row.capital = company1.get_capital()
            row.ceo = company1.get_ceo()
            updated_rows.append(row)
    return updated_rows



gsheet_b = gsheet()  
  
urls = load_urls()

updated_urls = define_unchecked_row(urls)
gsheet_b.override_score(updated_urls)

# print(updated_urls)








