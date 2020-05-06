a={"reason":"查询成功!","result":
    {"city":"武穴","realtime":
        {"temperature":"13","humidity":"99","info":"中雨",
         "wid":"08","direct":"西北风","power":"2级","aqi":"73"},
     "future":[{"date":"2020-04-20","temperature":"13\/17℃","weather":
         "小雨","wid":{"day":"07","night":"07"},"direct":"西北风"},
               {"date":"2020-04-21","temperature":"12\/19℃","weather":"小雨转多云","wid":{"day":"07","night":"01"},"direct":"东北风转东风"},
     {"date":"2020-04-22","temperature":"13\/18℃","weather":"晴转多云","wid":
         {"day":"00","night":"01"},"direct":"东风"},{"date":"2020-04-23",
    "temperature":"9\/17℃","weather":"阴","wid":{"day":"02","night":"02"},
"direct":"东风转西风"},{"date":"2020-04-24","temperature":"10\/19℃","weather":"多云转晴",
                   "wid":{"day":"01","night":"00"},"direct":"西风"}]},"error_code":0}

print(type(a))

import json
d_json=json.dumps(a,indent=4)
print(type(d_json))












