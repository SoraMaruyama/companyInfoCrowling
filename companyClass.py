"""
＜クラスの考え方のサンプル＞
- googleからurl取って来る  *) G_sheet　ー＞ 対象がGシートで共通だったから１クラス
- googleに結果書き込み     *) G_sheet
- urlのスコア計算   *) やることが一つなのでクラスを作らなかった気がする
-----------------
- URLからhtmlを取って来る
- htmlから情報を抜き取る（社名、創立。。。。）
  -> url/html/社名/創立　..... -> データが共通してるから１クラスにしようかなぁ。。。
"""

import urllib.request
import bs4
import re

class Company:
    
    def __init__(self):
        self.html = ""
    
    def get_html_from_url(self, url):
        response = urllib.request.urlopen(url)
        preHtml = response.read() # ここでhtmlをとる
        soup = bs4.BeautifulSoup(preHtml, "html.parser")
        self.html = soup.get_text()
        print(self.html)
        #soup = bs4.BeautifulSoup(html, "html.parser")
        #print(soup.get_text())
    
    def get_companyName(self):
        companyName = re.search("[名称|会社名|商号|社名]\s*(\S*)\s*(\S*)", self.html)
        if companyName == None :
            print("Comapny Name: no data found")
        else :
            print("Company Name:" + companyName[0])
            return companyName[0]
        
    def get_capital(self):
        capital = re.search("[資本金|資本]\s*([0-9,]*)[万円|億円]([0-9,]*)[万円|億円]", self.html)
        if capital == None :
            print("Capital:no data found")
        else :
            print("capital:" + capital[0])
            return capital[0]
        
    def get_ceo(self):
        ceo = re.search("[代表|社長|代表者]\s*(\S*)\s*(\S*)（", self.html)
        if ceo == None :
            print("CEO: no data found")
        else :
            print("CEO:" + ceo[0])
            return ceo[0]
    
    def get_establishedIn(self):
        # shimada memo:  もしかしたら
        # pattern = re.search("[創立|設立]\s*([0-9]{4})[年|/]([0-9]*)月", self.html)
        # pattern2 = re.search("[設立\s*昭和|設立\s*平成|設立\s*大正]\s*([0-9]*)[年|/]([0-9]*)月", self.html)
        # pattern3 = re.search("[創立\s*昭和|創立\s*平成|創立\s*大正]\s*([0-9]*)[年|/]([0-9]*)月", self.html)
        
        # result = pattern[0] or pattern2[0] or pattern3[0]
        # return result 
        # memo ここまで

        establishedIn = re.search("[創立|設立]\s*([0-9]{4})[年|/]([0-9]*)月", self.html)
        if establishedIn == None :
            establishedIn = re.search("[設立\s*昭和|設立\s*平成|設立\s*大正]\s*([0-9]*)[年|/]([0-9]*)月", self.html)
            if establishedIn == None :
                establishedIn = re.search("[創立\s*昭和|創立\s*平成|創立\s*大正]\s*([0-9]*)[年|/]([0-9]*)月", self.html)
                if establishedIn == None :
                    print("Established In: no data found")
        
        else :
            print("Established In:" + establishedIn[0])
            return establishedIn[0]
        


# company1 = Company()
# company1.get_html_from_url('http://recruit.yoga-lava.com/about/company/')
# company1.get_capital()
# company1.get_companyName()
# company1.get_ceo()
# company1.get_establishedIn()