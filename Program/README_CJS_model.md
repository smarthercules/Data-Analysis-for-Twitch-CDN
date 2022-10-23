# CJS Model

## Introduction

In the chapter 5, 6, and 7 of my thesis, I deploy the clustering results to MLE based CJS model. We use the package "marked" in r.
We divide the code into 3 phase, kmeans_phase1.py, CJS.R, cheng_kmeans_phase1.py.
And run codes on the remote machine, "140.112.42.161".

## Deploy Method
### ch5.1 Preliminaries
Run the .sh files in the folder to generate the estimation results of the CJS model.\
The estimation error rate will show on the terminal.\
Besides, the estimation result will save as "p2_est_result_sample_hour_{smaple_hour}.txt", and the plot of estimation number and baseline will save as "p2_daily_plot_sample_hour_{smaple_hour}.png"

### ch5.2 Multiple_KMeans
Before run the codes in ch5.2 Multiple_KMeans, one needs to choose one the folder in "../Rusult", and the files should be to the same directory with the codes in "ch5.2_Multiple_KMeans".

Next, the "sample_hour" and dataset of "db" in "kmeans_phase1.py" and "cheng_kmeans_phase2.py" need to be changed by the data you choose.\
In the following code blocks, it is an example for the code for us dataset (United_States).\

1. sample_hour
```
  sample_hour = ['00', '01']
```

2. dataset
```
  streams = db.United_States.find(...)
```

### ch6.2 ~ ch6.
