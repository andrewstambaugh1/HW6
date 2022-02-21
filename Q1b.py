import sys
import requests
import json
with open(sys.argv[1]) as f:
    lines = f.readlines()
doc=lines
cnt = {}
for i in doc:
    if i.split('\n')[0] not in cnt:
        cnt[i.split('\n')[0]]=1
    else:
        cnt[i.split('\n')[0]]+=1


sorted_cnt = sorted(cnt.items(), key = lambda kv: kv[1], reverse=True)
for i in sorted_cnt[0:10]:
    print(str(i[0]+','), i[1])

print('\n')
