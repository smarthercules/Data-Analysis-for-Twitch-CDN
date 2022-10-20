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
dates.append(["04-29", "04-30", "05-01", "05-02", "05-03", "05-04", "05-05"])
dates.append(["05-07", "05-08", "05-09", "05-10", "05-11", "05-12", "05-13", "05-14", "05-15", "05-16"])
date = dates[int(argv[1])]
print(f'date: {date}')

period_choose = argv[1]

streams_end_date = []
streams_end_date.append("05-06")
streams_end_date.append("05-17")
end_date = streams_end_date[int(argv[1])]

#sample_hour_options = [['11', '12'], ['12', '13'], ['13', '14'], ['14', '15'], ['15', '16'], ['16', '17'], ['17', '18'], ['18', '19'], ['19', '20'], ['20', '21']] # [start, end]

sample_hour_options = [['00', '01'], ['06', '07'], ['12', '13'], ['18', '19']] # [start, end]
sample_hour = sample_hour_options[int(argv[2])]
print(f'sample_hour: {sample_hour}')


client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')
streams = db.United_States.find({ "start": { "$lt": "2021-"+end_date+"T00:00:00"}, "end": { "$gte": "2021-"+date[0]+"T00:00:00"}})

ip_list = list()
for s in streams:
    for ip in s["addrPool"]:
        if ip not in ip_list:
            ip_list.append(ip)
print(len(ip_list))

ip_group_dict = {}
file_cluster = f'./p0_k_means.csv'
with open(file_cluster, newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if row[2] not in ip_list:
            continue
        ip_group_dict[row[2]] = row[1]

ip_dict = dict.fromkeys(ip_list, "")
for d in date:
    streams = db.United_States.find({ "start": { "$lte": "2021-"+d+"T"+sample_hour[-1]+":00:00" }, "end": { "$gte": "2021-"+d+"T"+sample_hour[0]+":00:00" }})
    cur_ip_list = list()
    for s in streams:
        for (tm, ip) in s["transactionList"].items():
            if tm >= "2021-"+d+"T"+sample_hour[0]+":00:00" and tm <= "2021-"+d+"T"+sample_hour[-1]+":00:00":
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

output_ch_rec = f'./p1_label.txt'
f = open(output_ch_rec, 'w')
for ch in ip_ch_rec:
    f.writelines(f'{ch}\n')
f.close()

output_ip_group = f'./p1_group_label.txt'
f = open(output_ip_group, 'w')
for group in ip_group:
    f.writelines(f'{group}\n')
f.close()

print('kmean phase-1 end.\n')