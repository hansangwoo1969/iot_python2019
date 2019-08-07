'''

1] KRX 30030 일별종목별거래현황 자료 수집,
2] 엑셀파일로 저장하기..
3] 엑셀파일을 DB에 저장,,
4] version 20181226 한상우

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

import sqlite3 as sq

import logging
import logging.handlers


import pyodbc
import requests
import numpy as np
import pandas as pd
from io import BytesIO

'''
========================================================================================================================
                                        01_KRX_30030_상장종목현황
------------------------------------------------------------------------------------------------------------------------
[목적]
    1. 주식 종목 일자별 가격 데이터 크롤링
        ㅁ 크롤링 사이트: http://marketdata.krx.co.kr/mdi#document=040602

        ㅁ 크롤링 시계열
            ㅇ 소급적용: 2001.01.02-2018.08.31
            ㅇ 일별작업: 2018.09.01-

[내용]
    1. 주식 종목 일자별 가격 데이터를 XLSX 파일에 저장하고, SQL Table에 적재한다.
        ㅁ 사용 함수
            ㅇ krx_30030(p_tdate, p_mktidx)
                - 해당날짜에 해당시장에 속한 모든 주식의 일자별 가격, 수익률 데이터를 DataFrame 형태로 크롤링 한다.

            ㅇ krx_30030_to_excel(p_tdate)
                - krx_30030을 통해 크롤링한 DataFrame을 'KRX_30030_yyyyMMdd.xlsx'의 엑셀파일로 저장한다.

            ㅇ krx_30030_excel_to_sql(p_tdate)
                - krx_30030_to_excel을 통해 저장한 엑셀파일을 SQL Server Table 'KSDB.dbo.st_KRX_30030'에 삽입한다.

[저장]
    1. 엑셀파일
        ㅁ 저장형식
            ㅇ 디렉토리: 'C://Users//hansangwoo2//Desktop//TEST//'
            ㅇ 파일이름: 'KRX_30030_' + str(tdate) + '.xlsx'

    2. SQL테이블
        ㅁ 저장형식
            ㅇ 테이블명: 'KRX_30030'

'''

'''
====================================
 KRX 사이트 크롤링 함수    
====================================
'''

DATABASE = 'C:\\Users\\hansangwoo2\\Documents\\blog\\KRXDB.db'

def krx_30030(p_tdate, p_mktidx):
    # Parameters Settings
    schdate = p_tdate
    mktidx = p_mktidx

    if mktidx == 1:
        market_gubun = 'STK'  # KOSPI
        indx_ind_cd = '1001'  # 코스피지수

    elif mktidx == 2:
        market_gubun = 'KSQ'  # KOSDAQ
        indx_ind_cd = '2001'  # 코스닥지수

    elif mktidx == 3:
        market_gubun = 'KNX'  # KONEX
        indx_ind_cd = 'N001'  # 코넥스지수

    else:  # p_mktidx == 9:
        market_gubun = 'ALL'  # 전체
        indx_ind_cd = ''      # 전체

    # Requests
    gen_req_url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'
    query_str_parms = {
        'name': 'fileDown',
        'filetype': 'xls',
        'url': 'MKD/04/0406/04060200/mkd04060200',
        'market_gubun': str(market_gubun),  # 시장구분: [KOSPI, 'STK'], [KOSDAQ, 'KSQ'], [KONEX, 'KNX'], [전체, 'ALL']
        'indx_ind_cd': str(indx_ind_cd),    # 업종구분: [코스피, '1001'], [코스닥, '2001'], [코넥스, 'N001'], [전체, '']
        'sect_tp_cd': 'ALL',
        'isu_cdnm': '전체',
        'isu_cd': '',
        'isu_nm': '',
        'isu_srt_cd': '',
        'secugrp': 'ST',
        'stock_gubun': 'on',      # 종류: [보통주, '0'], [우선주, '9'], [전체, 'on']
        'schdate': str(schdate),  # 조회일자: YYYYMMDD
        'pagePath': '/contents/MKD/04/0406/04060200/MKD04060200.jsp'
    }
    r = requests.get(gen_req_url, query_str_parms)

    gen_req_url = 'http://file.krx.co.kr/download.jspx'

    headers = {
        'Referer': 'http://marketdata.krx.co.kr/mdi'
    }

    form_data = {
        'code': r.content
    }
    r = requests.post(gen_req_url, form_data, headers=headers)

    # DataFrame 크롤링한 자료를 데이터프레임으로,,,
    df = pd.read_excel(BytesIO(r.content), thousands=',',
                       converters={'종목코드': str})  # 000245를 245로 읽게되는 경우 방지

    # 이름 바꾸기 (한글에서 영어로,,)
    df = df.rename(
        {
            '종목코드': 'code',
            '종목명': 'name',
            '현재가': 'cprc',
            '대비': 'cng',
            '등락률(%)': 'rtn',
            '매수호가': 'bquote',
            '매도호가': 'squote',
            '거래량(주)': 'trdvol',
            '거래대금(원)': 'trdval',
            '시가': 'oprc',
            '고가': 'hprc',
            '저가': 'lprc',
            '액면가': 'faceval',
            '통화구분': 'cunit',
            '상장주식수(주)': 'snum',
            '상장시가총액(원)': 'mktcap'
        }, axis='columns'
    )

    # df['code'] = 'A' + df['code']  # A#####@, Short ISIN, A=주권, #####=발행회사, @=보통/우선주
    df['tdate'] = schdate          # 거래일자 열 추가
    df['mktidx'] = mktidx          # 시장구분 열 추가

    df['rtn'] = pd.to_numeric(df['rtn'], errors='coerce')  # KRX 자체 데이터 오류 NULL 처리
    df['cng'] = pd.to_numeric(df['cng'], errors='coerce')  # KRX 자체 데이터 오류 NULL 처리

    df = df.replace(np.NaN, 999999999)          # NaN 값 변환
    # df.loc[df['rtn'].isnull(), 'rtn'] = 9999  # coerce 로 인한 NaN 값 변환
    # df.loc[df['cng'].isnull(), 'cng'] = 9999  # coerce 로 인한 NaN 값 변환

    # 거래소 수익률은 다운로드 받으면 모두 (+)이기 때문에,,, df.loc[행인덱스,열인덱스]
    df.loc[(df.rtn > 0) & (df.cng < 0), 'rtn'] = -1.00 * df['rtn']  # 대비부호에 따라 수익률 부호를 조정해줌(망할...)

    # Re-order Columns,,,,  Column순서
    col_order = [
        'tdate', 'code', 'name', 'mktidx',
        'oprc', 'hprc', 'lprc', 'cprc',
        'cng', 'rtn', 'snum', 'mktcap',
        'bquote', 'squote', 'faceval', 'cunit'
    ]
    df = df.reindex(col_order, axis=1)

    return df


'''
====================================
 크롤링한 후 엑셀파일 저장 함수    
====================================
'''


def krx_30030_to_excel(p_tdate):
    tdate = p_tdate

    ksp = krx_30030(tdate, 1)
    ksq = krx_30030(tdate, 2)
    knx = krx_30030(tdate, 3)

    kor = [ksp, ksq, knx]
    df = pd.concat(kor)
    df.reset_index(drop=True, inplace=True)

    if len(df) >= 1:  # 데이터가 있는 경우

        file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
        file_name = 'KRX_30030_' + str(tdate) + '.xlsx'

        df.to_excel(file_dir + file_name,
                    index=False, index_label=None, encoding='utf-8-sig')
        print('KRX_30030_상장종목현황', '/', tdate, '/', 'EXCEL Done: Data O')
    else:
        print('KRX_30030_상장종목현황', '/', tdate, '/', 'EXCEL Done: Data X')
        pass

    return


'''
====================================
 EXCEL TO SQL 함수   
====================================
'''

def krx_30030_excel_to_sql(p_tdate):
    tdate = p_tdate

    file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
    file_name = 'KRX_30030_' + str(tdate) + '.xlsx'

    file_exist = 'Q'
    df = pd.DataFrame()

    try:
        df = pd.read_excel(file_dir + file_name)
        file_exist = 'Y'

    except FileNotFoundError:
        df = pd.DataFrame()
        file_exist = 'N'

    finally:

        if file_exist == 'Y':  # 해당일자 엑셀 파일이 있는 경우

            # SQL Connection
            conn = sq.connect(DATABASE)

            query_delete = '''
                                DELETE
                                FROM KRX_30030
                                WHERE TradeDay = ''' + "'" + str(tdate) + "'" + '''
                           '''

            query_insert = '''
                                INSERT INTO KRX_30030
                                            (TradeDay,      StockCode,  StockName,  MktIdx,
                                             OpenPrice,     HighPrice,  LowPrice,   ClosePrice,
                                             Cng,           Rtn,        StockNum,   MktCap,
                                             BQuote,        SQuote,     FaceValue,  CUnit,      
                                             IPUser,        IPDate )
                                VALUES      (?,             ?,          ?,          ?,          
                                             ?,             ?,          ?,          ?,          
                                             ?,             ?,          ?,          ?,
                                             ?,             ?,          ?,          ?,
                                             'swhan',      DATE());
                            '''

            # Type Changes
            df['tdate'] = df['tdate'].astype(str)    # 거래일자 변수 숫자형 -> 문자형
            df['mktidx'] = df['mktidx'].astype(str)  # 시장구분 변수 숫자형 -> 문자형

            float_list = [
                'oprc', 'hprc', 'lprc', 'cprc',
                'cng', 'rtn', 'snum', 'mktcap',
                'bquote', 'squote', 'faceval'
            ]
            for f in range(len(float_list)):
                float_col = float_list[f]
                df[float_col] = df[float_col].astype(float)

            # Cursor and Execute
            cur = conn.cursor()
            cur.execute(query_delete)  # 기존 데이터 삭제

            for r in range(len(df)):
                parms_value = [
                    df['tdate'][r], df['code'][r], df['name'][r], df['mktidx'][r],
                    df['oprc'][r], df['hprc'][r], df['lprc'][r], df['cprc'][r],
                    df['cng'][r], df['rtn'][r], df['snum'][r], df['mktcap'][r],
                    df['bquote'][r], df['squote'][r], df['faceval'][r], df['cunit'][r]
                ]

                cur.execute(query_insert, parms_value)
                conn.commit()

            query_count = '''
                            SELECT COUNT(*) AS obs_cnt
                            FROM KRX_30030
                            WHERE TradeDay = ''' + "'" + str(tdate) + "'" + '''
                          '''
            obs_cnt = pd.read_sql(query_count, conn)['obs_cnt'][0]

            conn.close()
            print('KRX_30030_상장종목현황', '/', tdate, '/', '데이터 삽입 있음', '/', '[', len(df), '/', obs_cnt, ']')

        else:
            print('KRX_30030_상장종목현황', '/', tdate, '/', '데이터 삽입 없음', '/', '[', 0, '/', 0, ']')
            pass

    return


'''
=========================================
ㅁ 크롤링 시계열
    ㅇ 소급적용: 2001.01.02-2018.08.31
=========================================
'''
for year in range(2018, 2019):
    for month in range(1, 13):
        for day in range(1, 32):

            ymd = year * 10000 + month * 100 + day

            if 20181203 <= ymd <= 20181205:
                krx_30030_to_excel(ymd)
                krx_30030_excel_to_sql(ymd)


