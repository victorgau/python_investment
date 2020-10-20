# 一些pandas的補充資料

因為.ipynb的檔案有時候在GitHub上面無法載入，所以我把部分內容移到.md檔上面，使用上比較方便。

## pandas資料匯入練習

使用pandas.read_csv()匯入底下資料：

* [上市公司基本資料](https://data.gov.tw/dataset/18419)
  * [CSV資料網址](https://dts.twse.com.tw/opendata/t187ap03_L.csv)
* NASDAQ公司列表 (底下為相關連結)
  * http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs
  * ftp://ftp.nasdaqtrader.com/symboldirectory/
  * https://stackoverflow.com/questions/25338608/download-all-stock-symbol-list-of-a-market
  * https://quant.stackexchange.com/questions/1640/where-to-download-list-of-all-common-stocks-traded-on-nyse-nasdaq-and-amex
  * ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt

使用pandas.read_html()匯入底下資料：

* https://www.pmi.org.tw/?p=5361
* [讀取S&P500公司資料](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)

使用pandas.read_json()匯入底下資料：

* [元大投信](https://www.yuantafunds.com/)
  * [0050成分股](http://www.yuantaetfs.com/api/StkWeights?date=&fundid=1066)

使用pandas.read_excel()匯入底下資料：

* [政府開放資料 - 國發會 景氣指標及燈號](https://www.ndc.gov.tw/News_Content.aspx?n=9D32B61B1E56E558&sms=9D3CAFD318C60877&s=C367F13BF38C5711)

## requests讀取資料練習

* 讀取NYSE公司列表
  * https://www.nyse.com/api/quotes/filter

## 其他網址：

* [開放資料-每月國內主要金融指標](https://data.gov.tw/dataset/30815)
* [開放資料-年度國內主要金融指標](https://data.gov.tw/dataset/130490)
