import datetime
import time


day_time = time.strftime("%H%M", time.localtime(time.time()))
print(day_time)
print("==="*10)

cur_time = datetime.datetime.now()
cur_time = cur_time.strftime("%Y%m%d %H%M")
ymd = cur_time.split(" ")[0]
print(ymd)
print(cur_time)
print(cur_time.split(" ")[1])
# day_time = datetime.datetime.now().strftime("%H%M")
# print(day_time)
# yymmdd = day_time.strftime("%Y%m%d")
# print(yymmdd)
# cur_day = datetime.datetime.now()
# print(cur_day)
# yymmdd = cur_day.strftime("%Y%m%d")
# print(yymmdd)
# day_time = cur_day.strftime("%H%M")
# print(HM)
# cur_time_min = cur_day.strftime("%M")
# # print(cur_time)
# print(cur_time_min)
# # print(cur_time)
# # print(cur_day.strftime("%H%M"))
# past_15 = cur_day - datetime.timedelta(minutes=15)

# print(past_15)