from pymongo import MongoClient 
from pprint import pprint
import csv

client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')
# location = ['Taiwan', 'Russian', 'Brazil', 'Ukraine', 'South_Korea',
#             'Spain', 'United_Kingdom', 'Canada', 'France', 'Netherlands',
#             'Germany', 'Japan', 'Australia', 'Denmark', 'Poland',
#             'Sweden', 'Italy', 'Turkey', 'United_States', 'SouthKorea']
#print(db.list_collection_names()) 

data_dict = dict()
loc = 'us'
for x in db.United_States.find():
    data_dict[x['_id']] = x
print(f'loc={loc}, count={len(data_dict)}')


filename = f'./{loc}.csv'
with open(filename, 'w', newline='') as csvfile:
  fieldnames = ['_id', 'vpnServerId', 'channel', 'end', 'language', 'serverPool', 'start', 'transactionList', 'addrPool', 'viewerList']

  # 將 dictionary 寫入 CSV 檔
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # 寫入第一列的欄位名稱
  writer.writeheader()

  # 寫入資料
  for key, value in data_dict.items():
    writer.writerow(value)