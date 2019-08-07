'''

1] DATABASE에서 자료 조회,
2] 엑셀파일로 저장하기..
3] version 20181223 한상우

'''


# -*- coding: utf-8 -*-
import os, glob, sys, getopt
from pytz import timezone, utc

import re
import calendar

import datetime, time
from datetime import timedelta
import urllib.request
import requests, json
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as pdsql
from matplotlib import dates
from io import BytesIO

import sqlite3 as sq

import logging
import logging.handlers

"""
=======================================================================
            *** DB에서 자료 조회하기 ***
=======================================================================
"""
# DATABASE = 'C:\\Users\\hansangwoo2\\Documents\\blog\\KRXDB.db'
DATABASE = 'C:\\Users\\hansangwoo2\\Documents\\mymoneybotEbest\\DATA\\mymoneybot.sqlite'

conn = sq.connect(DATABASE)
cur = conn.cursor()

get_query1 = """
    SELECT [일자],[단축코드],[종가],[누적거래량],[기관],[외인계],[개인]
    FROM [종목별투자자]
    WHERE [일자] = '20181221'
    """

get_query2 = """
    SELECT [날짜],[종목명],[종목코드],[매출액],[영업이익],[PER],[PBR],[DPS],[배당수익률]
        FROM [재무정보]
             INNER JOIN [종목코드]
             ON [종목코드] = [단축코드]
        WHERE [날짜] = '2018-12-31' AND [기간구분]= '년간'
        ORDER BY [배당수익률]  DESC LIMIT 200
    """

get_query3 = """
    SELECT [종목코드],[종목명],MAX([종가]) AS 'MAX',MIN([종가]) AS 'min'
         FROM [일별주가]
             INNER JOIN [종목코드]
             ON [종목코드] = [단축코드]
         WHERE [날짜] >= '2017-12-31'
         GROUP BY [종목명]
    """
get_query4 = """
    SELECT [종목코드],[종목명],[종가]
         FROM [일별주가]
             INNER JOIN [종목코드]
             ON [종목코드] = [단축코드]
         WHERE [날짜] = '20190426'
         GROUP BY [종목명]
    """


# 조회할 쿼리 선택
df = pd.read_sql(get_query2, conn)

conn.commit()
print(df)
conn.close()


"""
=======================================================================
            *** 조회한 자료 엑셀파일로 저장하기 ***
=======================================================================
"""
# 특정장소에 파일 저장
to_day = datetime.datetime.now()
todate = to_day.strftime('%Y%m%d')  # 오늘 날짜
file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
# file_name = '종목별_투자자_' + todate + '.xlsx'
# file_name = 'MAX_min_' + todate + '.xlsx'
file_name = 'MAX_min_1' + todate + 'FIN' + '.xlsx'
df.to_excel(file_dir + file_name, index=False, index_label=None)  # 인덱스 배제된 저장

print('데이터베이스 읽어 엑셀로 저장 성공')

















#
# def sqliteconn():
#     conn = sqlite3.connect(DATABASE)
#     return conn
#
#
# def get_webpage(url, encoding=""):
#     cj = CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     opener.addheaders = [('User-agent',
#                           'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95  Safari/537.36')]
#
#     respstr = ""
#     try:
#         op = opener.open(url)
#         sourcecode = op.read()
#     except Exception as e:
#         time.sleep(1)
#         op = opener.open(url)
#         sourcecode = op.read()
#
#     encodingmethod = op.info().get_param('charset')
#     if encodingmethod == None:
#         if encoding != "":
#             encodingmethod = encoding
#
#     if encoding != "":
#         encodingmethod = encoding
#
#     try:
#         respstr = sourcecode.decode(encoding=encodingmethod, errors='ignore')
#     except Exception as e:
#         respstr = sourcecode.decode(encoding="cp949", errors='ignore')
#
#     opener.close()
#
#     return respstr
#
#
# def get_company_report_fnguide(시작일='20170101', 종료일='20181017'):
#     url = "http://comp.fnguide.com/SVO2/asp/SVD_Report_Summary_Data.asp?fr_dt=%s&to_dt=%s&stext=&check=all&sortOrd=5&sortAD=A&_=2" % (
#     시작일, 종료일)
#     respstr = get_webpage(url, encoding="utf8")
#
#     # soup = BeautifulSoup(respstr)
#     soup = BeautifulSoup(respstr, "lxml")
#
#     result = []
#     for i in soup.find_all('tr'):
#         arry = i.find_all("td")
#         날짜 = arry[0].text.strip().replace('/', '-')
#
#         line1 = arry[1].text.strip().replace('\n', ' ')
#         종목명 = line1.split(' ')[0]
#         코드 = line1.split(' ')[1].replace('A', '')
#         if len(코드) < 6:
#             종목명 = '%s %s' % (종목명, 코드)
#             코드 = line1.split(' ')[2].replace('A', '')
#         if len(코드) < 6:
#             종목명 = '%s %s' % (종목명, 코드)
#             코드 = line1.split(' ')[3].replace('A', '')
#
#         line131 = line1.split(' ')[2:]
#         추천사유 = (' '.join(line131)).strip()
#         의견 = arry[2].text.strip()
#         try:
#             목표가 = int(arry[3].text.strip().replace(',', ''))
#         except Exception as e:
#             목표가 = 0
#         try:
#             추천일가격 = arry[4].text.strip().replace(',', '')
#         except Exception as e:
#             추천일가격 = 0
#
#         line51 = arry[5].text.strip()[:-3]
#         line52 = arry[5].text.strip()[-3:]
#         추천증권사 = "%s %s" % (line51, line52)
#
#         result.append([날짜, 코드, 종목명, 의견, 목표가, 추천일가격, 추천증권사, 추천사유])
#
#     df = DataFrame(data=result, columns=['날짜', '코드', '종목명', '의견', '목표가', '추천일가격', '추천증권사', '추천사유'])
#     df.set_index('날짜', inplace=True)
#
#     return df
#
#
# def build_broker_report(시작일='20170701', 종료일='20181017'):
#     df = get_company_report_fnguide(시작일=시작일, 종료일=종료일)
#     df.reset_index(inplace=True)
#     # print(df)
#     values = df.values
#     # print(values)
#
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.executemany("replace into 증권사추천주(일자,종목코드,종목명,의견,목표가,추천일가격,추천증권사,추천사유) values(?, ?, ?, ?, ?, ?, ?, ?)",
#                            df.values.tolist())
#         conn.commit()
#
#
# def time_print(start, middle, end):
#     print("[{}] 걸린시간 : {} 전체걸린시간 : {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), end - middle,
#                                               end - start))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     middle = time.time()
#
#     # print(sys.argv)
#
#     # help = "usage: {} 시작일[20150101] 종료일[20150131]".format(sys.argv[0])
#
#     # if len(sys.argv) < 3:
#     # print (help)
#     # sys.exit(2)
#
#     if len(sys.argv) == 1:
#         시작일 = "{:%Y%m}01".format(datetime.datetime.now())
#         종료일 = "{:%Y%m%d}".format(datetime.datetime.now())
#     if len(sys.argv) == 2:
#         시작일 = sys.argv[1]
#         종료일 = "{:%Y%m%d}".format(datetime.datetime.now())
#     if len(sys.argv) == 3:
#         시작일 = sys.argv[1]
#         종료일 = sys.argv[2]
#
#     build_broker_report(시작일=시작일, 종료일=종료일)
#
#     # ---------------------------------------------------
#     #
#     # year = ['2013', '2014', '2015']
#     # month = ['{:02d}'.format(x) for x in range(1,13)]
#     # for y in year:
#     #     for m in month:
#     #         print('%s년 %s월' %(y, m))
#     #         build_broker_report(시작일=y+m+'01', 종료일=y+m+'31')
#     #
#     # print("완료")
#
#     # ---------------------------------------------------
#     #
#     # build_broker_report(시작일='20151201', 종료일='20151212')
#
#     end = time.time()
#     time_print(start, middle, end)
