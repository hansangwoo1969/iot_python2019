'''

 1] KRX 30015 크롤링하고,
 2] 엑셀파일로 저장하고,
 2] DB에 저장하기.
 3] version 20181224 한상우

'''


import pyodbc
import time
import sqlite3 as sq
import requests
import numpy as np
import pandas as pd
from io import BytesIO

'''
=============================================================
             KRX_30015 일별 종목별 거래현황 ///  조회후 엑셀저장
=============================================================
'''

def krx_daily_trading(p_tdate):

    tdate = p_tdate

    gen_req_url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx"
    query_str_parms = {
        'name': 'fileDown',
        'filetype': 'xls',
        'url': 'MKD/04/0404/04040200/mkd04040200_01',
        'market_gubun': 'ALL',
        'sect_tp_cd': 'ALL',
        'schdate': str(tdate),
        'pagePath': '/contents/MKD/04/0404/04040200/MKD04040200.jsp'
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

    df = pd.read_excel(BytesIO(r.content), thousands=',')
    df['일자'] = tdate
 
    file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
    file_name = 'KRX_30015_' + str(tdate) + '.xlsx'

    # 엑셀로 저장
    df.to_excel(file_dir + file_name, index=False, index_label=None)  # 인덱스 배제된 저장
    print('KRX_30015_일자별 전종목 거래현황_크롤링 완료', tdate)

    return df

# krx_daily_trading(20181226)

DATABASE = 'C:\\Users\\hansangwoo2\\Documents\\blog\\KRXDB.db'

def krx_daily2DB(p_tdate):
    # tdate = 20180104
    tdate = p_tdate

    file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
    file_name = 'KRX_30015_' + str(tdate) + '.xlsx'

    file_exist = 'Q'

    df = pd.DataFrame()

    try:
        df = pd.read_excel(file_dir + file_name)
        file_exist = 'Y'
    except FileNotFoundError:
        df = pd.DataFrame()
        file_exist = 'N'

    finally:
        if file_exist == 'Y':

            # conn = sq.connect(DATABASE)

            insert_query = (
                """
                INSERT INTO KRX_30015_DAYILY(
                         [일자],     [종목코드],      [종목명],   [현재가],
                         [대비],     [등락률],        [거래량],   [거래대금],
                         [시가],     [고가],          [저가],     [시가총액],
                         [시가총액비중], [상장주식수], [외국인보유주식수], [외국인지분율], 
                         [IPUSER], [IPDATE])
            
                VALUES   (?,       ?,     ?,      ?,
                          ?,       ?,     ?,      ?,
                          ?,       ?,     ?,      ?,
                          ?,       ?,     ?,      ?,
                          '한상우', DATE())
                """)

            df['일자'] = df['일자'].astype(str)

            # cur = conn.cursor()

            # 정수형 모양을 float형 변환(엑셀에서 자료를 가져오지 못하는 문제 해결)
            float_list = [
                        '현재가', '대비', '거래량', '거래대금',
                        '시가', '고가', '저가', '시가총액',
                        '상장주식수', '외국인 보유주식수'
                        ]
            for f in range(len(float_list)):
                float_col = float_list[f]
                df[float_col] = df[float_col].astype(float)

            # cur = conn.cursor()
            conn = sq.connect(DATABASE)
            cur = conn.cursor()
            for i in range(len(df)):

                # 일자 = df['일자'][i]
                # 종목코드 = df['종목코드'][i]
                # 종목명 = df['종목명'][i]
                # 현재가 = df['현재가'][i]
                # 대비 = df['대비'][i]
                # 등락률 = df['등락률'][i]
                # 거래량 = df['거래량'][i]
                # 거래대금 = df['거래대금'][i]
                # 시가 = df['시가'][i]
                # 고가 = df['고가'][i]
                # 저가 = df['저가'][i]
                # 시가총액 = df['시가총액'][i]
                # 시가총액비중 = df['시가총액비중(%)'][i]
                # 상장주식수 = df['상장주식수'][i]
                # 외국인보유주식수 = df['외국인 보유주식수'][i]
                # 외국인지분율 = df['외국인 지분율(%)'][i]

                parms_value = [
                    df['일자'][i],    df['종목코드'][i],       df['종목명'][i],     df['현재가'][i],
                    df['대비'][i],    df['등락률'][i],         df['거래량'][i],     df['거래대금'][i],
                    df['시가'][i],    df['고가'][i],           df['저가'][i],      df['시가총액'][i],
                    df['시가총액비중(%)'][i],    df['상장주식수'][i],    df['외국인 보유주식수'][i], df['외국인 지분율(%)'][i]
                ]

                # conn = sq.connect(DATABASE)
                # cur = conn.cursor()
                cur.execute(insert_query, parms_value)
                conn.commit()

                # if i % 200 == 0:
                #     print(i)

            conn.close()
        print('KRX_30015_일자별 전종목 거래현황_DB저장 완료', tdate)

    return


for year in range(2018, 2019):
    for month in range(1,13):
        for day in range(1,32):
            tdate = year*10000 + month*100 + day*1   # yymmdd

            #print(tdate,'성공')
            if tdate <= 20180104 :
                krx_daily_trading(tdate)
                krx_daily2DB(tdate)





