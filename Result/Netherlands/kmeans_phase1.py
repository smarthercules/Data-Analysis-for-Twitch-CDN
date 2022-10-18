from sys import argv
from pymongo import MongoClient
from pprint import pprint 
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sys import argv

dates = []
dates.append(["06-18", "06-19", "06-20", "06-21", "06-22", "06-23", "06-24", "06-25", "06-26", "06-27"])
dates.append(["06-30", "07-01", "07-02", "07-03", "07-04", "07-05", "07-06", "07-07", "07-08", "07-09", "07-10", "07-11", "07-12", "07-13"])
date = dates[int(argv[1])]
print(f'date: {date}')

period_choose = argv[1]

streams_end_date = []
streams_end_date.append("06-28")
streams_end_date.append("07-14")
end_date = streams_end_date[int(argv[1])]

_num_cluster     = argv[2]
_label = argv[3]

sample_hour = ['19', '20'] # [start, end]

client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')
# date need to change
streams = db.Netherlands.find({ "start": { "$lt": "2021-"+end_date+"T00:00:00"}, "end": { "$gte": "2021-"+date[0]+"T00:00:00"}})

ip_list = list()
for s in streams:
    for ip in s["addrPool"]:
        if ip not in ip_list:
            ip_list.append(ip)
print(len(ip_list))

ip_group_dict = {}
file_cluster = f'./p0_cluster_result/period_{period_choose}/n_cluster_{argv[2]}/label_{argv[3]}.csv'
print(f'cluster: {file_cluster[20:]}')
with open(file_cluster, newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if row[2] not in ip_list:
            continue
        ip_group_dict[row[2]] = row[1]

# can change sample hour
ip_dict = dict.fromkeys(ip_list, "")
for d in date:
    streams = db.Netherlands.find({ "start": { "$lte": "2021-"+d+"T"+sample_hour[-1]+":00:00" }, "end": { "$gte": "2021-"+d+"T"+sample_hour[0]+":00:00" }})
    cur_ip_list = list()
    for s in streams:
        for (tm, ip) in s["transactionList"].items():
            if tm >= "2021-"+d+"T"+sample_hour[0]+":00:00" and tm <= "2021-"+d+"T"+sample_hour[1]+":00:00":
                if ip not in cur_ip_list:
                    cur_ip_list.append(ip)
    for ip in ip_list:
        if ip in cur_ip_list:
            ip_dict[ip] += "1"
        else:
            ip_dict[ip] += "0"

ip_and_ch = ip_dict.items()
ip_ch_rec = []
ip_group = []
for (ip, ch) in ip_and_ch:
    if ch == "0"*len(date):
        continue
    ip_ch_rec.append(ch)
    ip_group.append(ip_group_dict[ip])

output_ch_rec = f'./p1_capture_history/period_{period_choose}/n_cluster_{_num_cluster}/label_{_label}.txt'
f = open(output_ch_rec, 'w')
for ch in ip_ch_rec:
    f.writelines(f'{ch}\n')
f.close()

output_ip_group = f'./p1_capture_history/period_{period_choose}/n_cluster_{_num_cluster}/group_label_{_label}.txt'
f = open(output_ip_group, 'w')
for group in ip_group:
    f.writelines(f'{group}\n')
f.close()
