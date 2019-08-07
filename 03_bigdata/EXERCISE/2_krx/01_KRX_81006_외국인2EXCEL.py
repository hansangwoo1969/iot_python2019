'''

1] KRX에서 자료(81006_외국인보유량) 조회,
2] 엑셀파일로 저장하기..
3] version 20181226 한상우

'''

import pyodbc
import time
import requests
import numpy as np
import pandas as pd
from io import BytesIO

def krx_foreign_holding(p_tdate):

    tdate = p_tdate

    gen_req_url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx"
    query_str_parms = {
        'name': 'fileDown',
        'filetype': 'xls',
        'url': 'MKD/13/1302/13020402/mkd13020402',
        'market_gubun': 'ALL',
        'lmt_tp': '1',
        'sect_tp_cd': 'ALL',
        'schdate': str(tdate),
        'pagePath': '/contents/MKD/13/1302/13020402/MKD13020402.jsp'

    }

    r = requests.get(gen_req_url, query_str_parms)
    time.sleep(2.0)

    gen_req_url = "http://file.krx.co.kr/download.jspx"

    headers = {
        'Referer': 'http://marketdata.krx.co.kr/mdi'
    }
    form_data = {
        'code': r.content
    }

    r = requests.post(gen_req_url, form_data, headers=headers)
    time.sleep(2.0)

    df = pd.read_excel(BytesIO(r.content))
    df['거래일자'] = tdate                                       # 거래일자 column추가

    file_dir = './krx/'
    file_name = 'KRX_81006_' + str(tdate) + '.xlsx'

    df.to_excel(file_dir + file_name, index=False, index_label=None)  # 인덱스 배제된 저장

    print('KRX_81006_외국인 보유량_크롤링 완료', tdate)

    return

for year in range(2019, 2020):
    for month in range(1,13):
        for day in range(1,32):
            tdate = year*10000 + month*100 + day*1   # yymmdd

            if tdate <= 20190105 :
                krx_foreign_holding(tdate)




