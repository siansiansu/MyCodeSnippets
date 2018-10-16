import pandas as pd
import json
import urllib.parse
import pandas as pd
from pandas.io.json import json_normalize
from bson import json_util
from urllib.request import urlopen

START_DATE = "2014-01-01"
END_DATE = "2018-10-16"
DATE_RANGE = pd.date_range(START_DATE, END_DATE).tolist()
DATE_RANGE = [i.strftime("%Y-%m-%d") for i in DATE_RANGE]

def getData(date):
    yy = date[0:4] 
    mm = date[5:7]
    dd = date[8:10]
    print(yy, mm, dd)
    target_url = "http://data.coa.gov.tw/Service/OpenData/TraceBeefData.aspx?$skip=0&$filter=SlaughterDate+like+{}%2f{}%2f{}".format(yy,mm,dd)
    res = urlopen(target_url)
    con = res.read().decode(res.headers.get_content_charset())
    raw = json.loads(con)
    df = json_normalize(raw)
    return df

def main():
    out = pd.DataFrame()
    for i in DATE_RANGE:
        try:
            df = getData(i)
        except:
            df = pd.DataFrame()
        out = pd.concat([out, df]) 
    out.to_csv("TraceBeefData.csv". index=False)

if __name__ == "__main__":
    main()
