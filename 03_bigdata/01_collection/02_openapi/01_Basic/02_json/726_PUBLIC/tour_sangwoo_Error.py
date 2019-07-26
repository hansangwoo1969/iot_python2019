import urllib.request
import datetime
import json
import math
# 서비스명: 관광자원통계서비스
access_key = \
    "XCeRmN%2B%2BubaLKjj%2BA8W%2Bx1QghqjBqMqJRZYXcFRhJiZ%2BZJUOH%2FPvWvsc8mcBE0M9YUC7T0iJ9LM%2FjWg2cD2o9Q%3D%3D"
def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

#[CODE 1]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):
    end_point =\
        "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList "

    parammeters = "?_type=json&serviceKey="+access_key    # must_have
    parammeters += "&YM="+yyyymm
    parammeters += "&SIDO="+urllib.parse.quote(sido)
    parammeters += "&GUNGU="+urllib.parse.quote(gungu)
    parammeters += "&RES_NM=&pageNo="+str(nPagenum)
    parammeters += "&numOfRows="+str(nItems)            # must_have

    url = end_point + parammeters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 2]
def getTourPointData(item, yyyymm, jsonResult):
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm'  not in item.keys() else item['resNm' ]
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatNum' not in item.keys() else item['csNatNum']

    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd, 'gungu': gungu, 'sido': sido,
                       'resNm': resNm, 'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})
    return

def main():
    jsonResult = []

    sido = '서울특별시'
    gungu = ''
    nPagenum = 1
    nTotal = 0
    nItems = 100
    nStartYear = 2013
    nEndYear = 2019

    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            yyyymm = "{0} {1:0>2}".format(str(year), str(month))
            nPagenum = 1

            #[CODE 3]
            while True:
                jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)

                if(jsonData['response']['header']['resultMsg'] == 'OK'):
                    nTotal = jsonData['response']['body']['totalCount']

                    if nTotal == 0:
                        break
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)

                    nPage = math.ceil(nTotal/100)

                    if (nPagenum == nPage):
                        break

                    nPagenum += 1
                else:
                    break
    with open('%s_관광지입장정보_%d_%d.json' % (sido, nStartYear,nEndYear-1), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print("%s_관광지입장정보_%d_%d.json SAVED" % (sido, nStartYear, nEndYear-1))

if __name__ == '__main__':
    main()

