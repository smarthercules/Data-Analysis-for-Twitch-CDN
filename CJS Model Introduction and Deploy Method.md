# CJS Model Introduction and Deploy Method

## Introduction

In the chapter 5, 6, and 7 of my thesis, I deploy the clustering results to MLE based CJS model on the remote machine, "140.112.42.161".
The CJS model is divided the code into 3 phase, kmeans_phase1.py, CJS.R, and cheng_kmeans_phase2.py.\
1. kmeans_phase1.py: read the clustering results in the folder, "p0_cluster_result", and output the capture histories in the folder, "p1_capture_history".
2. CJS.R: use the capture histories as input, and output the survival rates and capture probabilities in the folder, "R_capture_probability".
3. cheng_kmeans_phase2.py: use the capture probability and clustering results to calculate the estimation number, and generate error rate and daily plot in the folders, "p2_est_result" and "p2_daily_plot".

## Deploy Method
### ch5.1 Preliminaries
Firstly, use putty to connect to "nslab@140.112.42.161".\
Change the directory to "~/Desktop/Data-Analysis-for-Twitch-CDN/ch5/ch5.1_Preliminaries".\
Run the .sh files in the folders, "k_means", "mean_shift", and "no_clustering", to generate the estimation results of the CJS model.\
The estimation error rate will show on the terminal.\
Besides, the estimation result will save as "p2_est_result_sample_hour_{smaple_hour}.txt", and the plot of estimation number and baseline will save as "p2_daily_plot_sample_hour_{smaple_hour}.png"

### ch5.2 Multiple_KMeans & ch6.2~ch6.5
Before run the codes in ch5.2 Multiple_KMeans, one needs to choose one region folder in "../Rusult" (ex: France, United_Kingdom).\
Move the all the files in this region folder to the same directory with the codes in "ch5.2_Multiple_KMeans".\
The files include "p0_cluster_result", "p1_capture_history", "p2_daily_plot", "p2_est_result", "R_capture_probability", and "random_nc_2to8".

Next, the "sample_hour" and dataset of "db" in "kmeans_phase1.py" and "cheng_kmeans_phase2.py" need to be changed by the data you choose.\
In the following code blocks, it is an example for the code for us dataset (United_States).

1. sample_hour
```
  sample_hour = ['00', '01']
```

2. dataset
```
  streams = db.United_States.find(...)
```

In the end, run the srcipt, run.sh, and the results will be generated in the folders, "p2_daily_plot" and "p2_est_result". 
