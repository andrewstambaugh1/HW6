import sys
import requests
import json
import time
year=sys.argv[1]
keys=[]
# lol I got tired of the range function looping through the wrong range so I did the list manually
for month in [1,2,3,4,5,6,7,8,9,10,11,12]:
    url= f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=diXA7xTCzlG1w1GQGaQcmdDO2DnPKLT3"
    r=requests.get(url).text
    res=json.loads(r)
    for i in res['response']['docs']:
        for j in range(0,len(i['keywords'])):
            keys.append(i['keywords'][j]['value'])
    ## to prevent from calling API too fast
    time.sleep(5)

for i in keys:
    print(i)
