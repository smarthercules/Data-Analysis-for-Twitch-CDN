from sys import argv
from pymongo import MongoClient
from pprint import pprint 
import csv
import numpy as np
import matplotlib.pyplot as plt

print('kmean phase-2 start...')

dates = []
dates.append(["04-29", "04-30", "05-01", "05-02", "05-03", "05-04", "05-05"])
dates.append(["05-07", "05-08", "05-09", "05-10", "05-11", "05-12", "05-13", "05-14", "05-15", "05-16"])
date = dates[int(argv[1])]

period_choose = argv[1]

streams_end_date = []
streams_end_date.append("05-06")
streams_end_date.append("05-17")
end_date = streams_end_date[int(argv[1])]

sample_hour_options = [['00', '01'], ['06', '07'], ['12', '13'], ['18', '19']] # [start, end]
sample_hour = sample_hour_options[int(argv[2])]
print(f'sample_hour: {sample_hour}')

num_cluster = 1

# R_capture_p format transform
def r_label_2_p2(n_cluster=1):
    file_path = f'./r_no_clustering.txt'
    with open(file_path) as f:
        lines = f.readlines()
    # locate the p
    start=100000
    end=0
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(lines)):
        if lines[i][:2] == '$p':
            start=i+1
        elif lines[i] == lines[-3]:
            end=i
    CJS_time_use = float(lines[-1][19:-6])
    # record class, time, est
    time_record = []
    est_record = [] # ex: 6.197041e-01
    for line in lines[start+1:-2]:
        print(line)
        if line[4] in numbers: # period-0
            time_record.append(int(line[4:6]))
        elif line[5] in numbers: # period-1
            time_record.append(int(line[5:7]))
        else:
            time_record.append(int(line[6]))
        est_record.append(float(line[11:-1]))
    #print(f'time_record: {time_record}')
    num_cluster = 1
    time_len = len(date)-1 # time = 2 ~ last date
    #print(f'num_cluster: {num_cluster}, time_len: {time_len}')
    est_p_sort = [] # [[], []] num of class = num of list()
    for j in range(time_len):
        est_p_sort.append(1) # est num will be 'INF' if append '0' and some data not load 
    for i in range(len(time_record)):
        est_p_sort[time_record[i]-2] = est_record[i]

    return est_p_sort, CJS_time_use

# phase-2
client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')
streams = db.United_States.find({ "start": { "$lt": "2021-"+end_date+"T00:00:00"}, "end": { "$gte": "2021-"+date[0]+"T00:00:00"}})

ip_list = list()
for s in streams:
    for ip in s["addrPool"]:
        if ip not in ip_list:
            ip_list.append(ip)

file_cluster = f'./p0_no_clustering.csv'
ip_group_dict = {} # {52.223.242.228: class_1}
with open(file_cluster, newline='') as csvfile: # open(argv[1], newline='')
    rows = csv.reader(csvfile)
    for row in rows:
        if row[2] not in ip_list:
            continue
        ip_group_dict[row[2]] = row[1]
server_num_each_day = []
for d in date:
    streams = db.United_States.find({ "start": { "$lte": "2021-"+d+"T23:59:59" }, "end": { "$gte": "2021-"+d+"T00:00:00" }})
    cur_ip_list = list()
    for s in streams:
        for (tm, ip) in s["transactionList"].items():
            if tm >= "2021-"+d+"T00:00:00" and tm <= "2021-"+d+"T23:59:59":
                if ip not in cur_ip_list:
                    cur_ip_list.append(ip)
    server_num_each_day.append(len(cur_ip_list))
server_num_each_day = np.array(server_num_each_day)
print(f'server_num_each_day: {server_num_each_day}')

baseline_with_cluster = []
for i in range(num_cluster):
    baseline_with_cluster.append([])

for i, d in enumerate(date):
    streams = db.United_States.find({ "start": { "$lte": "2021-"+d+"T23:59:59" }, "end": { "$gte": "2021-"+d+"T00:00:00" }})
    cur_ip_list = list()
    for s in streams:
        for (tm, ip) in s["transactionList"].items():
            if tm >= "2021-"+d+"T00:00:00" and tm <= "2021-"+d+"T23:59:59":
                if ip not in cur_ip_list:
                    cur_ip_list.append(ip)
    c_123 = []
    for i in range(num_cluster):
        c_123.append(0)
    for ip in cur_ip_list:
        _class = int(ip_group_dict[ip][-1])-1 # KeyError: '52.223.244.187'
        c_123[_class] += 1 # index err: index out of range
    for i in range(num_cluster):
        baseline_with_cluster[i].append(c_123[i])

sample_with_cluster = []
for i in range(num_cluster):
    sample_with_cluster.append([])

for i, d in enumerate(date):
    streams = db.United_States.find({ "start": { "$lte": "2021-"+d+"T"+sample_hour[-1]+":00:00" }, "end": { "$gte": "2021-"+d+"T"+sample_hour[0]+":00:00" }})
    cur_ip_list = list()
    for s in streams:
        for (tm, ip) in s["transactionList"].items():
            if tm >= "2021-"+d+"T"+sample_hour[0]+":00:00" and tm <= "2021-"+d+"T"+sample_hour[-1]+":00:00":
                if ip not in cur_ip_list:
                    cur_ip_list.append(ip)
    c_123 = []
    for i in range(num_cluster):
        c_123.append(0)
    for ip in cur_ip_list:
        _class = int(ip_group_dict[ip][-1])-1
        c_123[_class] += 1
    for i in range(num_cluster):
        sample_with_cluster[i].append(c_123[i])

capturing_p, CJS_time_use = r_label_2_p2()
print(f'capturing_p: {capturing_p}')

baseline_with_cluster = np.array(baseline_with_cluster)
sample_with_cluster = np.array(sample_with_cluster)
capturing_p = np.array(capturing_p)
estimation_with_cluster = sample_with_cluster[:, 1:] / capturing_p
estimation_sum = np.sum(estimation_with_cluster, axis=0)

err = np.mean(np.abs( estimation_sum[1:-2] - server_num_each_day[2:-2] ) / server_num_each_day[2:-2])
std = np.std(np.abs( estimation_sum[1:-2] - server_num_each_day[2:-2] ) / server_num_each_day[2:-2])
output_path = f'./p2_no_clustering_sample_hour_{sample_hour[0]}.txt'
f = open(output_path, 'w')
f.write(f'err: {err}\n')
f.write(f'std: {std}\n')
f.write(f'CJS time: {CJS_time_use}')
f.close()
print(f'estimation_server_num: {estimation_sum}')
print(f'error rate: {err}')

# output daily estimation plot
x_axis = date[1:-1]
y_axis = server_num_each_day[1:-1]
y_axis1 = estimation_sum[:-1]
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_xlabel("Day", fontsize=24)
ax.set_ylabel("Number of Servers", fontsize=24)
plt.axis([None, None, 0, 600])
plt.plot(x_axis, y_axis, "o-", markersize=12, linewidth=3, color="k", label="baseline", alpha=0.7)
plt.plot(x_axis, y_axis1, "o-", markersize=12, linewidth=3, color="b", label="MLE-CJS", alpha=0.7)
ax.set_xticks(np.arange(0,len(server_num_each_day),1))
ax.set_yticks(np.arange(0,1200,50))
ax.grid(which="both")
leg = ax.legend(fontsize=20)
ax.tick_params(axis="both", which='major', labelsize=20)
plot_path = f'./p2_no_clustering_sample_hour_{sample_hour[0]}.png'
plt.savefig(plot_path)

print('finish plot\n')