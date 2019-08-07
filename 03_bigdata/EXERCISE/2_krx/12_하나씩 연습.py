import pyodbc
import time
import sqlite3 as sq
import requests
import numpy as np
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta

DATABASE = 'C:\\Users\\hansangwoo2\\Documents\\blog\\KRXDB.db'


def krx_short_trading(p_sday, p_eday, p_mktidx):
    sday = p_sday  # 조회시작일
    eday = p_eday  # 조회종료일

    # if todate == None:
    #     todate = datetime.today().strftime('%Y%m%d')  # 오늘 날짜
    #
    # if fromdate == None:
    #     todate = datetime.today().strftime('%Y%m%d')  # 오늘 날짜
    #     # fromdate = (datetime.today() - timedelta(days=30)).strftime('%Y%m%d')  # 30일 이전 날짜

    mktidx = p_mktidx  # 시장구분

    if p_mktidx == 1:  # 1 = 유가증권(종목)
        mktidx = 1
    elif p_mktidx == 2:  # 2 = 코스닥(종목)
        mktidx = 3
    elif p_mktidx == 3:  # 3 = 코넥스(종목)
        mktidx = 4
    else:  # 9 = 유가증권(증권상품)
        mktidx = 2

    gen_req_url = "http://short.krx.co.kr/contents/COM/GenerateOTP.jspx"
    query_str_parms = {
        'name': 'fileDown',
        'filetype': 'xls',
        'url': 'SRT/02/02020100/srt02020100',
        'mkt_tp_cd': str(mktidx),
        'isu_cdnm': '전체',
        'isu_cd': '',
        'isu_nm': '',
        'isu_srt_cd': '',
        'strt_dd': str(sday),
        'end_dd': str(eday),
        'pagePath': '/contents/SRT/02/02020100/SRT02020100.jsp'
    }

    r = requests.get(gen_req_url, query_str_parms)
    time.sleep(2.0)

    gen_req_url = "http://file.krx.co.kr/download.jspx"

    headers = {
        'Referer': 'http://short.krx.co.kr/contents/SRT/02/02020100/SRT02020100.jsp'
    }

    form_data = {
        'code': r.content
    }

    r = requests.post(gen_req_url, form_data, headers=headers)
    time.sleep(2.0)

    df = pd.read_excel(BytesIO(r.content), thousands=',')

    # 필드명 변경 (한글 -> 영어) ,,   안해도 될 듯,,,
    df = df.rename({
        '일자': 'tdate',
        '종목코드': 'code',
        '종목명': 'name',
        '공매도거래량': 'short_vol',
        '총거래량': 'tradvol',
        '비중': 'svolratio',
        '공매도거래대금': 's_tradval',
        '총거래대금': 'tradval',
        '비중.1': 'svalratio'},
        axis='columns'
    )
    df['tdate'] = df['tdate'].str.replace('/', '')  # yyyy/mm/dd -> yyyymmdd
    # df['mktidx'] = p_mktidx

    if len(df) >= 1:
        print(sday, '/', eday, p_mktidx, '/', '데이터 있음')

    else:
        print(sday, '/', eday, p_mktidx, '/', '데이터 없음')

    file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
    file_name = 'KRX_80163_' + str(eday) + '.xlsx'

    # df.to_excel(file_dir + file_name)
    df.to_excel(file_dir + file_name, index=False, index_label=None)  # 인덱스 배제된 저장
    print('KRX_80163_종목별공매도거래현황_크롤링 완료', p_eday)

    return df


def krx_short2db(p_date):

    s_edate = p_date

    # if len(df) > 1:
    file_dir = 'C://Users//hansangwoo2//Desktop//TEST//'
    file_name = 'KRX_80163_' + str(s_edate) + '.xlsx'

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

            insert_query = (
                """
                INSERT INTO KRX_80163_FS(
                         [일자],     [코드],      [종목명],   [공매도거래량], 
                         [총거래량], [공매도비율], [공매도금액],[총거래금액], 
                         [공매도금액비율], [마켓], [IPUSER], [IPDATE])
        
                VALUES   (?,       ?,     ?,      ?,
                          ?,       ?,     ?,      ?,
                          ?,       ?, '한상우', DATE())
                """)

            # kor['mktidx'] = kor['mktidx'].astype(str)  # 시장구분 변수 숫자형 -> 문자형
            float_list = [ '공매도거래량', '총거래량', '공매도금액', '총거래금액']
            for f in range(len(float_list)):
                float_col = float_list[f]
                df[float_col] = float(df[float_col])
                #df[float_col] = df[float_col].astype(float)

            for i in range(len(df)):
                일자 = df['tdate'][i]
                코드 = df['code'][i]
                종목명 = df['name'][i]
                공매도거래량 = df['short_vol'][i]
                총거래량 = df['tradvol'][i]
                공매도비율 = df['svolratio'][i]
                공매도금액 = df['s_tradval'][i]
                총거래금액 = df['tradval'][i]
                공매도금액비율 = df['svalratio'][i]
                마켓 = df['mktidx'][i]

                parms_value = [일자, 코드, 종목명, 공매도거래량, 총거래량, 공매도비율, 공매도금액, 총거래금액, 공매도금액비율, 마켓]

                # conn = sq.connect(DATABASE)
                cur = conn.cursor()
                cur.execute(insert_query, parms_value)
                conn.commit()

            tdate = df['tdate'][0]

            query_count = '''
                        SELECT COUNT(*) AS obs_cnt
                        FROM KRX_80163_FS
                        WHERE 일자 = ''' + "'" + str(tdate) + "'" + '''
                        '''
            cnt = pd.read_sql(query_count, conn)['obs_cnt'][0]

            conn.close()
            print('[', len(kor), '/', cnt['obs_cnt'][0], ']', '일자: ', tdate, 'insert successfully')

    #else:
    #    print('데이터가 없습니다.')
    #    pass

    return


for year in range(2018, 2019):
    for month in range(1, 13):
        for day in range(1, 32):

            ymd = year * 10000 + month * 100 + day * 1  # yymmdd

            if ymd <= 20180102:
                ksp = krx_short_trading(ymd, ymd, 1)
                ksq = krx_short_trading(ymd, ymd, 2)
                kns = krx_short_trading(ymd, ymd, 3)

                frames = [ksp, ksq, kns]
                kor = pd.concat(frames)
                # krx_short2db(ymd)
                # print(kor)
                # kor.reset.index(drop=True, inplace = True) # 'df' has no attribute 'reset'




