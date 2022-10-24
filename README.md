# Data analysis for CDN server population estimation based on CMR model with heterogeneity

## Absract
Data analysis for CDN server population estimation based on CMR model with heterogeneity

Streaming media become more and more popular and important in recent years. Among streaming platforms, Twitch is dominating the game streaming market. In 2021, Twitch had 2,778,000 average concurrent viewers and 105,000 average concurrent streamers.

Similar to other streaming media, Twitch uses Content Delivery Network to provide the service to massive viewers from all around the world. Content Delivery Network (CDN), which is the key part of the streaming system, is crucial for the quality of service.

In the early work, a one-time experiment has been done to survey Twitch's CDN. However, due to the rapid growth of Twitch and the high cost of a detailed scan on CDN, Twitch's CDN remains largely unknown to the public. 

In our previous work, we used the CJS model, which assumes every individual share the same time-dependent survival rate and captures probability, to estimate the CDN size. However, different servers may have different survival rates and capture probability. If we assume every server has its own survival rate and capture probability, the computation overhead of the CJS model may be too high since there are many parameters needed to estimate. Besides, maximum likelihood estimation would have a large bias if the sample size is too small.

In this research, I use the transaction count in hour periods to do clustering on the data from 5 countries and use the CMR model with heterogeneity with these clustering results. Next, I use the S\_Dbw score to evaluate the clustering results. However, I find a better S_Dbw score does not lead to a lower error rate in the MLE-CJS model. Instead, if Avg/Std in the number of sample servers is larger than 0.3 of a cluster, it will tend to have a larger estimation error rate. As a result, the clustering results with a number of clusters less than 5 tend to have a lower estimation error rate since these clustering results contain fewer clusters with Avg/Std larger than 0.3.


## Complete Video Demonstration
1. Data Access: https://youtu.be/z22uhSRdCqw
2. Chapter 5.1 Demo: https://youtu.be/5SienlbZ3mI
3. Chapter 5.2 Demo: https://youtu.be/seR_gY2gQqk

## Structure

### ./Presentation: 
My thesis oral presentation, including .pdf file and .ppt file.

### ./Thesis:
The file of my thesis, including .pdf file and latex source file.

### ./Data:
The file, Introduction of the Data and Data Access.md, in the folder, introduces Twitch's dataset and data access.\
One need to follow the instruction in the folder to get the data before executing the codes in './Program'

### ./Program:
The code I used in my thesis, including .ipynb file and code for the CJS model.

  (1) .ipynb files: The codes for generating the results of figures and tables in my thesis.\
  To run the .ipynb files, one needs to install the Python and Jupyter Notebook and setup the environment.\
  The .ipynb files will use the .csv file in './Data' and the CJS model results in './Result'.\
  Thus, one needs to follow the instruction in './Data' to get the dataset in different regions, and then start to run the program.\
  
  (2) ./ch5_CJS_Estimation_Error: code and script for runnung the CJS model.\
  * ./ch5.1_Preliminaries: run the script in all 3 folder (no_clustering, k_means, mean_shift), 
    and to get the results (ex: p2_daily_plot_sample_hour_00.png and p2_est_result_sample_hour_06.txt)\
  * ./ch5.2_Multiple_KMeans: Before running the script, put the files here to one folder in './Result' (ex: us_period_1). 
    Run the script 'run.sh', and the CJS results will show in the folder './p2_daily_plot' and './p2_est_result'

### ./Result:
The CJS results of the experiment in my thesis. 
It is divided into p0_cluster_result, p1_capture_history, R_capture_probability, p2_daily_plot, and p2_est_result.

1.  p0_cluster_result: The clustering results I generated by k-means or other algorithms.\
It is the input for "kmeans_phase1.py"
2.  p1_capture_history: The capture history is generated by "kmeans_phase1.py".\
It is the iuput for "CJS.R".
3.  R_capture_probability: The capture probability and survival rate are calculated by the CJS.R.\
It is the input for "cheng_kmeans_phase2.py".
4.  p2_daily_plot: The plot of baseline and estimation number of servers on every date.\
It is generated by "cheng_kmeans_phase2.py".
5.  p2_est_result: The estimation error rate, standard deviation, and the runtime of the CJS model.\
It is generated by "cheng_kmeans_phase2.py".

### ./Readme:
This file.

## CJS Model Introduction and Deploy Method

### Introduction

In chapters 5, 6, and 7 of my thesis, I deploy the clustering results to MLE based CJS model on the remote machine, "140.112.42.161".
The CJS model is divided the code into 3 phases, kmeans_phase1.py, CJS.R, and cheng_kmeans_phase2.py.
1. kmeans_phase1.py: read the clustering results in the folder, "p0_cluster_result", and output the capture histories in the folder, "p1_capture_history".
2. CJS.R: use the capture histories as input, and output the survival rates and capture probabilities in the folder, "R_capture_probability".
3. cheng_kmeans_phase2.py: use the capture probability and clustering results to calculate the estimation number, and generate the error rate and daily plot in the folders, "p2_est_result" and "p2_daily_plot".

### Deploy Method
#### ch5.1 Preliminaries
Firstly, use putty to connect to "nslab@140.112.42.161" and change the directory to "~/Desktop/Data-Analysis-for-Twitch-CDN/ch5/ch5.1_Preliminaries".\
Secondly, Run the .sh files in the folders, "k_means", "mean_shift", and "no_clustering", to generate the estimation results of the CJS model.\
Lastly, the estimation error rate will show on the terminal.\
Besides, the estimation result will save as "p2_est_result_sample_hour_{smaple_hour}.txt", and the plot of estimation number and baseline will save as "p2_daily_plot_sample_hour_{smaple_hour}.png"

#### ch5.2 Multiple_KMeans & ch6.2~ch6.5
Before running the codes in ch5.2 Multiple_KMeans, one needs to choose one region folder in "../Result" (ex: France, United_Kingdom).\
Move all the files in this region folder to the same directory with the codes in "ch5.2_Multiple_KMeans".\
The files include "p0_cluster_result", "p1_capture_history", "p2_daily_plot", "p2_est_result", and "R_capture_probability".

Next, the "sample_hour" and dataset of "db" in "kmeans_phase1.py" and "cheng_kmeans_phase2.py" need to be changed by the data you choose.\
The following code blocks, it is an example of the code for us dataset (United_States).

1. sample_hour
```
  sample_hour = ['00', '01']
```

2. dataset
```
  streams = db.United_States.find(...)
```

In the end, check the argv[1] in the script (in the below two lines) and change to the dates you want to deploy.\
For US-0, change the argv[1] to 0, and for US-1, change the argv[1] to 1.
After that, run the script, run.sh, and the results will be generated in the folders, "p2_daily_plot" and "p2_est_result". 

```
python kmeans_phase1.py 1 $n_cluster $loop
```

```
python cheng_kmeans_phase2.py 1 $n_cluster $loop
```

