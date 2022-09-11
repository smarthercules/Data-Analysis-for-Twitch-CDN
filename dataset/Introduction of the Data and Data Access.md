# Introduction of the Data and Data Access

## Introduction of the Data

Our lab member, Wang, implemented the crawler by using Twitch’s API and VPN server to collect the CDN data from different regions. The crawler chose the top K channels that account for 80% of the total viewers.

The data is stored in MongoDB, and the dataset in MongoDB is divided into several collections that each represent VPN servers in one country. 

In my research, I picked the data from 'United_States', 'United_Kingdom', 'France', 'Netherlands', and 'Germany', which have larger data sizes than those from other countries.

## Data Access
1. Use SSH to connect to the server, "140.112.42.161".
2. Change the variable 'loc' in 'load_csv.py' to the data you want to choose. (The option of locations is shown below. [note 1]) 
3. Run 'load_csv.py'
4. The program, 'load_csv.py', will create the data file as, './dataset/{loc}.csv'.

[note 1]
location = 'Taiwan', 'Russian', 'Brazil', 'Ukraine', 'South_Korea', 'Spain', 'United_Kingdom', 'Canada', 'France', 'Netherlands', 'Germany', 'Japan', 'Australia', 'Denmark', 'Poland', 'Sweden', 'Italy', 'Turkey', 'United_States', 'SouthKorea'
