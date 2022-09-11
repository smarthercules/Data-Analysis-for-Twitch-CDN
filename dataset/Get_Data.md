# Introduction of the Data and Data Access

## Introduction of the Data

Our lab member, Wang, implemented the crawler by using Twitch’s API and VPN server to collect the CDN data from different regions. The crawler chose the top K channels that account for 80% of the total viewers.

The data is stored in MongoDB, and the dataset in MongoDB is divided into several collections that each represent VPN servers in one country. 
